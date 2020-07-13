#coding=utf-8
def create_folder_for_file(filename):
  import os
  path = os.path.dirname(filename)
  try:
    os.makedirs(path)
  except OSError:
    pass
