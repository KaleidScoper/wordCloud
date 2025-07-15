# wordCloud

用python进行文本分词并生成词云

## 需要安装的包

* `sudo pip3 install jieba`
* `sudo pip3 install wordcloud`
* wordcloud包依赖于Pillow，numpy，matplotlib 

## 其他

* 分词采用结巴分词，并支持自定义字典（userdict.txt）、自定义停用词
* 分词结果进行词频统计分析，并导出
* 支持自定义过滤低频词
* 词云图可自己设定背景图（input_mask.png）
* 英文词云图不需先进行分词

## 运行结果

运行demo.py，会把“input.txt”生成为相应的的词云图，和“doc/词频统计.txt”  
eg:
![image](Images/output.png)


