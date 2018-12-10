# Asennusohjeet

Sovellus toimii Python 3.6 versiolla, lisäksi tarvitset PIP pakettienhallinnan sekä venv Python-virtuaaliympäristöä varten. Paikallista kehitystä varten tarvitset SQLite:n, tuotannossa (Heroku) käytetään Postgres-tietokantaa.

## Asennus paikalliseen ympäristöön

```bash
$ git clone https://github.com/vaahtokarkki/drinkkiarkisto.git
$ cd drinkkiarkisto
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 run.py
```

Nyt sovelluksen pitäisi olla käytettävissä osoitteessa ``localhost:5000``

## Asennus tuotantoympäristöön (Heroku)

Luo [Herokuun](http://heroku.com) tunnus ja asenna [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). 
Luo sovellus Herokuun (vaihda nimi drinkkiarkisto):  
```bash
$ heroku create drinkkiarkisto
```  
Aseta ``heroku`` ympäristömuuttuja, jotta tuotannossa käytetään Postgres-tietokantaa:  
```
$ heroku config:set HEROKU=1
```  
Lisää Heroku-sovellukselle Postgres-tietokanta:
```bash
$ heroku addons:add heroku-postgresql:hobby-dev
```  
Lisää git-versionhallintaan Herokun osoite (muuta osoite vastaamaan sovelluksesi nimeä):  
```bash
git remote add heroku https://git.heroku.com/drinkkiarkisto.git
```  
Lähetä sovellus Herokuun:  
```bash
$ git add .
$ git commit -m "Initial commit"
$ git push heroku master
```

# Käyttöohje 

### Kirjautuminen ja rekisteröityminen

Sivun oikeasta yläreunasta voit kirjautua tai voi rekisteröityä uudeksi käyttäjäksi. Rekisteröityessä tarvitsen käyttäjänimen ja salasanan.

### Drinkkien haku ja selaaminen

Etusivulla voit hakea vapaalla sanahaulla drinkkejä. Tuloksissa on kaikki drinkit joissa nimi, valmistusohjeet, ainesosat tai avainsanat täsmäävät hakusanaan. Etusivulla ja yläpalkissa on myös painikkeet, joista pääset selaamaan kaikkia drinkkejä, ainesosia sekä avainsanoja. Ainesosien ja avainsanojen listauksesta pääset myös selaamaan kaikkia drinkkejä jotka sisältävät jonkun näistä. Drinkin nimeä klikkaamalla pääset tarkastelemaan yksittäistä drinkkiä. 

### Drinkin lisääminen

Lisätäksesi drinkin tarvitset käyttäjätunnuksen. Kun olet kirjautunut sisään, voit yläpalkista valita *Lisää uusi drinkki* ja pääset luomaan drinkin. Anna drinkille kuvaava nimi ja kirjoita sille mahdolliset valmistusohjeet, kuten missä järjestyksessä ainesosat kuuluu lisätä. Lisää drinkin ainesosat valitsemalla kukin niistä luettelosta ja antamalla määrä. Yksikkö jossa muodossa ainesosan määrä annetaan, on ilmoitettu ainesosan vieressä sulkuihin merkattuna. Lisää ainesosia drinkkiin saat lisättyä *Lisää ainesosa* napista. Lopuksi valitse ruksittamalla mahdolliset avainsanat drinkille, esimerkiksi jos drinkki on tunnettu jollakin muulla nimellä ja mahdolliset kategoriat.

#### Uusien ainesosien ja avainsanojen lisääminen

Jos palvelusta ei löydy haluamiasi ainesosia tai drinkkejä, voit lisätä ne erikseen *Selaa ainesosia* ja *Selaa avainsanoja* sivujen kautta. Myös näiden lisäämiseen tarvitset käyttäjätunnukset. 

## Käyttäjäprofiilit

Pääset tarkastelemaan omaa profiiliasi kun olet kirjautunut sisään yläpalkin *Oma profiili* napista. Myös jokaisen drinkin yhteydessä on linkki drinkin lisänneen käyttäjän profiilin. Profiilisivulla on listattu käyttäjän lisäämät drinkit, käyttäjän tiedot sekä tieto käyttäjän statuksesta (käyttäjä, ylläpitäjä jne.). Jos olet kirjautuneena sisään pääset myös muokkaamaan omaa profiiliasi profiilisivun kautta. 

---

## Ylläpitäjien ominaisuudet

Ylläpitäjästatuksen omaavilla käyttäjillä sivun yläpalkissa on linkki ylläpitosivulle. Sivulla on listattuna uudet, hyväksyntää odottavat drinkit, ainesosat ja avainsanat. Jokaisen hyväksyntää odottavan kohteen vieressä on nappi jolla sen voi hyväksyä ja kohde tulee julkisesti näkyviin, tai sen voi poistaa kokonaan. **Huom:** On syytä hyväksyä ensin uudet ainesosat ja avainsanat. Muuten julkisesti näkyvillä olevassa drinkissä voi olla hyväksymättömiä ainesosia ja avainsanoja, jolloin ne eivät näy käyttäjille ja lopputulos drinkistä voi olla sekava.

Ylläpidon etusivulta pääsee *Hallitse käyttäjiä* napista selaamaa, muokkaamaan ja poistamaan palveluun rekisteröityneitä käyttäjiä. Ylläpitäjänä voit myös muuttaa käyttäjien rooleja.  

Kun olet kirjautuneena ylläpitäjänä, pääset muokkaamaan drinkkejä, ainesosia, avainsanoja ja käyttäjien tietoja  myös sivulta joissa hakutuloksia on listattu (kuten hakutuloksista).