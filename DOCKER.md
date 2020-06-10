# How to Run (docker)

## Prerequisite
- [Docker](https://www.docker.com/)
- [MariaDB](https://mariadb.org/)
- https reverse proxy (such as [`nginx`](https://nginx.org/), [`haproxy`](http://www.haproxy.org/), [`envoy`](https://www.envoyproxy.io/) etc.)

## How to use this image
### Pull image from github package
``` bash
$ docker pull docker.pkg.github.com/skkuse/2020spring_41class_team9/modu:tag
```

### Run container
``` bash
$ docker run --name modu-server-name            \
    -e SECRET_KEY="django-secret-key"           \
    -e FIREBASE_API_KEY="firebase-api-key"      \
    -e MARIADB_DBNAME="mariadb-database-name"   \
    -e MARIADB_USERNAME="mariadb-username"      \
    -e MARIADB_PW="mariadb-password"            \
    -e MARIADB_HOST="mariadb-host-address"      \
    -e MARIADB_PORT="mariadb-port"              \
    -p port-to-bind:8086                        \
    -d docker.pkg.github.com/skkuse/2020spring_41class_team9/modu:tag
```

### Environment Variables
#### `SECRET_KEY`
This variable is mandatory and specifies the django secret key.

#### `FIREBASE_API_KEY`
This variable is mandatory and specifies firebase web api key.

#### `MARIADB_DBNAME`
This variable is mandatory and specifies the MariaDB database name to use.

#### `MARIADB_USERNAME`
This variable is mandatory and specifies the MariaDB username to access with.

#### `MARIADB_PW`
This variable is mandatory and specifies the MariaDB password to access with.

#### `MARIADB_HOST`
This variable is mandatory and specifies the MariaDB host to access to.

#### `MARIADB_PORT`
This variable is mandatory and specifies the MariaDB port number to access to.

#### `ALLOWED_HOST`
This variable is optional and specifies the allowed host of modu webserver.