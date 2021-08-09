## 4 Feladat: Email mező

#Készíts egy Pythpython applikációt (egy darab python file) ami selenium-ot használ.

#A program töltse be a Email mező app-ot az [https://black-moss-0a0440e03.azurestaticapps.net/mm43.html]
# (https://black-moss-0a0440e03.azurestaticapps.net/mm43.html) oldalról.

#Feladatod, hogy automatizáld selenium webdriverrel a Email mező app tesztelését.

#A cél az email validáció tesztelése:

#* Helyes kitöltés esete:
    #* email: teszt@elek.hu
    #* Nincs validációs hibazüzenet

#* Helytelen:
   #* email: teszt@
    #* Please enter a part following '@'. 'teszt@' is incomplete.

#* Üres:
    #* email: <üres>
   # * b: <üres>
   # * Please fill out this field.

#Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

### A megoldás beadása
#* a megoldásokat a `testproject` mappába tedd, `mm43.py`

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

url = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"

driver.get(url)

# test data

td = ("teszt@elek.hu", "teszt@", "")

response1 ="Kérjük, adja meg a „@” utáni részt is. A(z) „test@” cím nem teljes."
response2 = "Kérjük, töltse ki ezt a mezőt."

# elements
input_field = driver.find_element_by_xpath('//*[@id="email"]')
submit = driver.find_element_by_xpath('//*[@id="submit"]')
error = driver.find_element_by_xpath('/html/body/div/div/form/div')

def validation(test_data):
    input_field.send_keys(test_data)
    submit.click()
    response = error.get_attribute('value')
    return response

#TC1
assert validation(td[1]) == ""

#TC2
assert validation(td[1]) == response1

#TC3
assert validation(td[2]) == response2

driver.close()