README
======

The present repository contains a mini CRUD project using the FastApi python framework.

the crud is focused on user management.
the system will store all the users in memory, no database is used, because it is intended to demonstrate the operation of a CRUD. however the file in charge of controlling the storage of users in memory; storage.py can be replaced by a database connector and thus, make the system work.

the system validates the user's schema, validates that the email is unique, validates the format of the date of birth and validates the age.


Running locally
---------------

install dependencies
```bash
python3.9 -m pip install -r requirements.txt
```
To run locally, use the following commands:

```bash
python3.9 -m uvicorn app:app --reload
```

Then try to visit `http://localhost:8000/docs` or `http://localhost:8000/redoc` to see the documentation.
you can use the UI to run API tests and check its operation.

Running on Docker
---------------

```docker
docker pull 4311094/fastapi_crud_example:v3
docker run -it -d -p 8000:8000 fastapi_crud_example_api
```
Environment variables
---------------

| Environment | Default Value |
|-------------|-------|
| API_NAME | API_USUARIOS |
| API_PREFIX | /api/v1 |

Credentials
---------------

Test Header token: 
* 🔑 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9

This token is only an example. the token validation security system is not prepared for a productive environment.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## TO DO
- [ ] UML Diagrams
- [ ] Unitests
