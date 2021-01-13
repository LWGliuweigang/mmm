import unittest
import time
import pyautogui
from selenium import webdriver
from HTMLTestRunnerNew import HTMLTestRunner
class Denglu(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.we = webdriver.Firefox()
        self.we.get("http://123.57.140.190/manage")
        time.sleep(5)
        self.we.find_element_by_name("Username").send_keys("admin")
        self.we.find_element_by_name("Password").send_keys("admin999")
        self.we.find_element_by_name("Submit").click()
        time.sleep(5)
    @classmethod
    def tearDownClass(self):
        self.we.close()
        self.we.quit()
    # @unittest.skip
    def test_deng(self):
        try:
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.we.find_element_by_name("pro_name").send_keys("山药")
            time.sleep(5)
            self.we.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/button").click()
            time.sleep(5)
            aa=self.we.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[4]/a").text
            self.assertEqual(aa,"山药",msg="出现错误")
        except Exception as a:
            print("异常为",a)
    # @unittest.skip
    def test_deng1(self):
        try:
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.we.find_element_by_name("pro_name").send_keys("")
            time.sleep(5)
            self.we.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/button").click()
            time.sleep(5)
            aa = self.we.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[4]/a").text
            self.assertIsNotNone(aa, not None)
        except Exception as a:
            print("异常为", a)
    # @unittest.skip
    def test_deng2(self):
        try:
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.we.find_element_by_name("pro_name").send_keys("哈哈")
            time.sleep(5)
            self.we.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/button").click()
            time.sleep(5)
            aa=self.we.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/section/header").text
            self.assertEqual(aa,"删除已选产品",msg="出现错误")
        except Exception as a:
            print("异常为",a)
    # @unittest.skip
    def test_deng3(self):
        try:
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.we.find_element_by_name("cpbh").send_keys("0025")
            time.sleep(5)
            self.we.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/button").click()
            time.sleep(5)
            aa=self.we.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/table/tbody/tr/td[5]").text
            self.assertEqual(aa,"0025",msg="出现错误")
        except Exception as a:
            print("异常为",a)
    # @unittest.skip
    def test_deng4(self):
        try:
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.we.find_element_by_name("cptxm").send_keys("0035")
            time.sleep(5)
            self.we.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/button").click()
            time.sleep(5)
            aa=self.we.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/table/tbody/tr/td[6]").text
            self.assertEqual(aa,"0035",msg="出现错误")
        except Exception as a:
            print("异常为",a)
    # @unittest.skip
    def test_deng5(self):
        try:
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.we.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/a/button").click()
            time.sleep(5)
            aa = self.we.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[4]/a").text
            self.assertEqual(aa,"")
        except Exception as a:
            print("异常为", a)
    # @unittest.skip
    def test_deng6(self):
        try:
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.we.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[7]/span").click()
            time.sleep(5)
            aa = self.we.find_element_by_xpath("/html/body/div[4]/div[1]").text
            self.assertEqual(aa,"预览",msg="出现错误")
        except Exception as a:
            print("异常为", a)
    # @unittest.skip
    def test_deng7(self):
        try:
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.we.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/a").click()
            time.sleep(5)
            self.we.find_element_by_name("pro_name").clear()
            self.we.find_element_by_name("pro_name").send_keys("肉夹馍")
            self.we.find_element_by_name("cpbh").clear()
            self.we.find_element_by_name("cpbh").send_keys("1301")
            self.we.find_element_by_name("cptxm").clear()
            self.we.find_element_by_name("cptxm").send_keys("1201")
            time.sleep(2)
            # self.we.find_element_by_css_selector(".ke-edit-iframe").clear()
            self.we.find_element_by_css_selector(".ke-edit-iframe").send_keys("肉夹馍")
            time.sleep(2)
            self.we.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[9]/div/button").click()
            aa = self.we.find_element_by_xpath("/html/body/div[3]/div").text
            self.assertEqual(aa, "产品更新成功！", msg="出现错误")

        except Exception as a:
            print("异常为", a)
    # @unittest.skip
    def test_deng8(self):
        try:
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.we.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/span").click()
            self.we.find_element_by_css_selector(".layui-layer-btn0").click()
            aa = self.we.find_element_by_xpath("/html/body/div[3]/div").text
            self.assertEqual(aa, "产品删除成功！", msg="出现错误")

        except Exception as a:
            print("异常为", a)

    @unittest.skip
    def test_deng9(self):
        try:
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.we.find_element_by_xpath("//*[@id='chk[]']").click()
            self.we.find_element_by_xpath("//*[@id='del']").click()
            pyautogui.moveTo(672,279)
            pyautogui.click()
            pyautogui.moveTo(685,288)
            aa=pyautogui.text
            self.assertEqual(aa,"删除成功",msg="出现错误")
            pyautogui.moveTo(739,357)
            pyautogui.click()
        except Exception as a:
            print("异常为", a)
if __name__ == '__main__':
    z=unittest.TestSuite()
    z.addTest(Denglu("test_deng"))
    a=open(r'C:\Users\Dell\PycharmProjects\产品溯源\test_Report\test.html','wb')
    baogao=HTMLTestRunner(a,title="产品管理报告",description="用例描述",tester="小明")
    baogao.run(z)