#encoding=utf-8
from Action.basic_function import *
from Util.GetConf import *

#登录页面包括用户名输入框、密码输入框、登录按钮
p=ParsePageObjectRepositoryConfig()
#用户名输入框定位方式及表达式
usernameType = p.getItemsFromSection('ypth_login')['loginpage.username'].split('>')[0]
usernameExpression=p.getItemsFromSection('ypth_login')['loginpage.username'].split('>')[1]
#密码输入框定位方式及表达式
passwordType=p.getItemsFromSection('ypth_login')['loginpage.password'].split('>')[0]
passwordExpression=p.getItemsFromSection('ypth_login')['loginpage.password'].split('>')[1]
#登录控件定位方式及表达式
bloginType=p.getItemsFromSection('ypth_login')['loginpage.loginbutton'].split('>')[0]
bloginExpression=p.getItemsFromSection('ypth_login')['loginpage.loginbutton'].split('>')[1]


def login(driver,usernameAndpassword,*arg):
    username,password=usernameAndpassword.split('||')
    visit_url(driver,url)
    driver.maximize_window()
    pause(0.5)
    input_string(driver,usernameType, usernameExpression, username)
    pause(0.5)
    input_string(driver,passwordType, passwordExpression, password)
    pause(0.5)
    click_button(driver,bloginType, bloginExpression)


