#encoding=utf-8
from HTMLTestRunner import HTMLTestRunner
import unittest
from Action.action_autoproduction import *
from Action.test_data import *
from Action.basic_function import *

class TestAutoProduction(unittest.TestCase):
    def setUp(self):
        self.driver=open_browser(browser_name)

    # 初始化各个储罐的期初
    # def test_settank(self):
    #     # 进入自动排产页面
    #     enter_autopro(self.driver)
    #     #点击储罐期初设置按钮，设置各个储罐的期初
    #     click_button(self.driver, "id", "btnSetAllCanStart")
    #     self.driver.switch_to.frame(0)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GH01', '16.4', 达混='55.5', 卡斯蒂利亚='44.5')
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GH02', '16.4', 达混=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GH03', '16.6', 凯撒杰=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GH04', '3.3', 凯撒杰=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GH05', '17', 凯撒杰=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GH06', '2.5', 卡斯蒂利亚=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GH07', '2.5', 沙中=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GH08', '17', 阿曼=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GH09', '5', 萨杜恩=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GH010', '17', 萨杜恩=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GH011','5' , 萨杜恩=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GH012', '17',阿曼=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GL01', '16.5', 卡斯蒂利亚=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GL02', '19.5', 沙中=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GL03', '2.5', 沙轻=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GL04', '15.6', 沙轻=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GL05', '3.8', 沙中=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'GL06', '20', 卡斯蒂利亚=100)
    #     pause(0.5)
    #     # set_cgqc(self.driver, 'G107', '20',  萨杜恩=100)
    #     # pause(0.5)
    #     set_cgqc(self.driver, 'G111', '14', 萨杜恩=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'G112', '2.5', 阿曼=80,达混=20)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'G113', '9.5',  阿曼=80,达混=20)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'G114', '3.5',  阿曼=80,达混=20)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'G101', '17', 沙轻=80,卡斯蒂利亚=20)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'G103', '9.5', 沙轻=80,卡斯蒂利亚=20)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'G109', '8.9', 沙轻=80,卡斯蒂利亚=20)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'G110', '3', 沙中=100)
    #     pause(0.5)
    #     set_cgqc(self.driver, 'G102', '11.5', 沙轻=80,卡斯蒂利亚=20)
    #     pause(1)
    #     self.driver.find_element_by_link_text('确定').click()
    #     print('期初储罐数据设置成功')
    #设置正确数据，自动排产成功
    def test_autoprosuc(self):
        try:
            enter_autopro(self.driver)
        except Exception as e:
            raise e
        else:
            print ('原油转输调度系统登录成功')
        finally:

            # 工艺约束数据初始化
            set_gyys(self.driver)
            # 来油计划数据初始化
            set_oil(self.driver)
            # 初始化1#加工方案，先删除全部，再添加需要的加工方案
            del_jgfa1(self.driver)
            pause(0.5)
            add_jgfa1(self.driver, 阿曼=80, 达混=20)
            add_jgfa1(self.driver, 萨杜恩=100)
            add_jgfa1(self.driver, 凯撒杰=80, 达混=20)
            add_jgfa1(self.driver, 埃斯坡=80, 达混=20)
            add_jgfa1(self.driver, 杰诺=80, 沙轻=20)
            # 初始化3加工方案，先删除全部，再添加需要的加工方案
            del_jgfa3(self.driver)
            pause(0.5)
            add_jgfa3(self.driver, 沙轻=80, 卡斯蒂利亚=20)
            add_jgfa3(self.driver, 沙中=80, 卡斯蒂利亚=20)
            add_jgfa3(self.driver, 巴士拉=80, 卡斯蒂利亚=20)
            add_jgfa3(self.driver, 沙轻=40, 沙中=40, 卡斯蒂利亚=20)
            pause(0.5)
        click_button(self.driver, "id", "btnStart")
        time.sleep(10)
        try:
            alert = self.driver.switch_to.alert
            message = alert.text
            alert.accept()
            self.assertIn(zdpc_keyword, message, zdpc_keyword + ' not in page_source')
        except Exception as e:
            error_screen(self.driver, '自动排产失败-' + time.strftime('%H%M%S') + '.png')
            print('自动排产失败原因：' + message)
            # print(traceback.format_exc())
            pause(0.5)
        else:
            capture_screen(self.driver, '自动排产-' + zdpc_keyword + time.strftime('%H%M%S') + '.png')
            print('自动排产成功')
        finally:
            time.sleep(5)
    #删除所以3#常减压方案，自动排产失败，页面提醒“请设置3#常加工方案”
    def test_autoprofail(self):
        try:
            enter_autopro(self.driver)
        except Exception as e:
            raise e
        else:
            print('原油转输调度系统登录成功')
        finally:
            # 初始化3加工方案，先删除全部，再添加需要的加工方案
            pause(0.5)
            del_jgfa3(self.driver)
            pause(0.5)
        click_button(self.driver, "id", "btnStart")
        time.sleep(10)
        try:
            alert = self.driver.switch_to.alert
            message = alert.text
            alert.accept()
            self.assertIn(zdpc_keyword, message, zdpc_keyword + ' not in page_source')
        except Exception as e:
            error_screen(self.driver, '自动排产失败-' + time.strftime('%H%M%S') + '.png')
            print('自动排产失败原因：'+message)
            # print(traceback.format_exc())
            pause(0.5)
        else:
            capture_screen(self.driver, '自动排产-' + zdpc_keyword + time.strftime('%H%M%S') + '.png')
            print('自动排产成功')
        finally:
            time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestAutoProduction("test_autoprofail"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    with open('HTMLForLogin.html', 'w')as fp:
        runner = HTMLTestRunner(stream=fp, title='auto report', description='report', verbosity=2)
        runner.run(suite)
