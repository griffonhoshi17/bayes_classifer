# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xlrd
import random
import numpy as np
import re

def extractBigStringFromFile(filename):
    spamlist = []
    hamlist = []
    workbook = xlrd.open_workbook(filename)
    #sheet_names= workbook.sheet_names()
    booksheet = workbook.sheet_by_index(0) # 用索引取第一个sheet
    rows = booksheet.nrows # 获取行数
    #clos = booksheet.ncols # 获取列数
    for i in range(rows): # 遍历每一行
        cell_class = booksheet.cell_value(i, 0) # 取第一列数据
        cell_content = booksheet.cell_value(i, 1) # 取第二列数据
        if cell_class == 'spam':
            spamlist.append(cell_content)
        elif cell_class == 'ham':
            hamlist.append(cell_content)
        else:
            pass
    return spamlist, hamlist

"""
函数说明：接受一个大字符串并将其解析为字符串列表
"""
def textParse(bigString):
    listOfTokens = re.split(r'[^a-zA-Z0-9\']+', bigString) # 将特殊符号作为切分标志进行字符串切分， 即非字母非数字
    print(listOfTokens)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

"""
函数说明：将切分的实验样本词条整理成不重复的词条列表，即词汇表
Parameters:
    dataSet 整理的样本数据集
Returns:
    vocabSet 返回不重复的词条列表
"""
def createVocabList(dataSet):
    vocabSet = set([]) # 创建一个空集
    for document in dataSet:
        vocabSet = vocabSet | set(document) # 取并集
    return list(vocabSet)


"""
函数说明:根据vocabList词汇表，将inputSet向量化，向量的每个元素为1或0
Parameters:
    vocabList - createVocabList返回的列表
    inputSet - 切分的词条列表
Returns:
    returnVec - 文档向量,词集模型
"""
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec


"""
函数说明:根据vocabList词汇表，构建词袋模型
Parameters:
    vocabList - createVocabList返回的列表
    inputSet - 切分的词条列表
Returns:
    returnVec - 文档向量,词袋模型
"""
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)  # 创建一个其中所含元素都为0的向量
    for word in inputSet:             # 遍历每个词条
        if word in vocabList:         # 如果词条存在于词汇表中，则计数加一
            returnVec[vocabList.index(word)] += 1
    return returnVec  # 返回词袋模型


"""
函数说明:朴素贝叶斯分类器训练函数
Parameters:
    trainMatrix - 训练文档矩阵，即setOfWords2Vec返回的returnVec构成的矩阵
    trainCategory - 训练类别标签向量，即loadDataSet返回的classVec
Returns:
    p0Vect - 正常邮件类的条件概率数组
    p1Vect - 垃圾邮件类的条件概率数组
    pAbusive - 文档属于垃圾邮件类的概率
"""
# TODO ...



if __name__ == '__main__':
    print([0]*10)
    pass