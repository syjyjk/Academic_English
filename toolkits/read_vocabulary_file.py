# coding=utf-8
def is_english_sentence(strs):
  if strs.strip() == '':
    return False
  if strs[0] == '/':
    return False
  cn_count = 0
  en_count = 0
  for _char in strs:
    if not '\u4e00' <= _char <= '\u9fa5':
      en_count = en_count + 1
    else:
      cn_count = cn_count + 1
  if cn_count == 0: 
    return True
  else:
    return False


def english_vocabulary_file(filename,language='English'):
  import codecs
  filename = filename
  count = 0
  with codecs.open(filename,'r','utf-8') as ff:
    content = ff.readlines()
    content = [item.strip().strip('\n') for item in content]
    content = [item for item in content if is_english_sentence(item) and item != '']
    for item in content:
      print(item)

    #items = out.strip().split('\n')
    #for item in items:
    #  item = item.replace('（','')
    #  item = item.replace('）','')
    #  item = item.replace('.','')
    #  item = item.replace('(','')
    #  item = item.replace(')','')
    #  if is_english_sentence(item):
    #    saveroutine = 'vocabulary{}.wav'.format(count)
    #    count = count + 1
    #    savecode(item,saveroutine)

english_vocabulary_file('hello.txt')
