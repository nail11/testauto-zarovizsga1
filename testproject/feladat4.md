## 4 Feladat: Email mező

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a Email mező app-ot az [https://black-moss-0a0440e03.azurestaticapps.net/mm43.html](https://black-moss-0a0440e03.azurestaticapps.net/mm43.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Email mező app tesztelését.

A cél az email validáció tesztelése:

* Helyes kitöltés esete:
    * email: teszt@elek.hu
    * Nincs validációs hibazüzenet

* Helytelen:
    * email: teszt@
    * Please enter a part following '@'. 'teszt@' is incomplete.

* Üres:
    * email: <üres>
    * Please fill out this field.

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `mm43.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(