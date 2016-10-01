# -*- coding: UTF-8 -*-
import chardet as cd
import pynlpir
from itertools import islice
from copy import *
from numpy import *
from collections import Counter


####读入文件进行分词####
#输入：文件名（绝对路径）（string）
#输出：分词结果 （list）
def separateWordFromFile(fileName):
	pynlpir.open()
	file = open(fileName,'r')
	lines = file.readlines()
	i = 0
	allSegmentResult = []
	#print type(s)
	label = []
	for line in lines:
		i = i+1
		textsegment = line
		if textsegment == "\n":
			print "skip"
			continue
		##note:
		'''   gbk 转 utf-8时，    
		   gbk --> unicode --> utf-8
           分解为两个步骤，
                   1.    gbk --> unicode
                             python 语法：你的字符串.decode("gbk")
                   2.    unicode --> utf-8
                            python 语法：你的字符串.decode("gbk").encode("utf-8")
		'''

		segmentResult = pynlpir.segment(textsegment,pos_tagging=True)
		newSegmentResult = removePunctuation(segmentResult)
		allSegmentResult.append(newSegmentResult)

	print len(allSegmentResult)
	file.close()
	pynlpir.close()	
	#print label
	return allSegmentResult

    
 
####去除分词工具分词后留下的词性信息####
#输入：分词结果 （list）
#输出：去除词性后的分词结果 （list）
def removePunctuation(segmentResult):
	NewSegmentResult = deepcopy(segmentResult)
	for everyone in NewSegmentResult:
		if (everyone[1]==u'punctuation mark' or everyone[1]== None):
			NewSegmentResult.remove(everyone)
	newSegmentResult = [everyeum[0] for everyeum in NewSegmentResult]
	return newSegmentResult
	
    
 
####分词结果输出到文件（utf8格式）####
#输入：文件名（string），分词结果 （list）
#输出：无    
def output2File(FileName,wordList):	#输出到文件看看分词结果如何
	f =  open(FileName,'w')
	WriteText = []
	for everyrow in wordList:
		#print everyrow
		for everycolumn in everyrow:
			#print everycolumn
			WriteText.append((str(everycolumn.encode('utf-8'))+' '))
		WriteText.append('\n')
	f.writelines(WriteText)
	f.close()
def output2File_label(FileName,labelList):	#输出到文件看看分词结果如何
	f =  open(FileName,'w')
	WriteText = []
	for everynum in labelList:
		WriteText.append((str(everynum)))
		WriteText.append('\n')
	f.writelines(WriteText)
	f.close()
    
	
def output2File_highFre(FileName,labelList):	#输出到文件看看分词结果如何
	f =  open(FileName,'w')
	WriteText = []
	for everynum in labelList:
		WriteText.append((str(everynum.encode('utf-8'))))
		WriteText.append('\n')
	f.writelines(WriteText)
	f.close()
	
####消除停用词####
#输入：文件名（string），未去除停用词的分词结果（list）
#输出：去除停用词的分词结果（list）
def cutStopWord(fileName,rawCorpus):	#消除停用词
	file = open(fileName,'r')
	lines = file.readlines()
	stopwoedlist = []
	TCorpus = deepcopy(rawCorpus)
	for line in lines:
		#print line.decode('gbk')
		stopwoedlist.append(line.strip('\n').decode('utf-8'))
		#print stopwoedlist
	
	for row in TCorpus:
		for word in row:
			if word in stopwoedlist:
				row.remove(word)
	return TCorpus
	
	
####消除高频词####
#输入：高频词列表（list），未去除高频词的分词结果（list）
#输出：去除高频词的分词结果（list）		
def cutHighFreWord(highFreWordList,rawCorpus):	#消除高频词
	TCorpus = deepcopy(rawCorpus)
	for row in TCorpus:
		for word in row:
			if word in highFreWordList:
				row.remove(word)
	return TCorpus
    
	
####统计高频词，为消除高频词做准备####
#输入：未去除高频词的分词结果（list），统计最高频的词的个数（int）
#输出：高频词列表（list）		    
def highFreStatistic(allSegmentResult,wordNumber):
	highFreWord = []
	TSeg = []
	for row in allSegmentResult:
		TSeg.extend(row)
	wordDictionary = Counter(TSeg)
	#print wordDictionary
	wordSorted = sorted(wordDictionary.items(), key=lambda d:d[1],reverse=True)
	#print wordSorted[-10:-1]
	for i in range(wordNumber):
		highFreWord.append(wordSorted[i][0])	#取出高频词
	#print highFreWord
	return highFreWord


	
def highFreStatistic2File(allSegmentResult,wordNumber,FileName):
	highFreWordList = highFreStatistic(allSegmentResult,wordNumber)
	output2File_highFre(FileName,highFreWordList)


if __name__ == '__main__':
	cutStopWord_or_not = 0
	cutHighFreWord_or_not = 0
	highFreStatistic2File_or_not = 0
	cutHighFreWord_num = 200
	sourceFilePosition = r"D:\NLP_exLab\pythonCode\CNN\data\hotel_annotatedData_utf8\new_style_data\\"
	aimFilePostion = r"D:\NLP_exLab\pythonCode\CNN\data\hotel_annotatedData_utf8\sepWord_result\\"
	
	allSegmentResult = separateWordFromFile(sourceFilePosition+"hotelNeg2443.txt")
		
	allSentence = allSegmentResult
		
	if cutStopWord_or_not == 1:
		allSentence = cutStopWord(sourceFilePosition+'stopword1208.txt',allSentence) #这里一般为"stopword1208"
	if cutHighFreWord_or_not == 1:
		allSentence = cutHighFreWord(highFreStatistic(allSentence,cutHighFreWord_num),allSentence)		
	
	output2File(aimFilePostion+'Segment_result_hotel_neg.txt' ,allSentence)
		
	if highFreStatistic2File_or_not == 1:
		highFreFileName = 'highFreWord_neg.txt'
		highFreStatistic2File(allSubjectSentence,cutHighFreWord_num,sourceFilePosition + highFreFileName)
	
	allSegmentResult = separateWordFromFile(sourceFilePosition+"hotelPos2322.txt")
		
	allSentence = allSegmentResult
		
	if cutStopWord_or_not == 1:
		allSentence = cutStopWord(sourceFilePosition+'stopword1208.txt',allSentence) #这里一般为"stopword1208"
	if cutHighFreWord_or_not == 1:
		allSentence = cutHighFreWord(highFreStatistic(allSentence,cutHighFreWord_num),allSentence)		
	
	output2File(aimFilePostion+'Segment_result_hotel_pos.txt' ,allSentence)
		
	if highFreStatistic2File_or_not == 1:
		highFreFileName = 'highFreWord_pos.txt'
		highFreStatistic2File(allSubjectSentence,cutHighFreWord_num,sourceFilePosition + highFreFileName)
