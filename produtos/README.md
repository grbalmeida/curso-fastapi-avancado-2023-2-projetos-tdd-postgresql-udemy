### Comando para subir a aplicação

```
docker compose up app
```

### Comando para subir banco de dados

```
docker compose up postgresql -d

```

### Comando para subir pgAdmin

```
docker compose up pgadmin -d
```

### Caso não crie o usuário e o banco automaticamente


```sql
CREATE DATABASE main;
CREATE USER admin WITH ENCRYPTED PASSWORD 'adminpass';
GRANT ALL PRIVILEGES ON DATABASE main TO admin;
```

### Comando para criar migration

```
docker-compose run --user 1000 app sh -c 'alembic revision --autogenerate -m "add categories table"'
```

### Comando para aplicar as migrações

```
docker-compose run --user 1000 app sh -c 'alembic upgrade head'
```