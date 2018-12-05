#encoding=utf-8
from selenium import webdriver
from Util.ObjectMap import *
from ProjectVar.Var import *
from Util.DirAndFile import *
import traceback
import os

def open_browser(browserName,*arg):
    # 打开浏览器
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path=ie)
            return driver
        elif browserName.lower() == 'chrome':
            #driver = webdriver.Chrome(executable_path=chrome)
            desired_caps = {}
            desired_caps['platform'] = 'WINDOWS'
            desired_caps['browserName'] = 'chrome'
            driver = webdriver.Remote('http://192.168.20.150:4444/wd/hub', desired_caps)
            driver = webdriver.Chrome(executable_path=chrome)
            return driver
        elif browserName.lower() == 'firefox':
            driver = webdriver.Firefox(executable_path=firefox)
            return driver
        else:
            print('has no such browser')
        pass
    except Exception as e:
        raise e


def visit_url(driver,url,*arg):
    #访问网页
    try:
        driver.get(url)
    except Exception as e:
        raise e

def close_browser(driver):
    #退出浏览器
    try:
        driver.quit()
    except Exception as e:
        raise e

def enter_frame(driver,locatorType,locatorExpression,*arg):
    #切换frame
    try:
        driver.switch_to.frame(getElement(driver,locatorType,locatorExpression))
    except Exception as e:
        raise e

def get_out_frame(driver):
    #切出来 frame
    try:
        driver.switch_to_default_content()
    except Exception as e:
        raise e

def input_string(driver,locatorType,locatorExpression,content,*arg):
    #send_keys and clear
    try:
        getElement(driver, locatorType, locatorExpression).clear()
        pause(0.5)
        getElement(driver,locatorType,locatorExpression).send_keys(content)
        pause(0.5)
    except Exception as e:
        raise e

def get_value(driver,locatorType,locatorExpression,content,*arg):
    try:
        getElement(driver, locatorType, locatorExpression).get_attribute('value')
        pause(0.5)
    except Exception as e:
        raise e

def click_button(driver,locatorType,locatorExpression):
    #点击操作
    try:
        getElement(driver, locatorType, locatorExpression).click()
    except Exception as e:
        raise e

def assert_keyword(driver,excepted_word,*arg):
    #断言
    try:
        assert True==(excepted_word in driver.page_source)
    except AssertionError as e:
        raise e
    except Exception as e:
        raise e
    else:
        print ('keyword : %s in page_source'%excepted_word)


def pause(seconds,*arg):
    time.sleep(float(seconds))


def max_window(driver):
    #最大化窗口
    try:
        driver.maximize_window()
    except Exception as e:
        raise e


def get_element_out_to_can_see(driver,locatorType, locatorExpression,*arg):
    #把元素拉倒可见的位置
    try:
        target = getElement(driver,locatorType, locatorExpression)
        driver.execute_script("arguments[0].scrollIntoView();", target)
    except Exception as e:
        raise e


def scroll_page_to_buttom(driver):
    #滚动条到最下方
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except Exception as e:
        raise e


def scroll_page_to_top(driver):
    #滚动条到最上方
    try:
        driver.execute_script("window.scrollTo(0, 0);")
    except Exception as e:
        raise e


def capture_screen(driver,pictureName):
    # 获取正常截图
    dirPath=createDir(project_path+"\ScreenPictures\CapturePicture",time.strftime("%Y-%m-%d"))
    os.chdir(dirPath)
    try:
        driver.get_screenshot_as_file(pictureName)
    except Exception as e:
        raise e

def error_screen(driver,pictureName):
    # 获取异常截图
    dirPath=createDir(project_path + "//ScreenPictures//ErrorPicture", time.strftime("%Y-%m-%d"))
    os.chdir(dirPath)
    try:
        driver.get_screenshot_as_file(pictureName)
    except Exception as e:
        raise e