# FAST-API APP


## How to run
```shell
python3 -m venv venv
```
```shell
. venv/bin/activate
```
```shell
pip install -r requirements.txt
```

Change filename example.env to .env:
```shell
mv example.env .env
```

To create database, open mysql via terminal with password "root":
```shell
mysql -u root -p
```
Run to create a database:
```
CREATE DATABASE mydatabase;
```


To run fast-api server, run from root folder:
```shell
uvicorn app.main:app --reload
```

To create a user, run:
```shell
curl -v -H "Content-Type: application/json" -X POST \
     -d '{"email":"your name","password":"111-111"}' http://127.0.0.1:8000/users/
```

To see encoded password, run:
```shell
http://127.0.0.1:8000/users/
```
