part 1: Convert a cinto speech using aliyun api
利用阿里云 语音合成 api 将例句转换为较为流畅的语音。

a. 开通阿里云语音合成服务
```
1. 登录 https://www.aliyun.com/， 实名注册。
2. 开通 智能语音交互产品中的语音合成服务（收费标准3.5元每千次调用）。
3. 复制并保存用户的  AccessToken信息。
4. 创建 “语音合成/语音识别” 项目，复制并保存项目的Appkey
```
b. 在本地安装 阿里云开发包 实现接口调用(需要 Python3 环境下执行下述命令)
```
1. 确认已经安装Python 包管理工具setuptools，如果没有安装，执行以下命令：
pip install setuptools
2. 下载开发包工具并将压缩包解压，进入文件夹目录：
http://download.taobaocdn.com/freedom/33762/compress/alibabacloud-nls-python-sdk.zip
3. 在开发包工具文件夹内执行以下命令：
python setup.py bdist_egg
python setup.py install
```

c.参照 [sentense_to_speech.py](./sentense_to_speech.py),以此为例将英文句子转写成wav格式的音频。转换效果可参见[demo/](demo).

由于语音合成服务要求每个句子不能超过300个英文字符，因此当输入文本总字符数超过300时，会将这句话按照文本中的分隔符进行分割。优先采用句号进行分割，若分割后仍然存在超过300字符的子句，则对此子句采用逗号分割，如果此时还存在超过300英文字符的子句，最终会利用该子句中which, what, that 等从句连接词进行分割 。
