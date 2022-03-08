# Mission Innovation RETSful API
This API allow you to do some CRUD operation with RESTful methods over the Mission Innovation mongoDB.

## Configure
Use the `env.sample` to setup your mongoDB URI and save it as `.env`.

## Run for development (locally)

  1. Get the environment varibales:
     ```bash
     export $(xargs < .env)
     ```
  2. Install virtualenv:
     ```bash
     python3 -m venv $ENV_BASE_DIR/$ENVIRONMENT_NAME
     cd $ENV_BASE_DIR; virtualenv $ENVIRONMENT_NAME
     cd <path/to/>/opendigitalheritage-api
     pip install -r requirements.txt
     ```
     where:
       - $ENV_BASE_DIR: virtual envs folder
       - $ENVIRONMENT_NAME: your virtual env name
  3. Run the app:
     ```bash
     python app/main.py
     ```
## Run for production (containerized)
  1. Build container:
     ```bash
     make build
     ```
  2. Run container
     ```bash
     make run
     ```
Or, if you want to build and run in one command:
```bash
make all
```

## Check API
```bash
curl http://0.0.0.0:8000/api
```
If all is working properly, you'll get this output:
```json
{"message": "Welcome to the Mission Innovation API"}
```

## Check documentation
Go to [http://0.0.0.0/api/docs](http://0.0.0.0/api/docs) to get a complete and interactive documentation on APIs, where you can test routes.


## ToDo
 - [X] Add CORS policies
 - [ ] Add GET routes
 - [ ] Add POST routes
 - [ ] Add PUT routes
 - [ ] Add DELETE routes
 - [ ] Add GraphQL support
 - [ ] Add Authentication 
