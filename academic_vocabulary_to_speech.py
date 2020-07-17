import os
from sentence_to_speech import sentence_to_speech

def vocabulary_to_sentences():
  with open('Academic_Vocabulary.txt','r') as text: 
    collect = {}
    lines = text.readlines()
    for item in lines:
      if item.strip() != '':
        item = item.strip()
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
          example_count = 0
        if item[0] == '[':
          zh_meaning = item.strip('[').strip().strip(']').strip()
          collect[pos][word]['zhmeaning'+str(meaning_count)] = zh_meaning 
        if item[0] == '>':
          example_count = example_count + 1
          example = item.strip('>').strip()
          collect[pos][word]['exmaple'+str(meaning_count)+'_'+str(example_count)] = example

    for pos in collect.keys():
      pos_dict = collect[pos]
      for word in pos_dict.keys():
        word_dict = pos_dict[word]
        sen_count = 0
        sens = word+', '+ pos + '. '  
        audio_name = os.path.join('academic_vocabulary_mp3_sub_sentences',pos,word, word+ '_'+pos +'_'+ str(sen_count) + '_'+ 'word_and_pos' +'.mp3')
        sentence_to_speech(sens, audio_name, language='English')
  
        for label in word_dict.keys():
          sens = word_dict[label]
          sen_count = sen_count + 1
          audio_name = os.path.join('academic_vocabulary_mp3_sub_sentences',pos,word, word+ '_'+pos +'_'+ str(sen_count) + '_'+ label +'.mp3')
          if label[:2] == 'zh':
            language = 'Chinese'
          else:
            language = 'English'
          sentence_to_speech(sens, audio_name, language=language)

vocabulary_to_sentences()
