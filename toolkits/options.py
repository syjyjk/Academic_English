def choose_voice(language='English'):
  if language == 'English' or language == 'english':
    voice = 'Luna'
  elif language == 'Chinese' or language == 'chinese':
    voice = 'Aicheng'
  elif language == 'Chinese_and_English' or language == 'chinese_and_english':
    voice = 'Aicheng'
  else:
    voice = 'Aicheng'
  return voice


