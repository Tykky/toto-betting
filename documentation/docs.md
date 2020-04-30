# Toto-betting documentation

## User stories

* User can register and login
* User can view profile information (balance etc..)
* User can view current races
* User is able to place bets on current races
* Admin can perform user actions + create new races

## Create table SQL expressions


### User

´´´
CREATE TABLE user (
    userid INT PRIMARY KEY,
    date_created DATE,
    date_modified DATE,
    username VARCHAR(12),
    phash BINARY(60),
    credits DECIMAL,
    isadmin BOOLEAN
)
´´´