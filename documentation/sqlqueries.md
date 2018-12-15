# Keskeisimpien käyttötapauksien SQL-kyselyt

## Drinkkien listaus

#### Listaa kaikki drinkit
```SQL
SELECT drink.id AS drink_id, drink.date_created AS drink_date_created, drink.date_modified AS drink_date_modified, drink.name AS drink_name, drink.instructions AS drink_instructions, drink.accepted AS drink_accepted, drink.account_id AS drink_account_id 
FROM drink 
WHERE drink.accepted = ? ORDER BY drink.name
```

#### Listaa drinkit ainesosan perusteella
**Hae drinkit**
```SQL
SELECT drink.name, drink.id FROM drink
JOIN drink_ingredient ON drink_ingredient.drink_id = drink.id
JOIN ingredient ON ingredient.id = drink_ingredient.ingredient_id
AND drink.accepted = '1' AND ingredient.id = ?;
SELECT * FROM ingredient WHERE ingredient.id = ? --Hae ainesosa tulossivulle
```

#### Listaa drinkit avainsanan perusteella
```SQL
SELECT * FROM drink 
WHERE drink.accepted = ?
AND (EXISTS (SELECT 1 FROM keywords_helper, keyword WHERE drink.id = keywords_helper.drink_id AND keyword.id = keywords_helper.keyword_id AND keyword.id = ?))
AND (EXISTS (SELECT 1 FROM keywords_helper, keyword WHERE drink.id = keywords_helper.drink_id AND keyword.id = keywords_helper.keyword_id AND keyword.accepted = '1');
SELECT * FROM keyword WHERE keyword.id = ? --Hae avainsana tulossivulle
```

### Hae drinkkejä hakusanalla

```SQL
SELECT drink.id AS drink_id, drink.date_created AS drink_date_created, drink.date_modified AS drink_date_modified, drink.name AS drink_name, drink.instructions AS drink_instructions, drink.accepted AS drink_accepted, drink.account_id AS drink_account_id 
FROM drink 
WHERE drink.accepted = ? AND ((drink.name LIKE '%' || ? || '%') OR (drink.instructions LIKE '%' || ? || '%') OR (EXISTS (SELECT 1 FROM drink_ingredient, ingredient 
WHERE drink.id = drink_ingredient.drink_id AND (ingredient.name LIKE '%' || ? || '%'))) OR (EXISTS (SELECT 1 
FROM keywords_helper, keyword 
WHERE drink.id = keywords_helper.drink_id AND keyword.id = keywords_helper.keyword_id AND (keyword.name LIKE '%' || ? || '%'))))
```

#### Listaa käyttäjän lisäämät drinkit
```SQL
SELECT * FROM drink 
WHERE drink.account_id = ?
```

## Ainesosien ja avainsanojen listaus
**Ainesosat**
```SQL
SELECT * FROM ingredient 
WHERE ingredient.accepted = '1'
ORDER BY ingredient.name
```
**Avainsanat**
```SQL
SELECT * FROM keyword 
WHERE keyword.accepted = '1'
ORDER BY keyword.name
```

## Kirjautuminen ja rekisteröityminen
**Sisään kirjautuminen**
```SQL
SELECT * FROM account 
WHERE account.username = ? AND account.password = ?
```
**Rekisteröityminen**
Tarkista onko jo käyttäjää:
```SQL
SELECT * FROM account 
WHERE account.username = ? AND account.password = ?
```
Luo käyttäjä:
```SQL
INSERT INTO account (date_created, date_modified, name, username, password, roles)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```
## Drinkin lisääminen
```SQL
INSERT INTO drink (date_created, date_modified, name, instructions, accepted, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
INSERT INTO keywords_helper (keyword_id, drink_id) VALUES (?, ?)
INSERT INTO drink_ingredient (date_created, date_modified, amount, drink_id, ingredient_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
INSERT INTO drink_ingredient (date_created, date_modified, amount, drink_id, ingredient_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```

## Lisää ainesosia ja avainsanoja
**Lisää ainesosa**
```SQL
INSERT INTO ingredient (date_created, date_modified, name, unit, accepted, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```
**Lisää avainsana**
```SQL
INSERT INTO ingredient (date_created, date_modified, name, unit, accepted, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```

## Ylläpito-ominaisuudet
### Hyväksy kohteita
**Hyväksy drinkki**
```SQL
UPDATE drink SET date_modified=CURRENT_TIMESTAMP, accepted=? WHERE drink.id = ?
```
**Hyväksy ainesosa**
```SQL
UPDATE ingredient SET date_modified=CURRENT_TIMESTAMP, accepted=? WHERE ingredient.id = ?
```
**Hyväksy avainsana**
```SQL
UPDATE keyword SET date_modified=CURRENT_TIMESTAMP, accepted=? WHERE keyword.id = ?
```

### Poista drinkki
```SQL
UPDATE drink_ingredient SET date_modified=CURRENT_TIMESTAMP, drink_id=? WHERE drink_ingredient.id = ?
DELETE FROM drink WHERE drink.id = ?
```

### Hallitse käyttäjiä
**Listaa kaikki käyttäjät**
```SQL
SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password, account.roles AS account_roles
FROM account
```
**Poista käyttäjä**
```SQL
UPDATE drink SET date_modified=CURRENT_TIMESTAMP, account_id = None WHERE drink.id = ?
DELETE FROM account WHERE account.id = ?
```
**Muokkaa käyttäjää**
```SQL
UPDATE account SET date_modified=CURRENT_TIMESTAMP, username=?, roles=? WHERE account.id = ?
```

## Yhteenvetokyselyt
**Luo TOP-5 listaus eniten drinkkejä lisänneistä käyttäjistä**
```SQL
SELECT account.id, COUNT(account.id) as drinkCount
FROM account
LEFT JOIN drink ON drink.account_id = account.id
WHERE (drink.accepted = '1')
GROUP BY account.id
HAVING COUNT(drink.id) > 0
ORDER BY drinkCount DESC
LIMIT 5
```

**Hae keskimääräinen ainesosien määrä drinkissä**
```SQL
SELECT ROUND(AVG(count),2)
FROM (
SELECT COUNT(drink_ingredient.ingredient_id) as count
FROM drink
JOIN drink_ingredient on drink.id = drink_ingredient.drink_id
WHERE (drink.accepted = '1')
GROUP BY drink.id
) AS result
```