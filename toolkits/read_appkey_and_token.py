def read_appkey():
  with open('appkey.txt') as ff:
    info = ff.readlines()
    for item in info:
      item_t = item.strip().strip('\n')
      if item_t != '':
        return item_t

def read_token():
  with open('token.txt') as ff:
    info = ff.readlines()
    for item in info:
      item_t = item.strip().strip('\n')
      if item_t != '':
        return item_t


