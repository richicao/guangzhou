#encoding=utf-8
import configparser
from ProjectVar.Var import *

class ParsePageObjectRepositoryConfig(object):
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read(page_object_repository_path)

    def getItemsFromSection(self,sectionName):
        items=self.cf.items(sectionName)
        return dict(items)

if __name__ == '__main__':
        # 调试代码
    p=ParsePageObjectRepositoryConfig()
    #print( p.getItemsFromSection('126mail_login'))
    #print(p.getItemsFromSection('126mail_login')['loginpage.username'].split('//')[1])
    #print(type(p.getItemsFromSection('126mail_login')['loginpage.frame'].split('//')[1]))
    print(p.getItemsFromSection('zdpc_page')['zdpc_page.bg'].split('>')[0])
    print(p.getItemsFromSection('zdpc_page')['zdpc_page.bg'].split('//')[1])
    str = 'G20-放假安排'
    result = str.split('-')
    print(result)



