#coding=utf-8

from toolkits.read_appkey_and_token import read_appkey, read_token
from toolkits.verify import show_appkey_and_token
from toolkits.text2speech_api_from_aliyun import text2speech
from toolkits.options import choose_voice

language = 'English' # 'English'/ 'Chinese' / 
voice = choose_voice(language=language)  

def demo0():
  text = '北冥有鱼，其名为鲲,鲲之大，一锅炖不下'
  audio_name = '逍遥游.wav'
  chinese_optional_voices = ['Aiqi','Aicheng']
  english_optional_voices = ['Luca','Luna']
  text2speech(text, audio_name, voice='Aicheng',  volumn=50, speech_rate=5,pitch_rate=0)

demo0()

#def is_english_sentence(strs):
#  if strs.strip() == '':
#    return False
#  if strs[0] == '/':
#    return False
#  cn_count = 0
#  en_count = 0
#  for _char in strs:
#    if not '\u4e00' <= _char <= '\u9fa5':
#      en_count = en_count + 1
#    else:
#      cn_count = cn_count + 1
#  if cn_count == 0: 
#    return True
#  else:
#    return False
#
#def savecode(text,audioname):
#  import codecs
#  import ali_speech
#  from text2sppech_aliyun import text2speech
#
#  client = ali_speech.NlsClient()
#  # 设置输出日志信息的级别：DEBUG、INFO、WARNING、ERROR
#  client.set_log_level('INFO')
#  appkey = 'rDKx00GfgfmYCuJE'
#  token = 'f3390416c83848b8bd67e7391ffca80e'
#  voice = 'Luca'
#  audio_name = audioname
#  print(audioname)
#  print(text)
#  text2speech(client, appkey, token, 
#              text,
#              voice, 
#              audio_name)
#def readitem():
#  import codecs
#  filename = 'D:/A03 视频音频/文字转语音/Vocabulary.txt'
#  count = 0
#  with codecs.open(filename,'r','utf-8') as ff:
#    out = ff.read()
#    items = out.strip().split('\n')
#    for item in items:
#      item = item.replace('（','')
#      item = item.replace('）','')
#      item = item.replace('.','')
#      item = item.replace('(','')
#      item = item.replace(')','')
#      if is_english_sentence(item):
#        saveroutine = 'vocabulary{}.wav'.format(count)
#        count = count + 1
#        savecode(item,saveroutine)
