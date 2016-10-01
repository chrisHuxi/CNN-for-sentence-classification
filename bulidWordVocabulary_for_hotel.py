# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
import loadEmbedding_for_hotel
import numpy as np
import chardet

####��ȡ��wordEmbedding�ཻ���ĵ��ļ�####    ע��Ҳ������shuffled�������ݼ�
#���룺��wordEmbedding�ཻ�����ļ����ļ���������·����
#������ִʽ����������ж��еĴʣ���άlist��
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
	
####��¼�������ļ��г��ֹ�����####
#���룺���ļ��ж����Ķ�άlist(list)
#��������������������ʵ��ֵ�(dict)�������ɴʶ����������ֵ�(dict)
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
	
####�����ӱ�ʾΪindex�ĸ�ʽ��д��txt�ļ�#### ����125 302 52 0 127 ����������
#���룺��Ҫд����ļ���������·����������ľ��ӣ���άlist����������ת��Ϊindex���ֵ䣨dict��
#���룺�ޣ������txt�ļ���
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
	
	
####���ʵ��еĴ��Դ������ķ�ʽ�洢####
#���룺��Ҫ������ļ����ļ���������·��������index���ɴʵĴʵ䣨dict����������ģ�ͣ�model��
#������ޣ����array���浽�ļ��У�
def saveEmbedding(fileName,id2WordDict,model):
	wordVocabularyEmbedding = []
	for i in range(0,len(id2WordDict)):
		wordVocabularyEmbedding.append(model[id2WordDict[i].decode('utf-8')])
		
	wordVocabularyEmbedding = np.array(wordVocabularyEmbedding)
	array2File(fileName,wordVocabularyEmbedding)
	

	
####���ʵ��еĴʱ���Ϊtxt�ļ�####
#���룺��Ҫд����ļ���������·��������id����word�Ĵʵ䣨dict��
#������ޣ��������ʵ��txt�ı���
def saveVocabulary(fileName,id2WordDict):
	wordList = []
	for i in range(0,len(id2WordDict)):
		wordList.append(id2WordDict[i])
	
	output2File(fileName,wordList)
	print "save vocabulary in"+fileName+"successfully!" 

####����άlist������ļ�####
#���룺�ļ���������·����������Ķ�άlist��list��
#�������
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

	
####��ndarray����Ϊ�ļ�####  
#���룺Ŀ���ļ����ļ���������·��������Ҫ�����array
#�������
def array2File(saveFileName,savedArray):
	np.save(saveFileName,savedArray)
	
	
	
####list���������ļ���utf8��ʽ��####
#���룺�ļ�����string�����ִʽ�� ��list��
#�������    
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
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	