import os
import wave
import struct
import numpy as np
import matplotlib.pyplot as plt

def concatenate_sentences(slist,radio_name ,length=40000,length0=5000):
  #Reference:https://www.cnblogs.com/xingshansi/p/6799994.html
  mp3_list = []
  space0 = np.zeros(length0,dtype=np.int16)
  mp3_list.append(space0.copy())
  for filepath in slist:
    with wave.open(filepath,'rb') as ff:
      info = ff.getparams()
      wformat = info[3]
      framerate = info[2]
      mp3   = ff.readframes(wformat)
      mp3  = np.frombuffer(mp3,dtype=np.int16)
      mp3 = mp3*1./max( abs(mp3) )
      mp3_list.append(mp3.copy())
      space = np.zeros(length,dtype=np.int16)
    mp3_list.append(space)
  radio = np.concatenate( mp3_list ,axis=0)
    
  with wave.open(radio_name,'wb') as ff:
    ff.setparams((1,2,int(framerate),len(radio),'NONE','not compressed'))
    for v in radio:
      ff.writeframes(struct.pack('h', int(v * 64000 / 2)))

pos = 'verb'
path0 = 'academic_vocabulary_mp3/{}'.format(pos)
vocabularys = os.listdir(path0)
for vocabulary in vocabularys:
  path1 = os.path.join(path0, vocabulary)
  item_list = os.listdir(path1)
  path2 = [os.path.join(path1,item) for item in item_list]
  radio_name = '{}.mp3'.format(vocabulary)
  concatenate_sentences(path2, radio_name)

