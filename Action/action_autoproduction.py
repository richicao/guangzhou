#encoding=utf-8
from selenium import webdriver
import time
from selenium.common.exceptions import  NoAlertPresentException
from selenium.common.exceptions import  NoSuchElementException
from Action.action_login import *
from Action.test_data import *
driver=None
p = ParsePageObjectRepositoryConfig()
# 原油转输按钮
yyzs_pageType = p.getItemsFromSection('yyzs_page')['yyzs_page'].split('>')[0]
yyzs_pageExpression = p.getItemsFromSection('yyzs_page')['yyzs_page'].split('>')[1]
# 自动排产按钮
zdpc_pageType = p.getItemsFromSection('zdpc_page')['zdpc_page'].split('>')[0]
zdpc_pageExpression = p.getItemsFromSection('zdpc_page')['zdpc_page'].split('>')[1]
# 切到自动排产frame页
zdpc_pageframeType = p.getItemsFromSection('zdpc_page')['zdpc_page.frame'].split('>')[0]
zdpc_pageframeExpression = p.getItemsFromSection('zdpc_page')['zdpc_page.frame'].split('>')[1]
# 点击工艺约束按钮
zdpc_pagegyysType = p.getItemsFromSection('zdpc_page')['zdpc_page.gyys'].split('>')[0]
zdpc_pagegyysExpression = p.getItemsFromSection('zdpc_page')['zdpc_page.gyys'].split('>')[1]
#进入自动排产页面
def enter_autopro(driver):
    login(driver, login_info[0])
    click_button(driver, yyzs_pageType, yyzs_pageExpression)
    pause(0.5)
    click_button(driver, zdpc_pageType, zdpc_pageExpression)
    pause(0.5)
    enter_frame(driver, zdpc_pageframeType, zdpc_pageframeExpression)
    pause(0.5)
    click_button(driver, zdpc_pagegyysType, zdpc_pagegyysExpression)
#设置储罐期初
def set_cgqc(driver,cgname,cgyw,**kwargs):
    pause(0.5)
    #匹配储罐，按储罐名查找GH01储罐后，设置储罐的液位
    for j in range(3, 27):
         jg=str(j)
         if (driver.find_element_by_xpath('//*[@id="can_table"]/tbody/tr['+jg+']/td[2]').text == cgname):
            # 设置液位
            driver.find_element_by_xpath('//*[@id="can_table"]/tbody/tr[' + jg + ']/td[3]/input').clear()
            driver.find_element_by_xpath('//*[@id="can_table"]/tbody/tr['+jg+']/td[3]/input').send_keys(cgyw)
            # 单击油种弹出框
            driver.find_element_by_xpath(' //*[@id="can_table"]/tbody/tr['+jg+']/td[9]/div').click()
            pause(0.5)
          #筛选出被勾选的油种，去掉勾选框
            for i in range(1, 13):
                ji = "perRow_cb_" + str(i)
                if driver.find_element_by_id(ji).is_selected() == True:
                    driver.find_element_by_id(ji).click()
            else:
                pass
            #选择要设置的油种及比例，最后单击确定按钮
            for i in range(1, 13):
                oilselec = "perRow_cb_" + str(i)
                oilname = "//*[@id =" + "\"perRow_" + str(i) + "\"" + "]/td[2]/a"
                bl = "perRow_input_" + str(i)
                for key in kwargs:
                    if driver.find_element_by_xpath(oilname).text == key:
                        pause(0.5)
                        driver.find_element_by_id(oilselec).click()
                        driver.find_element_by_id(bl).clear()
                        driver.find_element_by_id(bl).send_keys(kwargs[key])
                        break
            driver.find_element_by_xpath('//*[@id="divOilList"]/div[1]/div/a[1]').click()
            break
#定义工艺约束数据初始化方法
def set_gyys(driver):
    # 对比页面中保温油种与预期保温bwyz列表中求集合对称差集
    pause(0.5)
    list1 = driver.find_element_by_xpath('//*[@id="section1"]/div[1]/div[1]/div/div/div/input').get_attribute(
        'value').split(',')
    bwyz = ['达混', '巴士拉', '杰诺']
    list = set(list1) ^ set(bwyz)

    #初始化保温油种,如果对比一样，不需要设置期初油种。否则设置期初油种
    if list == set():
         print("储罐不需要初始化")
    else:
         driver.find_element_by_xpath('//*[@id="section1"]/div[1]/div[1]/div/div/div/i').click()
         for temp in list:
             driver.find_element_by_xpath('//*[@id="section1"]/div[1]/div[1]/div/div/dl/dd[@lay-value="' + temp + '"]').click()
             pause(0.5)
         driver.find_element_by_xpath('//*[ @ id = "section1"]/div[1]/div[1]/label').click()
    list1 = driver.find_element_by_xpath('//*[@id="section1"]/div[1]/div[2]/div/div/div/input').get_attribute('value').split(',')


     #设置保温罐
    list1 = driver.find_element_by_xpath('//*[@id="section1"]/div[1]/div[2]/div/div/div/input').get_attribute('value').split( ',')
    bwg = ['GH01', 'GH02', 'GH03', 'GH04', 'GH05']
    list = set(list1) ^ set(bwg)
    if list == set():
         print("保温罐不需要初始化")
    else:
         driver.find_element_by_xpath('//*[@id="section1"]/div[1]/div[2]/div/div/div/i').click()
         for temp in list:
             driver.find_element_by_xpath('//*[@id="section1"]/div[1]/div[2]/div/div/dl/dd[@lay-value="' + temp + '"]').click()
             pause(0.5)
         driver.find_element_by_xpath('//*[ @ id = "section1"]/div[1]/div[1]/label').click()


     # 设置1#常加压的储罐
    n = 1
    list1sj = []
    list1yq=['1','2','3','4','5']
    for n in range(1, 10):
         temp = str(n)
         if driver.find_element_by_xpath('//*[@id="ownerColunm1"]/div[' + temp + ']').get_attribute('class') == 'layui-unselect layui-form-checkbox layui-form-checked':
                 list1sj.append(temp)
    list = set(list1sj) ^ set(list1yq)

    if list == set():
         print("1#常加工线不需要储罐配置")
    else:
         for temp in list:
             driver.find_element_by_xpath('//*[@id="ownerColunm1"]/div['+temp+']').click()
             pause(0.5)
    #报关
    input_string(driver, "xpath", "//*[@id='section1']/div[4]/div[1]/div/input", "12")

    #静置
    input_string(driver, "xpath", "//*[@id='section1']/div[4]/div[2]/div/input", "24")

    #流速1
    input_string(driver,"xpath", "//*[@id='section1']/div[5]/div[1]/div/input", "610")

    #流速3
    input_string(driver, "xpath", "//*[@id='section1']/div[5]/div[2]/div/input", "880")

    #马南线1档
    input_string(driver, "xpath", "//*[@id='section1']/div[6]/div/div[1]/input", "1400")

    #马南线2档
    input_string(driver, "xpath", "//*[@id='section1']/div[6]/div/div[2]/input", "1700")

    #马南线3档
    input_string(driver, "xpath", "//*[@id='section1']/div[6]/div/div[3]/input", "2000")

    #南厂线1档
    input_string(driver, "xpath", "//*[@id='section1']/div[7]/div/div[1]/input", "1700")

    #南厂线2档
    input_string(driver, "xpath", "//*[@id='section1']/div[7]/div/div[2]/input", "2300")

    #南厂线3档
    input_string(driver, "xpath", "//*[@id='section1']/div[7]/div/div[3]/input", "2800")
#定义来油计划数据初始化方法
def set_oil(driver):
     flag=1
     while flag==1:
         try:
             alert = driver.switch_to.alert
             alert.accept()
             flag=0
         except NoAlertPresentException as e:
             driver.find_element_by_xpath('// *[@id ="gridOilIn"]/div[1]/div[4]/a').click()

    #设置来油计划 巴士拉10.5
     select = Select(driver.find_element_by_xpath('//*[@id="gridOilIn"]/div[1]/div[2]/select'))
     select.select_by_value('巴士拉')
     pause(0.5)
     input_string(driver, "xpath", "//*[@id='gridOilIn']/div[1]/div[3]/input", "10.5")
     # 设置来油计划 巴士拉11.3
     click_button(driver, "id", "setOilIn")
     select = Select(driver.find_element_by_xpath('//*[@id="gridOilIn"]/div[2]/div[2]/select'))
     select.select_by_value('巴士拉')
     pause(0.5)
     input_string(driver, "xpath", "//*[@id='gridOilIn']/div[2]/div[3]/input", "11.3")
     # 设置来油计划 埃斯坡 10.75
     click_button(driver, "id", "setOilIn")
     select = Select(driver.find_element_by_xpath('//*[@id="gridOilIn"]/div[3]/div[2]/select'))
     select.select_by_value('埃斯坡')
     pause(0.5)
     input_string(driver, "xpath", "//*[@id='gridOilIn']/div[3]/div[3]/input", "10.75")
     # 设置来油计划 阿曼 13.07
     click_button(driver, "id", "setOilIn")
     select = Select(driver.find_element_by_xpath('//*[@id="gridOilIn"]/div[4]/div[2]/select'))
     select.select_by_value('阿曼')
     pause(0.5)
     input_string(driver, "xpath", "//*[@id='gridOilIn']/div[4]/div[3]/input", "13.07")
     # 设置来油计划 巴士拉 5.8
     click_button(driver, "id", "setOilIn")
     select = Select(driver.find_element_by_xpath('//*[@id="gridOilIn"]/div[5]/div[2]/select'))
     select.select_by_value('巴士拉')
     pause(0.5)
     input_string(driver, "xpath", "//*[@id='gridOilIn']/div[5]/div[3]/input", "5.8")
     # 设置来油计划 沙中 4.8
     click_button(driver, "id", "setOilIn")
     select = Select(driver.find_element_by_xpath('//*[@id="gridOilIn"]/div[6]/div[2]/select'))
     select.select_by_value('沙中')
     pause(0.5)
     input_string(driver, "xpath", "//*[@id='gridOilIn']/div[6]/div[3]/input", "4.8")
#油种加工方案1
def del_jgfa1(driver):
    flag = 1
    while flag == 1:
        try:
             driver.find_element_by_xpath('//*[@id="tbno1"]/tbody/tr[1]/td[4]/a/i').click()
        except  NoSuchElementException as e:
              flag = 0
def add_jgfa1(driver, **kwargs):
     driver.find_element_by_id("setno1").click()
     for i in range(0, 12):
        jg = "perRow_cb_" + str(i)
        jy = "perRow_" + str(i)
        ji = "perRow_input_" + str(i)
        for key in kwargs:
            if driver.find_element_by_xpath('//*[@id="' + jy + '"]/td[2]/a').get_attribute('text') == key:
               pause(0.5)
               driver.find_element_by_xpath('//*[@id="' + jg + '"]').click()
               pause(0.5)
               driver.find_element_by_xpath('//*[@id="' + ji + '"]').clear()
               pause(0.5)
               driver.find_element_by_xpath('//*[@id="' + ji + '"]').send_keys(kwargs[key])
               break
     driver.find_element_by_link_text('确认').click()
     time.sleep(1)
     try:
        alert = driver.switch_to.alert
        alert.accept()
        print('1常添加油种加工方案失败')
     except NoAlertPresentException as e:
         print('1常添加油种加工方案成功')
#油种加工方案3
def del_jgfa3(driver):
    flag = 1
    while flag == 1:
        try:
             driver.find_element_by_xpath('//*[@id="tbno3"]/tbody/tr[1]/td[4]/a/i').click()
        except  NoSuchElementException as e:
              flag = 0
def add_jgfa3(driver, **kwargs):
    driver.find_element_by_id("setno3").click()
    for i in range(0, 12):
        jg = "perRow_cb_" + str(i)
        jy = "perRow_" + str(i)
        ji = "perRow_input_" + str(i)
        for key in kwargs:
            if driver.find_element_by_xpath('//*[@id="' + jy + '"]/td[2]/a').get_attribute('text') == key:
                pause(0.5)
                driver.find_element_by_xpath('//*[@id="' + jg + '"]').click()
                pause(0.5)
                driver.find_element_by_xpath('//*[@id="' + ji + '"]').clear()
                pause(0.5)
                driver.find_element_by_xpath('//*[@id="' + ji + '"]').send_keys(kwargs[key])
                break
    driver.find_element_by_link_text('确认').click()
    time.sleep(1)
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print('3常添加油种加工方案失败')
    except NoAlertPresentException as e:
        print('3常添加油种加工方案成功')