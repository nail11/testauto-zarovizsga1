## 1 Feladat: Keressük a téglalap kerületét
#Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

#A program töltse be a téglalap kerülete app-ot az
# [htps://black-moss-0a0440e03.azurestaticapps.net/x234.html]
# (https://black-moss-0a0440e03.azurestaticapps.net/x234.html) oldalról.

#Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a téglalap kerülete
# appban:

#Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

#* Helyes kitöltés esete:
   # * a: 99
    #* b: 12
    #* Eredmény: 222

#* Nem számokkal történő kitöltés:
   # * a: kiskutya
   # * b: 12
   # * Eredmény: NaN

#* Üres kitöltés:
   # * a: <üres>
   # * b: <üres>
    #* Eredmény: NaN

# environment settings
#......................................................................

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

# In order for ChromeDriverManager to work you must pip install it in your own environment.

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"

driver.get(url)

# element
input_a = driver.find_element_by_xpath('//*[@id="a"]')
input_b = driver.find_element_by_xpath('//*[@id="b"]')
submit = driver.find_element_by_xpath('//*[@id="submit"]')
calc = driver.find_element_by_xpath('//*[@id="result"]')

# test data

test_case1 = (99, 12, 222)
print(int(test_case1[0]))
print(test_case1[1])

test_case2 = ("kiskutya", 12, "NaN")
test_case3 = ("","","NaN")

def circumference(x, y):
    input_a.clear()
    input_a.send_keys(int(x))
    input_a.clear()
    input_b.send_keys(int(y))
    submit.click()
    return calc.text


assert circumference(test_case1[0], test_case1[1]) == test_case1[2]


driver.close()