# Genetikus algoritmus program dokumentacio
## A feladat leirasa
### Kornyezet es feltetelek
 - Adott egy X * Y felbontasu terulet.
 - A teruleten adott (x, y) pozicioban van egy *w* szeles es *h* magassagu celpont.
 - A teruleten adott (x, y) pozicioban van egy *w* szeles es *h* magassagu robot.
 - Ismerjuk a x,y,w,h ertekeket a robot es a celpont vonatkozasaban.
 - A robot kepes balra, jobbra, fel, le lepni a teruleten.
 - A program Python3-ban keszult
 - A feladat vizualizalasara Pygame konyvtar kerult felhasznalasra

### Cel
 - Talalni a robotnak egy olyan lepessorozatot, hogy elerje a celpontot.

### Genetikus algoritmus 
 - Gen: a robot egy lepese egy adott iranyba
 - A gen kodolasa:

     1 - Bal,
     2 - Jobb,
     3 - Fel,
     4 - Le

 - Kromoszoma: a robot teljes lepessorozata
 - Egyed: robot egy lepessorozattal, egy lehetseges megoldas
 - Populacio: robot a meghatarozott mennyisegu lehetseges lepessorozatokkal

### Valtoztathato parameterek
 - A valtoztathato parameterej a config.py-ban talalhatok.
 - Kromoszoma hossza
 - Populacio merete
 - Kepernyo felbontasa
 - Robot merete
 - Celpont merete
 - Robot kiindulopontja (randomizalhato egy segitofuggveny meghivasaval)
 - Celpont kiindulopontja (randomizalhato egy segitofuggveny meghivasaval)
 
