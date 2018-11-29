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

>Toiminnallisuudessa voi olla tällä hetkellä pieniä puutteita, esimerkiksi uusia ainesosia ja drinkin reseptiä ei voi lisätä samalla lomakkeella. Myös osassa lomakkeiden (lähinnä lisää uusi drinkki) tietojen validoinnissa voi olla vielä aukkoja, johtuen wtform kirjaston hankaluudesta kun kenttiä on dynaaminen määrä.

Drinkkireseptit kuvaavat cocktaileja ja muita juomasekoituksia. Reseptejä voi hakea juoman nimeen liittyvällä hakusanalla, jonkin ainesosan tai drinkin tyypin (alkudrinkki, cocktail, shotti,jne) mukaan. Reseptejä voi tarkastella myös listana, aakkosjärjestyksen, ainesosan tai juoman tyypin mukaan. 

Juomia hakiessa samalla hakusanalla voi saada useita eri tuloksia tai samaan juomaan voidaan viitata usealla hakusanalla. Jokaiseen drinkkiin voi viitata yksi tai useampi avainsana, esimerkiksi jos drinkki on tunnettu usealla nimellä, voi muut nimet olla drinkin avainsanoina. 

Järjestelmään kirjaudutaan sisään, jos haluaa lisätä omia reseptejä. Tavallinen käyttäjä voi hakea drinkkireseptejä kannasta ja ehdottaa uusien lisäämistä kantaan. Järjestelmän ylläpitäjä voi lisätä järjestelmän reseptejä joko kokonaan itse tai ehdotettuja hyväksymällä. Lisääminen tapahtuu lisäämällä reseptin tiedot lomakkeeseen ja lähettämällä ne hyväksyttäväksi. Järjestelmän ylläpitäjä voi antaa myös tavallisille käyttäjille oikeuden lisätä reseptejä ilman hyväksyntää.

### Toimintoja käyttäjille
* Hae hakusanalla
* Näytä listana
* Järjestä lista nimen, tyypin tai ainesosan mukaan
* Lisää resepti
* Näytä omat reseptit
* (Muokkaa omia reseptejä, vaatii ylläpidon hyväksynnän)
### Lisätoimintoja ylläpitäjälle
* Hyväksy resepti arkistoon
* Poista resepti
* Anna oikeuksia käyttäjälle
* Listaa käyttäjät
* Poista käyttäjä
* Muokkaa reseptejä

## Dokumentaatio
* [Käyttötapaukset](documentation/userstory.md)
* [Tietokannan dokumentaatio](documentation/database.md)