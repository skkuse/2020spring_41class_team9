# How to Run (test server)

### 0. Prerequisite
- `mariaDB`
- `python` 3.7 or newer, with `pip` and `venv`

### 1. Create setting files
1) Write down secret keys in `./settings/secrets.json`
``` json
{
    "DJANGO_SECRET_KEY" : "put secret key"
    "FIREBASE_API_KEY"  : "put firebase api key"
}
```
2) Write down database information in `./settings/database.json`
``` json
{
    "MARIADB_DBNAME"    : "put db name",
    "MARIADB_USERNAME"  : "put user name",
    "MARIADB_PW"        : "put password",
    "MARIADB_HOST"      : "put host",
    "MARIADB_PORT"      : "put port"
}
```

### 2. Setup virtual environment
1) Create virtual environment on `./env`  
ex) on Windows cmd
``` cmd
py -m venv env
```
2) Get into virtual environment  
ex) on Windows cmd
``` cmd
cd ./env/Scripts
activate
cd ../..
```

### 3. Install required packages
In virutal environment, install required packages from ./requirements.txt  
ex) on Windows cmd
``` cmd
py -m pip install -r requirements.txt
```

### 4. Migrate django
In virutal environment, migrate django  
ex) on Windows cmd
``` cmd
py manage.py makemigrations
py manage.py migrate
```

### 5. Run server
In virutal environment, run server  
ex) on Windows cmd
``` cmd
py manage.py runserver
```