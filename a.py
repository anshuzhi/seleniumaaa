from selenium import webdriver
import time
# chrome_options=webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(options=chrome_options) #  代码在执行的时候回自行去寻找chromedriver.exe(在python目录下寻找)，不再需要制定chromedriver.exe路径
driver = webdriver.Chrome() #  代码在执行的时候回自行去寻找chromedriver.exe(在python目录下寻找)，不再需要制定chromedriver.exe路径
driver.get("http://www.baidu.com")

driver.find_element_by_xpath('//*[@id="kw"]').send_keys("python")
driver.find_element_by_xpath('//*[@id="su"]').click()
# print(driver.current_url)
time.sleep(3)
data=driver.page_source

print(data)
# driver.quit()