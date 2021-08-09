# environment sett
#......................................................................

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# In order for ChromeDriverManager to work you must pip install it in your own environment.

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"

driver.get(url)
head = 0

for i in range(99):
    driver.find_element_by_id("submit").click()
    if driver.find_element_by_xpath('//*[@id="lastResult"]').text == "fej":
        head = head+1
        print(head)

assert head > 30
print(f"Test passed! Number of heads = {head}")

driver.close()