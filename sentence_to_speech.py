#coding=utf-8
from toolkits.read_appkey_and_token import read_appkey, read_token
from toolkits.verify import show_appkey_and_token
from toolkits.text2speech_api_from_aliyun import text2speech
from toolkits.options import choose_voice
from toolkits.os_operations import create_folder_for_file
from toolkits.process_sentence import process_sentence
import os

def sentence_to_speech(text, audio_name, language='English'):
  sub_sentence_list = process_sentence(text)
  chinese_optional_voices = ['Aiqi','Aicheng']
  english_optional_voices = ['Luca','Luna']

  if language == 'English':
    voice= 'Luca'
  elif language == 'Chinese':
    voice= 'Aiqi'

  if len(sub_sentence_list)>1:
    for count,sub_sentence in enumerate(sub_sentence_list):
      print(len(sub_sentence),sub_sentence)
      save_name = os.path.splitext(audio_name)[0] + str(count + 1)+ os.path.splitext(audio_name)[1]
      create_folder_for_file(save_name)
      text2speech(sub_sentence, save_name, voice=voice,  volumn=50, speech_rate=-120,pitch_rate=0)
  elif len(sub_sentence_list)==1:
    save_name = audio_name 
    create_folder_for_file(save_name)
    text2speech(sub_sentence_list[0], save_name, voice=voice,  volumn=50, speech_rate=-120,pitch_rate=0)
  else:
    pass

text = '''“Ludwig Boltzmann, who spent much of his life studying statistical mechanics, died in 1906 by his own hand. Paul Ehrenfest, carrying on the work,
died similarly in 1933. Now it is our turn to study statistical mechanics.”'''
audio_name = 'demo/destiny.wav'
language = 'English' # available options: /'Chinese' / 'English'
sentence_to_speech(text=text, audio_name=audio_name,language='English')


text = '''The Ising model, named after the physicist Ernst Ising, is a mathematical model of ferromagnetism in statistical mechanics. The model consists of discrete variables that represent magnetic dipole moments of atomic spins that can be in one of two states (1 or minus 1). The spins are arranged in a graph, usually a lattice, allowing each spin to interact with its neighbors. The model allows the identification of phase transitions, as a simplified model of reality. The two-dimensional square-lattice Ising model is one of the simplest statistical models to show a phase transition.
The Ising model was invented by the physicist Wilhelm Lenz (1920), who gave it as a problem to his student Ernst Ising. The one-dimensional Ising model has no phase transition and was solved by Ising (1925) himself in his 1924 thesis. The two-dimensional square lattice Ising model is much harder, and was given an analytic description much later, by Lars Onsager (1944). It is usually solved by a transfer-matrix method, although there exist different approaches, more related to quantum field theory.
In dimensions greater than four, the phase transition of the Ising model is described by mean field theory.'''
audio_name = 'demo/long_sentence.wav'
language = 'English' # available options: /'Chinese' / 'English'
sentence_to_speech(text=text, audio_name=audio_name,language='English')
