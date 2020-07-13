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

