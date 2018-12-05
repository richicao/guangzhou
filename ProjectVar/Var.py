#encoding=utf-8
import os
import time

#当前文件路径
file_path=__file__
#工程路径
#os.path.dirname(__file__)当前文件所在路径
project_path=os.path.dirname(os.path.dirname(__file__))

page_object_repository_path=project_path+'\\Conf\\PageObjectRepository.ini'

url='http://192.168.30.111/gsdd'

chrome='C:\\Program Files (x86)\\Google\Chrome\\Application\\chromedriver'
ie='c:\\Python27\\IEDriverServer'
firefox='c:\\Python27\\geckodriver'