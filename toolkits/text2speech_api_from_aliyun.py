# -*- coding: utf-8 -*-
"""
 * Copyright 2015 Alibaba Group Holding Limited
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

import threading
import ali_speech
from ali_speech.callbacks import SpeechSynthesizerCallback
from ali_speech.constant import TTSFormat
from ali_speech.constant import TTSSampleRate


class MyCallback(SpeechSynthesizerCallback):
    # 参数name用于指定保存音频的文件
    def __init__(self, name):
        self._name = name
        self._fout = open(name, 'wb')

    def on_binary_data_received(self, raw):
        #print('MyCallback.on_binary_data_received: %s' % len(raw))
        self._fout.write(raw)

    def on_completed(self, message):
        #print('MyCallback.OnRecognitionCompleted: %s' % message)
        self._fout.close()

    def on_task_failed(self, message):
        #print('MyCallback.OnRecognitionTaskFailed-task_id:%s, status_text:%s' % (
        #message['header']['task_id'], message['header']['status_text']))
        self._fout.close()

    def on_channel_closed(self):
        #print('MyCallback.OnRecognitionChannelClosed')
        pass



def text2speech(text, audio_name, voice='Aicheng',  volumn=50, speech_rate=0,pitch_rate=0):
  from toolkits.read_appkey_and_token import read_appkey, read_token
  appkey = read_appkey()
  token  = read_token()
  client = ali_speech.NlsClient()
  client.set_log_level('INFO')
  callback = MyCallback(audio_name)
  synthesizer = client.create_synthesizer(callback)
  synthesizer.set_appkey(appkey)
  synthesizer.set_token(token)
  synthesizer.set_voice(voice)
  synthesizer.set_text(text)
  synthesizer.set_format(TTSFormat.WAV)
  synthesizer.set_sample_rate(TTSSampleRate.SAMPLE_RATE_16K)
  synthesizer.set_volume(volumn)
  synthesizer.set_speech_rate(speech_rate)
  synthesizer.set_pitch_rate(pitch_rate)
  try:
      ret = synthesizer.start()
      if ret < 0:
          return ret
      synthesizer.wait_completed()
  except Exception as e:
      print(e)
  finally:
      synthesizer.close()



#def savecode(text,audioname):
#  import codecs
#  from text2sppech_aliyun import text2speech
#
#  client = ali_speech.nlsclient()
#  # 设置输出日志信息的级别：DEBUG、INFO、WARNING、ERROR
#  client.set_log_level('inFO')
#  appkey = 'rdkx00gfgfmycuJE'
#  token = 'f3390416c83848b8bd67e7391ffca80e'
#  voice = 'luca'
#  audio_name = audioname
#  print(audioname)
#  print(text)
#  text2speech(client, appkey, token, 
#              text,
#              voice, 
#              audio_name)

#def process_multithread(client, appkey, token, number):
#    thread_list = []
#    for i in range(0, number):
#        text = "这是线程" + str(i) + "的合成。"
#        audio_name = "sy_audio_" + str(i) + ".wav"
#        thread = threading.Thread(target=process, args=(client, appkey, token, text, audio_name))
#        thread_list.append(thread)
#        thread.start()
#
#    for thread in thread_list:
#       thread.join()
