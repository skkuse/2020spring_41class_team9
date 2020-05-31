# How to Run

### 0. Prerequisite
- mariaDB
- python 3.7
- pip
- virtualenvwrapper

### 1. Create virtual environment
create virtual environment on ./env  
ex) on Windows cmd
``` cmd
py -m venv env
```

### 2. Set virtual environment
In virutal environment, install required packages from ./requirements.txt  
ex) on Windows cmd
``` cmd
py -m pip install -r requirements.txt
```

### 3. Create setting files
1) Write down secret keys in `./settings/secrets.json`
``` json
{
    "DJANGO_SECRET_KEY" : "put secret key"
}
```

2) Write down database information in `./settings/database.json`
``` json
{
    "MARIADB_DBNAME" : "put db name",
    "MARIADB_USERNAME" : "put user name",
    "MARIADB_PW" : "put password",
    "MARIADB_HOST" : "put host",
    "MARIADB_PORT" : "put port"
}
```

### 4. Migrate django
In virutal environment, migrate django  
ex) on Windows cmd
``` cmd
py manage.py migrate
py manage.py makemigrations
```

### 5. Run server
In virutal environment, run server  
ex) on Windows cmd
``` cmd
py manage.py runserver
```