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
