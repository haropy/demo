# coding:utf-8
from selenium import webdriver
import re, time, pprint, xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('E-mails')

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://www.baidu.com")
driver.find_element_by_xpath("//*[@id='lh']/a[text()='关于百度']").click()
driver.find_element_by_xpath("//*[@id='indexAdmin']/div[1]/div/div/div/div[2]/ul/li[4]/a").click()
print(driver.current_window_handle)
handles = driver.window_handles
print(handles)
for handle in handles:
    if handle != driver.current_window_handle:
        driver.close()  # 关闭第一个窗口
        print('马上切换到新标签。', handle)
        driver.switch_to.window(handle)  # 切换到第二个窗口
# 得到页面源代码
doc = driver.page_source
# print(doc)
emails = re.findall(r'[\w]+@[\w\.-]+', doc)  # 利用正则，找出xxx@xxx.xxx 的字段，保存到emails列表
for index, email in enumerate(emails):
    ws.write(index, 0, email)
    print(email)
wb.save('百度联系邮箱.xls')
print('提取完成')
driver.close()
