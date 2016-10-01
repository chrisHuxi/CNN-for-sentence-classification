# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
'''
#�ı��ļ�������utf-8��bom��ʽ
mod = Word2Vec.load(r'D:\NLP_exLab\pythonCode\CNN\Word60.model')	#3���ļ�����һ��Word60.model   Word60.model.syn0.npy   Word60.model.syn1neg.npy

fout = open(r"D:\NLP_exLab\pythonCode\CNN\similarity.txt", 'w') 

showWord = []
fout_testWord = open(r"D:\NLP_exLab\pythonCode\CNN\testWord.txt",'r')
lines = fout_testWord.readlines()#��ȡȫ������ 
for line in lines:
    showWord.append((line.strip().decode('utf-8')))
print showWord

for word in showWord:
    if word in mod.index2word:
        sim = mod.most_similar(word)
        fout.write(word.encode('utf-8') +'\n')
        for ww in sim:
            fout.write('\t\t\t' + ww[0].encode('utf-8') + '\t\t'  + str(ww[1])+'\n')
        fout.write('\n')
    else:
        fout.write(word.encode('utf-8') + '\t\t\t ???   '+'\n\n')

fout.close()  
'''

####����word embedding����####
#���룺��
#��������غõ�ģ�ͣ���ͨ��model['s']�����ʴ�������ÿһ��������Ϊ60ά��ndarray
def loadEmbedding():
	
    model = Word2Vec.load(r'D:\NLP_exLab\pythonCode\CNN\wordEmbedding\Word60.model')	#3���ļ�����һ��Word60.model   Word60.model.syn0.npy   Word60.model.syn1neg.npy
    return model
    
