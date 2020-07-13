#coding=utf-8
from toolkits.read_appkey_and_token import read_appkey, read_token
from toolkits.verify import show_appkey_and_token
from toolkits.text2speech_api_from_aliyun import text2speech
from toolkits.options import choose_voice
from toolkits.os_operations import create_folder_for_file
import os

def sentense_to_speech(text, audio_name, language='English'):
  create_folder_for_file(audio_name)
  chinese_optional_voices = ['Aiqi','Aicheng']
  english_optional_voices = ['Luca','Luna']
  if language == 'English':
    voice= 'Luca'
  elif language == 'Chinese':
    voice= 'Aiqi'
  text2speech(text, audio_name, voice=voice,  volumn=50, speech_rate=5,pitch_rate=0)


text = 'Ludwig Boltzmann, who spent much of his life studying statistical mechanics, died in 1906 by his own hand. Paul Ehrenfest, carrying on the work,died similarly in 1933. Now it is our turn to study statistical mechanics.'
audio_name = 'demo/destiny.wav'
language = 'English' # available options: /'Chinese' / 'English'
sentense_to_speech(text=text, audio_name=audio_name,language='English')
