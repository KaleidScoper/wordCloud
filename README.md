# wordCloud

用python进行文本分词并生成词云

## 需要安装的包

* `sudo pip3 install jieba`
* `sudo pip3 install wordcloud`
* wordcloud包依赖于Pillow，numpy，matplotlib 

## 其他

* 分词采用结巴分词，并支持自定义字典（userdict.txt）
* 分词结果进行词频统计分析，并导出
* 词云图可自己设定背景图（英文词云图不需先进行分词）
* 词云图可自定义形状（input_mask.png）

## 运行结果

运行demo.py，会把“input.txt”生成为相应的的词云图，和“doc/词频统计.txt”  
eg:输入十九大报告全文的词云图如下：  
![image](Images/十九大.png)


