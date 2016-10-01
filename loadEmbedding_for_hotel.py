# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
'''
#文本文件必须是utf-8无bom格式
mod = Word2Vec.load(r'D:\NLP_exLab\pythonCode\CNN\Word60.model')	#3个文件放在一起：Word60.model   Word60.model.syn0.npy   Word60.model.syn1neg.npy

fout = open(r"D:\NLP_exLab\pythonCode\CNN\similarity.txt", 'w') 

showWord = []
fout_testWord = open(r"D:\NLP_exLab\pythonCode\CNN\testWord.txt",'r')
lines = fout_testWord.readlines()#读取全部内容 
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

####加载word embedding函数####
#输入：无
#输出：加载好的模型，可通过model['s']来访问词向量，每一个词向量为60维的ndarray
def loadEmbedding():
	
    model = Word2Vec.load(r'D:\NLP_exLab\pythonCode\CNN\wordEmbedding\Word60.model')	#3个文件放在一起：Word60.model   Word60.model.syn0.npy   Word60.model.syn1neg.npy
    return model
    
