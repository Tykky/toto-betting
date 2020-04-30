# Toto-betting documentation


## Implemented features

* There are two user roles ( admin and regular user). Admin user has 
more features at disposal. Admin can create new races and add new horses 
while regular users cannot perform this.

* Regular users can place bets on races when admin has created those. 
Each racse has at least 2 horses since it wouldn't make much sense 
being able to place bet on a single horse. 

* Winner of each race (horse) is determined by throwing a dice (chosen randomly).

* Password hashing + salting through flask-bcrypt.



## User stories

* User can register and login
* User can view profile information (balance etc..)
* User can view current races
* User is able to place bets on current races
* Admin can perform user actions + create new races

## SQL in user stories

### Creating users in SQL

```
INSERT INTO account(username) VALUES (?)
```
### Viewing profile information in SQL
```
SELECT * FROM account WHERE username=?
```
### Setting admin privileges to a user (only possible in SQL)
```
UPDATE account SET isadmin=1 WHERE username=?
```
### Viewing bet history(note that bets can be deleted permanently)
```
SELECT account.username, race.name, race.location, bet.amount
                     FROM bet INNER JOIN race ON race.raceid = bet.raceid
                     INNER JOIN account ON account.userid = bet.userid");
```
### Viewing only current/open races
```
SELECT account.username, race.name, race.location, bet.amount
                     FROM bet INNER JOIN race ON race.raceid = bet.raceid
                     INNER JOIN account ON account.userid = bet.userid
                     WHERE race.isopen IS TRUE");
```
### Placing bet
```
INSERT INTO bet(userid,raceid,horseid) VALUES (?,?,?)
```

### Creating new races (admin only)

```
INSERT INTO race(name,location,description) VALUES (?,?,?)
```

## Create table SQL expressions
### User table
```
CREATE TABLE user (
    userid INT,
    date_created DATE,
    date_modified DATE,
    username VARCHAR(12),
    phash BINARY(60),
    credits DECIMAL,
    isadmin BOOLEAN,
    PRIMARY KEY (userid)
);
```

### Bet table
```
CREATE TABLE bet (
    betid INT,
    date_created DATE,
    amount DECIMAL,
    isopen BOOLEAN,
    userid INT,
    raceid INT,
    horseid INT,
    PRIMARY KEY (betid),
    FOREIGN KEY (userid) REFERENCES user(userid),
    FOREIGN KEY (raceid) REFERENCES race(raceid),
    FOREIGN KEY (horseid) REFERENCES horse(horseid)
);
```
### Race table
```
CREATE TABLE race (
    raceid INT,
    name VARCHAR(16),
    location VARCHAR(16),
    description VARCHAR(2000),
    isopean BOOLEAN,
    PRIMARY KEY (raceid)
);
```

### Connector table
```
CREATE TABLE connector (
    raceid INT,
    horseid INT,
    FOREIGN KEY (raceid) REFERENCES race(raceid),
    FOREIGN KEY (horseid) REFERENCES horse(horseid)
);
```
### Horse table
```
CREATE TABLE horse (
    horseid INT,
    name VARCHAR(12),
    breed VARCHAR(16),
    tier INT,
    description VARCHAR(2000),
    PRIMARY KEY (horseid)
);
```