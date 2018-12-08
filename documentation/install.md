# Asennusohjeet

Sovellus toimii Python 3.6 versiolla, lisäksi tarvitset PIP pakettienhallinnan sekä venv Python-virtuaaliympäristöä varten. Paikallista kehitystä varten tarvitset SQLite:n, tuotannossa (Heroku) käytetään Postgres-tietokantaa.

## Asennus paikalliseen ympäristöön

```bash
$ git clone https://github.com/vaahtokarkki/drinkkiarkisto.git
$ cd drinkkiarkisto
$ python3 -m venv venv
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

## Käyttöohje 