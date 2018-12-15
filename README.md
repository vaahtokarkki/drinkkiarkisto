# Drinkkiarkisto

## Palvelu drinkkireseptien hakemiseen

[Demo drinkkiarkistosta](https://drinkarchive.herokuapp.com/)  
**Demon testitunnukset**  
Normaali käyttäjä:  
`käyttäjätunnus: test`  
`salasana: 123456`  
Ylläpitäjä:  
`käyttäjätunnus: admin`  
`salasana: adminadmin`

## Ajatuksia harjoitustyöstä
Lähes kaikki suunnitellut käyttötapaukset on toteutettu ja sovelluksen käytettävyys on melko hyvä. Uuden drinkin lisäämiseen olisin halunnut samaan lomakkeeseen myös mahdollisuuden lisätä uusia ainesosia ja avainsanoja tietokantaa, jos niitä ei valikosta löydy valmiina. Tämä ei kuitenkaan ollut aivan yksinkertainen toteuttaa, joten jätin sen pois. Myös drinkin muokkaamiseen olisin halunnut mahdollisuuden poistaa ja lisätä ainesosia, mutta tässä oli vaikeuksia riippuvuuksien kanssa ja suurehko mahdollisuus rikkoa koko sovellus viime metreillä.

Olen lopputulokseen kuitenkin tyytyväinen ja sain sovelluksesta kutakuinkin sellaisen mitä olin alun perin ajatellut.

## Aihekuvaus
Drinkkireseptit kuvaavat cocktaileja ja muita juomasekoituksia. Reseptejä voi hakea juoman nimeen liittyvällä hakusanalla, jonkin ainesosan tai drinkin tyypin (alkudrinkki, cocktail, shotti,jne) mukaan. Reseptejä voi tarkastella myös listana, aakkosjärjestyksen, ainesosan tai juoman tyypin mukaan. 

Juomia hakiessa samalla hakusanalla voi saada useita eri tuloksia tai samaan juomaan voidaan viitata usealla hakusanalla. Jokaiseen drinkkiin voi viitata yksi tai useampi avainsana, esimerkiksi jos drinkki on tunnettu usealla nimellä, voi muut nimet olla drinkin avainsanoina. 

Järjestelmään kirjaudutaan sisään, jos haluaa lisätä omia reseptejä. Tavallinen käyttäjä voi hakea drinkkireseptejä kannasta ja ehdottaa uusien lisäämistä kantaan. Järjestelmän ylläpitäjä voi lisätä järjestelmän reseptejä joko kokonaan itse tai ehdotettuja hyväksymällä. Lisääminen tapahtuu lisäämällä reseptin tiedot lomakkeeseen ja lähettämällä ne hyväksyttäväksi. Järjestelmän ylläpitäjä voi antaa myös tavallisille käyttäjille oikeuden lisätä reseptejä ilman hyväksyntää.

### Toimintoja käyttäjille
* Hae hakusanalla
* Näytä listana
* Järjestä lista nimen, tyypin tai ainesosan mukaan
* Lisää resepti
* Näytä omat reseptit
* ~~Muokkaa omia reseptejä, vaatii ylläpidon hyväksynnän)~~

### Lisätoimintoja ylläpitäjälle
* Hyväksy resepti arkistoon
* Poista resepti
* Anna oikeuksia käyttäjälle
* Listaa käyttäjät
* Poista käyttäjä
* Muokkaa reseptejä

## Dokumentaatio
* [Asennus ja käyttöohjeet](documentation/install.md)
* [Käyttötapaukset](documentation/userstory.md)
* [Käyttötapauksien SQL-kyselyt](documentation/sqlqueries.md)
* [Tietokannan dokumentaatio](documentation/database.md)