# Installation guide

## Download project from git

```
git clone https://github.com/Tykky/toto-betting
cd toto-betting
```

## Install dependencies through python pip
```
pip install -r requirements.txt
```

## Run the development server
```
python run.py
```

Now you should be able to view the site at [http://localhost:5000/](http://localhost:5000/). When the program is ran first time, the 
database should be created in application/database.db. Sqlite is used for the database on the development server (the one you are on). 
The database can be accessed with (make sure you have sqlite3 installed on your machine).

```
sqlite3 application/database.db
```

## Creating admin account

Create a new account through the web 
app as you would do in normal scenario. 
After creating the account you need to set the boolean "isadmin=True"
manually in the database for this freshly created user. If you chose 
to use the username: admin, this can be done with command (in sqlite)
```
UPDATE account SET isadmin = TRUE WHERE username = 'admin';
```

## Deploying project on heroku

The project can be deployd in heroku by forking this project on 
[github](https://github.com/Tykky/toto-betting) and then linking 
your github account with [heroku](https://www.heroku.com/). Any cloud provider would be sufficient so this is only a recommendation. The 
project contains configuration files for setting this up at heroku. 