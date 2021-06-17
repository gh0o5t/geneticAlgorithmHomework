# Genetikus algoritmus beadando, Bene Robert ZAT9CR
### Kornyezet es feltetelek
 - Adott egy X * Y felbontasu terulet.
 - A teruleten adott (x, y) pozicioban van egy *w* szeles es *h* magassagu celpont.
 - A teruleten adott (x, y) pozicioban van egy *w* szeles es *h* magassagu robot.
 - Ismerjuk az *x,y,w,h* ertekeket a robot es a celpont vonatkozasaban.
 - A robot kepes balra, jobbra, fel, le mozogni a teruleten.
 - A program Python3-ban keszult.
 - A feladat vizualizalasara Pygame konyvtar kerult felhasznalasra.

### Cel
 - Talalni a robotnak egy olyan lepessorozatot, hogy elerje a celpontot.

### Genetikus algoritmus leirasa feladat vonatkozasaban
 - Gen: a robot egy lepese egy adott iranyba
 - A gen kodolasa:

     - 1 - Bal  
     - 2 - Jobb  
     - 3 - Fel  
     - 4 - Le
 - Kromoszoma: a robot teljes lepessorozata
 - Egyed: robot egy lepessorozattal, egy lehetseges megoldas
 - Populacio: osszes egyed a lehetseges lepessorozatokkal

### Valtoztathato parameterek
 - A valtoztathato parameterek a config.py-ban talalhatok:
     - Kromoszoma hossza
     - Populacio merete
     - Generaciok maximalas szama
     - Populacio mutacios faktor
     - Gen mutacios faktor
     - Kepernyo felbontasa
     - Robot merete
     - Celpont merete
     - Robot kiindulopontja (randomizalhato egy segitofuggveny meghivasaval)
     - Celpont kiindulopontja (randomizalhato egy segitofuggveny meghivasaval)
     

### Genetikus algoritmus pszeudokodja

- `Kezdeti populacio letrehozasa (0. generacio)`
- `A populacio egyedeinek fo mozgasiranyanak meghatarozasa`
- `A populacio egyedeinek alveletlen mozgatasa`
- `A 0. generacio fitneszenek kiszamitasa`
- `Ameddig a ciklusok szama nem egyenlo a max generaciok szamaval`
    - `A populacio keresztezese`
    - `Utodok fitnesz ertekenek kiszamitasa`
    - `Utodok mutacioja`
    - `Mutalt egyedek fitneszenek az ujraszamolasa`
    - `Az uj populacio = a keresztezett es mutalt egyedek`
    - `Generacio szamanak novelese`
    - `Ha valamelyik egyed elerte a celpontot visszater a program`


### Algoritmus megyarazata
*Megjegyzes: az algoritmus pszeudokodjaba nem kerult bele a vizulizalashoz szukseges lepesek sora, csak a genetikus algoritmusra vonatkozo reszek.*  

- A populacio egyedeinek mozgatasa a 0. generacioban pseudorandom modon tortenik, mivel minden egyednek van egy fo mozgasiranya.
Ez javitja a celpont megtalalasanak a lehetoseget, mivel igy a terulet minden iranyaba el fog mozdulni a kezdeti a populacio ahelyett, hogy
teljesen a veletlenre biznank a mozgasukat 

- A fintesz ertek kiszamitasa a robot es a celpont pixeleinek tavolsagan alapul

- A generaciok maximalizalasa a megoldhatatlan problema eseten meggatolja a vegtelen futast, alapvetoen nem ez a terminalasi feltetele a ciklusnak, hanem a celpont elerese

- A populacio keresztezese magaba foglalja a szelekciot is (Parverseny)

- A populacio mutacioja soran a populaciora vonatkoztatott mutacios faktor alapjan kerul veletlenszeruen kivalasztasra bizonyos mennyisegu egyed
    - Mutalt egyedek szama = osszes egyed * populacios mutacios faktor

- Az egyed mutacioja soran veletlenszeruen kerul kivalasztasra az egyedre vonatkoztatott mutacios faktor alapjan az egyed genallomanyanak egy resze
    - Mutalt genek szama = kromoszoma hossza * egyed mutacios faktor

### Eredmenyek
- A config.py fajlban talalhato parameterekkel az algoritmus 1200 futas soran atlagosan a 13. generaciora talalta meg a celponthoz vezeto lepessorozatot.







