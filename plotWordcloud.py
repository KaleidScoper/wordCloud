# coding:utf-8

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from collections import Counter

def generate_wordcloud(seg_text):
    '''
    输入文本生成词云。
    如果是中文文本，此处输入的是已经分好词、空格分隔的文本。
    现在做低频词过滤后生成词云
    '''
    # 设置显示方式
    d=path.dirname(__file__)
    input_mask = np.array(Image.open(path.join(d, "Images//input_mask.png")))
    font_path=path.join(d,"font//msyh.ttf")

    stopwords = set(STOPWORDS) # 设置默认停用词
    my_stopwords = set() # 添加自定义停用词
    with open(path.join(d, 'doc//stopwords.txt'), encoding='utf-8') as f:
        for line in f:
            my_stopwords.add(line.strip())
    stopwords.update(my_stopwords)

    words = seg_text.split(' ')
    words = [w.strip() for w in words if w.strip() and w not in stopwords]
    counter = Counter(words)
    min_freq = 2 # 设置词频阈值，低于此频率的词将被过滤
    filtered_words = {word: freq for word, freq in counter.items() if freq >= min_freq}

    wc = WordCloud(background_color="white",# 设置背景颜色
           max_words=2000, # 词云显示的最大词数  
           mask=input_mask,# 设置背景图片       
           stopwords=stopwords, # 设置停用词
           font_path=font_path, # 兼容中文字体，不然中文会显示乱码
                  )

    # 生成词云
    wc.generate_from_frequencies(filtered_words)
    # wc.generate(text)

    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, "Images//output.png"))

    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    plt.axis("off")# 关掉图像的坐标
    plt.show()

