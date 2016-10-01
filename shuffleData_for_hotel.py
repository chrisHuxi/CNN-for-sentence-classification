# -*- coding: utf-8 -*-
import random

####将数据随机打乱，存入一个统一的文件中####
#输入：需要整合的主题列表（list），需要shuffle的data所在文件夹名（s），需要shuffle的label所在文件夹名（s）
#输出：无（将shuffle好的文件存入shuffled_data文件夹中）
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
	
	
####将labelList输出到文件####
#输入：文件名（绝对路径），输出的list（list）
#输出：无
def output2File_label(fileName,labelList):	#输出到文件看看分词结果如何
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
	
	
