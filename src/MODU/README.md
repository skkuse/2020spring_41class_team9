# how to run

create virtual environment (ex - ./env)

install mariaDB

create setting files

- ./settings/secrets.json
    ``` json
    {
        "DJANGO_SECRET_KEY" : "put secret key"
    }
    ```

- ./settings/database.json
    ``` json
    {
        "MARIADB_DBNAME" : "put db name",
        "MARIADB_USERNAME" : "put user name",
        "MARIADB_PW" : "put password",
        "MARIADB_HOST" : "put host",
        "MARIADB_PORT" : "put port"
    }
    ```

and run server using visual studio on windows

or, though not tested, manually run the command
``` sh
py manage.py runserver
```
