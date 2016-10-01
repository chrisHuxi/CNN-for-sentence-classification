# -*- coding: utf-8 -*-
import random

####������������ң�����һ��ͳһ���ļ���####
#���룺��Ҫ���ϵ������б�list������Ҫshuffle��data�����ļ�������s������Ҫshuffle��label�����ļ�������s��
#������ޣ���shuffle�õ��ļ�����shuffled_data�ļ����У�
def shuffleAllData(sourceDataFilePosition):
	dataList = []
	labelList = []
	
	sourceDataFileName = sourceDataFilePosition + 'Intersect_result_hotel_neg.txt'
	fileData = open(sourceDataFileName,'r')
	linesData = fileData.readlines()
	for line in linesData:
		splitList = line.strip().split(' ')
		dataList .append(splitList)
		labelList.append(0)
	
	sourceDataFileName = sourceDataFilePosition + 'Intersect_result_hotel_pos.txt'
	fileData = open(sourceDataFileName,'r')
	linesData = fileData.readlines()
	for line in linesData:
		splitList = line.strip().split(' ')
		dataList .append(splitList)
		labelList.append(1)
		
	print len(dataList)
	print len(labelList)
		

	aimDataFile = r'D:\NLP_exLab\pythonCode\CNN\data\hotel_annotatedData_utf8\shuffData_result\shuffledData.txt'
	aimLabelFile = r'D:\NLP_exLab\pythonCode\CNN\data\hotel_annotatedData_utf8\shuffData_result\shuffledLabel.txt'
	outFileData = open(aimDataFile,'w')
	outFileLabel = open(aimLabelFile,'w')
	
	print len(dataList)
	print len(labelList)
	assert len(dataList) == len(labelList)
	
	indexList = range(0,len(dataList))
	random.shuffle(indexList)
	shuffledIndexList = indexList
	shuffledData = []
	shuffledLabel = []
	for i in range(0,len(dataList)):
		shuffledData.append(dataList[shuffledIndexList[i]])
		shuffledLabel.append(labelList[shuffledIndexList[i]])
		
	print len(shuffledData)
	print len(shuffledLabel)
	assert len(shuffledData) == len(shuffledLabel)
	
	list2OutFile(aimDataFile,shuffledData)
	output2File_label(aimLabelFile,shuffledLabel)
	
	
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
	
	
####��labelList������ļ�####
#���룺�ļ���������·�����������list��list��
#�������
def output2File_label(fileName,labelList):	#������ļ������ִʽ�����
	f =  open(fileName,'w')
	WriteText = []
	for everynum in labelList:
		WriteText.append((str(everynum)))
		WriteText.append('\n')
	f.writelines(WriteText)
	f.close()
	print "list output to "+fileName+"successfully!"
	
	
if __name__ == '__main__':

	sourceDataFilePosition = r'D:\NLP_exLab\pythonCode\CNN\data\hotel_annotatedData_utf8\inteSentence_result\\'

	shuffleAllData(sourceDataFilePosition)
	
	
