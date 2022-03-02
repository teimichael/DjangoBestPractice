# Django Best Practice

A scaffold for web development with Django, PostgreSQL, Docker, Gunicorn, and Nginx.

## Structure

~~~
├── .env.dev
├── .env.prod
├── .env.prod.db
├── .gitignore
├── app
│   ├── Dockerfile
│   ├── Dockerfile.prod
│   ├── entrypoint.prod.sh
│   ├── entrypoint.sh
│   ├── service
│   │   ├── __init__.py
│   │   ├── controllers
│   │   ├── models
│   │   └── templates
│   ├── web
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   └── requirements.txt
├── docker-compose.prod.yml
├── docker-compose.yml
└── nginx
    ├── Dockerfile
    └── nginx.conf
~~~

## Usage

### Development

Start up development server.

```shell
docker-compose up --build
```

Run in daemon mode.

```shell
docker-compose up -d --build
```

Stop and clear up.

```shell
# Stop containers and remove containers, networks, and images
docker-compose down --rmi "all"
# Remove volumes
docker volume prune
```

Stop and clear up everything (containers, networks, volumes, and images).

```shell
docker-compose down -v --rmi "all"
```

### Deployment

Build and start up.

```shell
docker-compose -f docker-compose.prod.yml up --build
```

Run in daemon mode.

```shell
docker-compose -f docker-compose.prod.yml up -d --build
```

Stop and clear up.

```shell
# Stop containers and remove containers, networks, and images
docker-compose -f docker-compose.prod.yml down --rmi "all"
# Remove volumes
docker volume prune
```

Stop and clear up everything (containers, networks, volumes, and images).

```shell
docker-compose -f docker-compose.prod.yml down -v --rmi "all"
```

### Issues

Permission issues of shell scripts

```shell
chmod +x app/entrypoint.sh
chmod +x app/entrypoint.prod.sh
```

---

## References

- https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
