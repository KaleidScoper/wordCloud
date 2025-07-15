# coding:utf-8

from os import path
import chnSegment
import plotWordcloud


if __name__=='__main__':

    # 读取文件
    d = path.dirname(__file__)
    text = open(path.join(d,'doc//input.txt'), encoding='utf-8').read()

    # 若是中文文本，则先进行分词操作
    seg_text = chnSegment.word_segment(text)
    
    # 生成词云
    plotWordcloud.generate_wordcloud(seg_text)
