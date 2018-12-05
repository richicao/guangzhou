#encoding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

def getElement(driver,locateType,locateExpression):
    #获取页面单个元素
    try:
        wait=WebDriverWait(driver,10)
        return wait.until(lambda x:x.find_element(locateType,locateExpression))
    except Exception as e:
        raise e

def getElements(driver,locateType,locateExpression):
    #获取页面多个元素
    try:
        wait=WebDriverWait(driver,10)
        return wait.until(lambda x:x.find_elements(locateType,locateExpression))
    except Exception as e:
        raise e

def getSelectElementWithIndex(driver,index_num):
    #获取select下拉框元素---index
    select_element=Select(driver.find_element_by_xpath('//select'))
    #打印已选中的文本
    print (select_element.all_selected_options[0].text)
    return select_element.select_by_index(index_num)

def getSelectElementWithText(driver,text):
    #获取select下拉框元素----text
    select_element=Select(driver.find_element_by_xpath('//select'))
    #打印已选中的文本
    print (select_element.all_selected_options[0].text)
    return select_element.select_by_visible_text(text)

def getSelectElementWithValue(driver,value):
    #获取select下拉框元素---value
    select_element=Select(driver.find_element_by_xpath('select'))
    #打印已选中的文本
    print (select_element.all_selected_options[0].text)
    return select_element.select_by_value(value)