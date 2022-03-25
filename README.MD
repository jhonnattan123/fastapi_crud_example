README
======

Running locally
---------------

install dependencies
```bash
pip install -r requirements.txt
```
To run locally, use the following commands:

```bash
uvicorn app:app --reload
```

Then try to visit `http://localhost:8000/docs` or `http://localhost:8000/redoc` to see the documentation.

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