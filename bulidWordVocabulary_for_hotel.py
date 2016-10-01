# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
import loadEmbedding_for_hotel
import numpy as np
import chardet

####读取与wordEmbedding相交过的的文件####    注：也可以是shuffled过的数据集
#输入：与wordEmbedding相交过的文件的文件名（绝对路径）
#输出：分词结果与词向量中都有的词（二维list）
def readRawSepFile(intersectedFileName):
	file = open(intersectedFileName,'r')
	lines = file.readlines()
	resultList = []
	for line in lines:
		splitList = line.strip().split(' ')
		resultList.append(splitList)
	print "intersectedFile"
	print "test_start:----------------------------"
	print resultList[0]
	print resultList[50]
	print resultList[0][0]
	print "test_end:----------------------------- \n\n"
	return resultList
	
####记录在整个文件中出现过单词####
#输入：从文件中读出的二维list(list)
#输出：可以由索引读出词的字典(dict)，可以由词读出索引的字典(dict)
def bulidDictionary(resultList):
	wholeWord = []
	for sentence in resultList:
		wholeWord.extend(sentence)
	assert len(wholeWord) != 3000
	wordSet = set(wholeWord)
	print "wordSet"
	print "test_start:----------------------------"
	print len(wordSet)
	print "test_end:----------------------------- \n\n"
	word2IdDict = dict()
	id2WordDict = dict()
	i = 0
	for everyWord in wordSet:
		word2IdDict[everyWord] = i
		id2WordDict[i] = everyWord
		i = i + 1
	
	print "word2IdDict"
	print "test_start:----------------------------"
	print len(word2IdDict)
	print "test_end:----------------------------- \n\n"
	
	print "id2WordDict"
	print "test_start:----------------------------"
	print id2WordDict[0]
	print id2WordDict[50]
	
	print "test_end:----------------------------- \n\n"
	
	return id2WordDict,word2IdDict
	
####将句子表示为index的格式，写入txt文件#### 例：125 302 52 0 127 。。。。。
#输入：需要写入的文件名（绝对路径），读入的句子（二维list），将单词转化为index的字典（dict）
#输入：无（输出到txt文件）
def sentence2Index(fileName,resultList,word2IdDict):
	idList = []
	for sentence in resultList:
		sentenceList_T = []
		for word in sentence:
			sentenceList_T.append(word2IdDict[word])
		idList.append(sentenceList_T)
	print "idList"
	print "test_start:----------------------------"
	print idList[0]
	print idList[50]
	print "test_end:----------------------------- \n\n"
	list2OutFile(fileName,idList)
	
	
####将词典中的词以词向量的方式存储####
#输入：需要输入的文件的文件名（绝对路径），由index生成词的词典（dict），词向量模型（model）
#输出：无（输出array保存到文件中）
def saveEmbedding(fileName,id2WordDict,model):
	wordVocabularyEmbedding = []
	for i in range(0,len(id2WordDict)):
		wordVocabularyEmbedding.append(model[id2WordDict[i].decode('utf-8')])
		
	wordVocabularyEmbedding = np.array(wordVocabularyEmbedding)
	array2File(fileName,wordVocabularyEmbedding)
	

	
####将词典中的词保存为txt文件####
#输入：需要写入的文件名（绝对路径），从id读出word的词典（dict）
#输出：无（输出保存词典的txt文本）
def saveVocabulary(fileName,id2WordDict):
	wordList = []
	for i in range(0,len(id2WordDict)):
		wordList.append(id2WordDict[i])
	
	output2File(fileName,wordList)
	print "save vocabulary in"+fileName+"successfully!" 

####将二维list输出到文件####
#输入：文件名（绝对路径），输出的二维list（list）
#输出：无
def list2OutFile(fileName,list):
	f =  open(fileName,'w')
	WriteText = []
	for everyrow in list:
		for everycolumn in everyrow:
			WriteText.append((str(everycolumn)+' '))
		WriteText.append('\n')
	f.writelines(WriteText)
	f.close()
	print "list output to "+fileName+"successfully!"

	
####将ndarray保存为文件####  
#输入：目标文件的文件名（绝对路径），需要保存的array
#输出：无
def array2File(saveFileName,savedArray):
	np.save(saveFileName,savedArray)
	
	
	
####list结果输出到文件（utf8格式）####
#输入：文件名（string），分词结果 （list）
#输出：无    
def output2File(FileName,wordList):	
	f =  open(FileName,'w')
	WriteText = []
	for everyword in wordList:
		try:
			WriteText.append((str(everyword.decode('utf-8').encode('gbk'))))
		except UnicodeEncodeError:
			WriteText.append((str(everyword.decode('utf-8').encode('utf-8'))))
		WriteText.append('\n')
	f.writelines(WriteText)
	f.close()
	
	
		
if __name__ == '__main__':
	
	shuffledDataFileNme = r'D:\NLP_exLab\pythonCode\CNN\data\hotel_annotatedData_utf8\shuffData_result\shuffledData.txt'
	resultList = readRawSepFile(shuffledDataFileNme)
	id2WordDict,word2IdDict = bulidDictionary(resultList)
	
	sentenceFileName = r'D:\NLP_exLab\pythonCode\CNN\data\hotel_annotatedData_utf8\non-static\sentence_index.txt'
	sentence2Index(sentenceFileName,resultList,word2IdDict)
	
	vocabularyFileName = r'D:\NLP_exLab\pythonCode\CNN\data\hotel_annotatedData_utf8\non-static\vocabulary.txt'
	saveVocabulary(vocabularyFileName,id2WordDict)
	
	
	embeddingFileName = r'D:\NLP_exLab\pythonCode\CNN\data\hotel_annotatedData_utf8\non-static\embeddingVocabulary'
	model = loadEmbedding_for_hotel.loadEmbedding()
	saveEmbedding(embeddingFileName,id2WordDict,model)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	