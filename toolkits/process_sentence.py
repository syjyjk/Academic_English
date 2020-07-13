def split_a(sentence, split_char):
  insert = '#&$&@#$%^&%#(*#'
  sentence = sentence.replace(split_char, split_char+insert)
  sentence_list = sentence.split(insert)
  return sentence_list

def split_b(sentence, split_char):
  insert = '#&$&@#$%^&%#(*#'
  sentence = sentence.replace(split_char, insert+split_char)
  sentence_list = sentence.split(insert)
  return sentence_list

def join(sentence_list):
  new_sentence_list = []
  collect = ''
  list_len = len(sentence_list)
  for count, sentence in enumerate(sentence_list[:-1]):    
    sentence = sentence.strip() + ' '
    if len(sentence) >=300:
      new_sentence_list.append(sentence.strip())
      #print('*****',len(sentence))
      collect = ''
    elif len(sentence)<300: 
      collect = collect + sentence
      if len(collect + sentence_list[count + 1]) >=300:
        new_sentence_list.append(collect)
        collect = ''
  new_sentence_list.append(collect+sentence_list[-1])
  return new_sentence_list
     
def process_sentence(sentence):
  sentence = sentence.replace('\n',' ')
  sentence = sentence.replace('  ',' ')
  if len(sentence)<300:
    sub_sentence_list = [sentence]
  if len(sentence)>=300:
    sentence_list = join(split_a(sentence.strip(),'.'))
    collect = []
    for item in sentence_list:
      if len(item.strip()) >= 300:
        commalist = join(split_a(item.strip(),',')) 
        collect = collect+commalist
      else:
        collect = collect+[item.strip()]
    sub_sentence_list = collect.copy()
    collect = []
    for item in sub_sentence_list:
      if len(item.strip()) >= 300:
        commalist = join(split_b(item.strip(),'which'))
        collect = collect+commalist
      else:
        collect = collect+[item.strip()]
    sub_sentence_list = collect.copy()
    collect = []
    for item in sub_sentence_list:
      if len(item.strip()) >= 300:
        commalist = join(split_b(item.strip(),'that'))
        collect = collect+commalist
      else:
        collect = collect+[item.strip()]
    collect = []
    for item in sub_sentence_list:
      if len(item.strip()) >= 300:
        commalist = join(split_b(item.strip(),'who'))
        collect = collect+commalist
      else:
        collect = collect+[item.strip()]
    sub_sentence_list = collect.copy()
    sub_sentence_list = [item for item in sub_sentence_list if item.strip() != '']
  return sub_sentence_list
