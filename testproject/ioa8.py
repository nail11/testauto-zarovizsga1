#Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

#A progrk-moss-0a0440e03.azurestaticapps.net/ioa8.html]
# (https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html) oldalról.

#Feladatod, hogy automatizáld selenium webdriverrel a összeadó app tesztelését.

#Az applikáció minden frissítésnél véletlenszerűen változik!

#A feladatod, hogy a random számokkal működő matematikai applikációt ellenőrizd.
# A teszted ki kell, hogy olvassa a két operandust (számot) és az operátort (műveleti jelet).
# Ennek megfelelően kell elvégezned a kalkulációt Pythonban.

#A kalkuláció gombra kattintva mutatja meg az applikáció, hogy mi a művelet eredménye szerinte.

#Hasonlítsd össze az applikáció által kínált megoldást és a Python által kalkulált eredményt.
# Ennek a kettőnek egyeznie kell.

#Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod
# (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

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

url = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"

driver.get(url)

# elements
num1 = driver.find_element_by_xpath('//*[@id="num1"]').text
num2 = driver.find_element_by_xpath('//*[@id="num2"]').text
op = driver.find_element_by_xpath('//*[@id="op"]').text
result = driver.find_element_by_xpath('//*[@id="result"]').text
submit_but = driver.find_element_by_xpath('//*[@id="submit"]')

# function
submit_but.click()


assert int(num1)+op+int(num2) == result

