import os
from sentence_to_speech import sentence_to_speech
with open('Academic_Vocabulary.txt','r') as text: 
  
  collect = {}
  lines = text.readlines()
  for item in lines:
    if item.strip() != '':
      item = item.strip()
      #print(item)
      if item[-3:] == ':::':
        pos = item.strip(':::').strip()
        collect[pos] = {}
      if item[0] == '?' or item[0]=='？':
        meaning_count = 0
        word = item.strip('?').strip('？').strip().strip(':')
        collect[pos][word] = {}
      if item[0] == '*' or item[0]=='*':
        meaning_count = meaning_count + 1
        meaning = item.strip('*').strip()
        collect[pos][word]['meaning'+str(meaning_count)] = meaning 
      if item[0] == '[':
        zh_meaning = item.strip('[').strip().strip(']').strip()
        collect[pos][word]['zhmeaning'+str(meaning_count)] = zh_meaning 
      if item[0] == '>':
        example = item.strip('>').strip()
        collect[pos][word]['exmaple'+str(meaning_count)] = example

  for i0 in collect.keys():
    poss = collect[i0]
    for i1 in poss.keys():
      words = poss[i1]
      sen_count = 0
      for i2 in words.keys():
        sens = words[i2]
        sen_count = sen_count + 1
        audio_name = os.path.join('academic_vocabulary_mp3',i0, i1 , i1+ '_' + str(sen_count) + '_'+ i2 +'.mp3')
        if i2[:2] == 'zh':
          language = 'Chinese'
        else:
          language = 'English'
        sentence_to_speech(sens, audio_name, language=language)
