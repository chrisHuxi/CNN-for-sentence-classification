# -*- coding: UTF-8 -*-
import chardet as cd
import pynlpir
from itertools import islice
from copy import *
from numpy import *
from collections import Counter


####�����ļ����зִ�####
#���룺�ļ���������·������string��
#������ִʽ�� ��list��
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
		'''   gbk ת utf-8ʱ��    
		   gbk --> unicode --> utf-8
           �ֽ�Ϊ�������裬
                   1.    gbk --> unicode
                             python �﷨������ַ���.decode("gbk")
                   2.    unicode --> utf-8
                            python �﷨������ַ���.decode("gbk").encode("utf-8")
		'''

		segmentResult = pynlpir.segment(textsegment,pos_tagging=True)
		newSegmentResult = removePunctuation(segmentResult)
		allSegmentResult.append(newSegmentResult)

	print len(allSegmentResult)
	file.close()
	pynlpir.close()	
	#print label
	return allSegmentResult

    
 
####ȥ���ִʹ��߷ִʺ����µĴ�����Ϣ####
#���룺�ִʽ�� ��list��
#�����ȥ�����Ժ�ķִʽ�� ��list��
def removePunctuation(segmentResult):
	NewSegmentResult = deepcopy(segmentResult)
	for everyone in NewSegmentResult:
		if (everyone[1]==u'punctuation mark' or everyone[1]== None):
			NewSegmentResult.remove(everyone)
	newSegmentResult = [everyeum[0] for everyeum in NewSegmentResult]
	return newSegmentResult
	
    
 
####�ִʽ��������ļ���utf8��ʽ��####
#���룺�ļ�����string�����ִʽ�� ��list��
#�������    
def output2File(FileName,wordList):	#������ļ������ִʽ�����
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
def output2File_label(FileName,labelList):	#������ļ������ִʽ�����
	f =  open(FileName,'w')
	WriteText = []
	for everynum in labelList:
		WriteText.append((str(everynum)))
		WriteText.append('\n')
	f.writelines(WriteText)
	f.close()
    
	
def output2File_highFre(FileName,labelList):	#������ļ������ִʽ�����
	f =  open(FileName,'w')
	WriteText = []
	for everynum in labelList:
		WriteText.append((str(everynum.encode('utf-8'))))
		WriteText.append('\n')
	f.writelines(WriteText)
	f.close()
	
####����ͣ�ô�####
#���룺�ļ�����string����δȥ��ͣ�ôʵķִʽ����list��
#�����ȥ��ͣ�ôʵķִʽ����list��
def cutStopWord(fileName,rawCorpus):	#����ͣ�ô�
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
	
	
####������Ƶ��####
#���룺��Ƶ���б�list����δȥ����Ƶ�ʵķִʽ����list��
#�����ȥ����Ƶ�ʵķִʽ����list��		
def cutHighFreWord(highFreWordList,rawCorpus):	#������Ƶ��
	TCorpus = deepcopy(rawCorpus)
	for row in TCorpus:
		for word in row:
			if word in highFreWordList:
				row.remove(word)
	return TCorpus
    
	
####ͳ�Ƹ�Ƶ�ʣ�Ϊ������Ƶ����׼��####
#���룺δȥ����Ƶ�ʵķִʽ����list����ͳ�����Ƶ�Ĵʵĸ�����int��
#�������Ƶ���б�list��		    
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
		highFreWord.append(wordSorted[i][0])	#ȡ����Ƶ��
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
		allSentence = cutStopWord(sourceFilePosition+'stopword1208.txt',allSentence) #����һ��Ϊ"stopword1208"
	if cutHighFreWord_or_not == 1:
		allSentence = cutHighFreWord(highFreStatistic(allSentence,cutHighFreWord_num),allSentence)		
	
	output2File(aimFilePostion+'Segment_result_hotel_neg.txt' ,allSentence)
		
	if highFreStatistic2File_or_not == 1:
		highFreFileName = 'highFreWord_neg.txt'
		highFreStatistic2File(allSubjectSentence,cutHighFreWord_num,sourceFilePosition + highFreFileName)
	
	allSegmentResult = separateWordFromFile(sourceFilePosition+"hotelPos2322.txt")
		
	allSentence = allSegmentResult
		
	if cutStopWord_or_not == 1:
		allSentence = cutStopWord(sourceFilePosition+'stopword1208.txt',allSentence) #����һ��Ϊ"stopword1208"
	if cutHighFreWord_or_not == 1:
		allSentence = cutHighFreWord(highFreStatistic(allSentence,cutHighFreWord_num),allSentence)		
	
	output2File(aimFilePostion+'Segment_result_hotel_pos.txt' ,allSentence)
		
	if highFreStatistic2File_or_not == 1:
		highFreFileName = 'highFreWord_pos.txt'
		highFreStatistic2File(allSubjectSentence,cutHighFreWord_num,sourceFilePosition + highFreFileName)
