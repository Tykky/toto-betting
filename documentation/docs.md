# Toto-betting documentation

## User stories

* User can register and login
* User can view profile information (balance etc..)
* User can view current races
* User is able to place bets on current races
* Admin can perform user actions + create new races

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