#encoding=utf-8
from HTMLTestRunner import HTMLTestRunner
import unittest
from Action.action_login import *
from Action.test_data import *
from Action.basic_function import *

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=open_browser(browser_name)

    def test_login(self):
        for i in range(len(login_info)):
            try:
                login(self.driver, login_info[i])
                pause(3)
                self.assertIn(login_keyword, self.driver.page_source, login_keyword + ' not in page_source')
            except Exception as e:
                print('login error, ' + login_keyword + 'in page_source can not be found !')
                error_screen(self.driver, 'login-' + self.driver.find_element_by_id('lblError').text + time.strftime('%H%M%S') + '.png')
                #print(traceback.format_exc())
                print(self.driver.find_element_by_id('lblError').text)
            else:
                capture_screen(self.driver, 'login-成功' + time.strftime('%H%M%S') + '.png')
                print('login success, ' + login_keyword + 'in page_source can be found !')
                self.driver.find_element_by_link_text('退出').click()
            finally:
                print('login 第%d次用例执行结束' % (i + 1))
            pause(2)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestLogin('test_login'))
    with open('HTMLForLogin.html','w')as fp:
        runner=HTMLTestRunner(stream=fp,title='login report',description='report',verbosity=2)
        runner.run(suite)