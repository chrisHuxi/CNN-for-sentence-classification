# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
import loadEmbedding_for_hotel

####��ȡ�ֺôʵ��ļ�####
#���룺�ֺôʵ��ļ����ļ���������·����
#������ִʽ����������ж��еĴʣ���άlist��
def readRawSepFile(RawSepFileName):
	file = open(RawSepFileName,'r')
	lines = file.readlines()
	resultList = []
	for line in lines:
		splitList = line.strip().split(' ')
		resultList.append(splitList)
	print "readRawSepFile"
	print "test_start:----------------------------"
	print resultList[0]
	print resultList[50]
	print resultList[0][0]
	print "test_end:----------------------------- \n\n"
	return resultList
	
####���ִʽ���б���������б��еĴ����Ƚ�####
#���룺�ִʽ���б�list����������ģ�ͣ�W2Vmodel��
#������ȽϺ����б�list��
def intersectSepResult_Embendding(sepResultList,model):
	intersectedResult = []
	for sentence in sepResultList:
		intersectedSentence = []
		for word in sentence:
			if word.decode('utf-8') in model.index2word:
				intersectedSentence.append(word.decode('utf-8'))
		intersectedResult.append(intersectedSentence)
	print "intersectSepResult_Embendding"
	print "test_start:----------------------------"
	print intersectedResult[0]
	print intersectedResult[50]
	print intersectedResult[0][1]
	print "test_end:----------------------------- \n\n"
	return intersectedResult

	
####����άlist������ļ�####
#���룺�ļ���������·����������Ķ�άlist��list��
#�������
def list2OutFile(fileName,list):
	f =  open(fileName,'w')
	WriteText = []
	for everyrow in list:
		for everycolumn in everyrow:
			WriteText.append((str(everycolumn.encode('utf-8'))+' '))
		WriteText.append('\n')
	f.writelines(WriteText)
	f.close()
	print "list output to "+fileName+"successfully!"

	
if __name__ == '__main__':
	sourceFilePosition = r"D:\NLP_exLab\pythonCode\CNN\data\hotel_annotatedData_utf8\sepWord_result\\"
	#RawSepFileName = "Segment_result_IphoneSE.txt"
	
	resultFilePosition = r"D:\NLP_exLab\pythonCode\CNN\data\hotel_annotatedData_utf8\inteSentence_result\\"
	#resultFileName = "Intersect_result_IphoneSE.txt"
	
	model = loadEmbedding_for_hotel.loadEmbedding()

	print "1"
	sepResultList = readRawSepFile(sourceFilePosition+'Segment_result_hotel_neg.txt')
	print "2"
	intersectedResult = intersectSepResult_Embendding(sepResultList,model)
	print "3"
	list2OutFile(resultFilePosition+'Intersect_result_hotel_neg.txt',intersectedResult)
	
	print "4"
	sepResultList = readRawSepFile(sourceFilePosition+'Segment_result_hotel_pos.txt')
	print "5"
	intersectedResult = intersectSepResult_Embendding(sepResultList,model)
	print "6"
	list2OutFile(resultFilePosition+'Intersect_result_hotel_pos.txt',intersectedResult)
	