# wordCloud

用python进行文本分词并生成词云

## 依赖

* `sudo pip3 install jieba`
* `sudo pip3 install wordcloud`
* wordcloud包依赖于Pillow，numpy，matplotlib 

## 功能

* 分词采用结巴分词，并支持自定义字典（userdict.txt）、自定义停用词
* 分词结果进行词频统计分析，并导出
* 支持自定义过滤低频词
* 词云图可自己设定背景图（input_mask.png），默认输出为1920*1920
* 英文词云图不需先进行分词

## 使用方法

双击运行run.bat，会把doc路径下的纯文本“input.txt”生成images下的词云图“output.png”，和doc下的“词频统计.txt” 。
示例如下：（输入为测试文本与长恨歌）
![image](Images/output.png)


