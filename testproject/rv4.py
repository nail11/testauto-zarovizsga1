#Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

#A progröltse be a Kakukktojás - városok app-ot az
# [https://black-moss-0a0440e03.azurestaticapps.net/rv4.html]
# (https://black-moss-0a0440e03.azurestaticapps.net/rv4.html) oldalról.

#Feladatod, hogy automatizáld selenium webdriverrel a Kakukktojás - városok app tesztelését.

#Az applikáció minden frissítésnél véletlenszerűen változik!

#Feladatod, hogy megtaláld a hiányzó városnevet, kitöltsd a form-ban a mezőt és ellnörizd le,
# hogy eltaláltad-e.

#Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos,
# hogy `assert` összehasonlításokat használj!

### A megoldás beadása
#* a megoldásokat a `testproject` mappába tedd, `rv4.py

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

url = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"

driver.get(url)


#elements

input_field = driver.find_element_by_xpath('//*[@id="missingCity"]')
check_but = driver.find_element_by_xpath('//*[@id="submit"]')

# makinin city list
city_names = ()
city_list = driver.find_elements_by_xpath('//*[@id="randomCities"]/li')
for i in range(len(city_list)):
    city_names.append(city_list[i])

# nincs több időm, de - a texarea-ból kiveszem a neveket, és listává alakítom, sorba rakom a
#két listát és elemeiket páronkánt összehasonlítom. Ahol a *párok tagjai nem egyeznek, ott van az
# eltérés a két listában, ott van a hiány