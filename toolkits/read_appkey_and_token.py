#coding=utf-8
import os
def read_appkey():
  filelist = os.listdir(os.getcwd()) 
  if 'appkey.txt' in filelist:
    print('appkey exist')
  else:
    with open('appkey.txt','w+') as ff:
      content = input('Enter Your Appkey:')
      ff.write(content)
      
  with open('appkey.txt') as ff:
    info = ff.readlines()
    for item in info:
      item_t = item.strip().strip('\n')
      if item_t != '':
        return item_t

def read_token():
  filelist = os.listdir(os.getcwd()) 
  if 'token.txt' in filelist:
    print('token exist')
  else:
    with open('token.txt','w+') as ff:
      content = input('Enter Your Token:')
      ff.write(content)
 
  with open('token.txt') as ff:
    info = ff.readlines()
    for item in info:
      item_t = item.strip().strip('\n')
      if item_t != '':
        return item_t
