# 3  给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/；  请大家写一个爬虫，将里面的英语节目MP3，都下载下来；
#    这些音频文件 在网页的html文件内容都是以mp3结尾的，如下图所示：
#  要求大家使用Requests库获取这个网页html文本内容，并且使用正则表达式获取里面所有的mp3文件的网址；并进行下载；
#   Windows上的wget可以点击这里 下载。 这个程序不用安装，直接在命令行里使用即可；
# 注意：
# 获取的音频网址前面需要加上 前缀 http://www.listeningexpress.com/studioclassroom/ad/ 才是完整的下载地址
# MP3文件中有空格字符，组成下载网址时，需要进行url编码，否则空格会被当成命令行分隔符。参考代码如下所示
# >>> from urllib.parse import quote
# >>> quote('2019-04-13 NEWSworthy Clips.mp3')
# '2019-04-13%20NEWSworthy%20Clips.mp3'