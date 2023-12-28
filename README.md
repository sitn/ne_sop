# ne_sop
Suivi des objets parlementaires

# Installation
## Requirements 
This applications requires:
* Backend: [Python](https://www.python.org/) (v10), [Django REST framework](https://www.django-rest-framework.org/)
* Frontend: [Vite](https://vitejs.dev/) (v4)

## Backend
Open a terminal in the directory of your app.

Move to back folder:
```
cd .\back\
```

1. Create a new virtual environment and activate it.

```
python -m venv venv
venv\Scripts\activate
```

2. Install requirements.
```
pip install -r requirements.txt
```

3. Copy the file `.env.template` to `.env` and complete it with your configuration settings.

4. Move to your backend server.
```
cd .\ne_sop_backend\
```

5. Apply migrations.
```
python .\manage.py migrate
```

6. Launch your backend server and test if it works.
```
python .\manage.py runserver
```
Then open [http://127.0.0.1:8000/api/test](http://127.0.0.1:8000/api/test) in your browser, you should see "Congratulations! It works".


## Database

Are you starting with a new database? Then run this only once:

```
python manage.py loaddata entities.json entity-types.json items.json item-types.json item-status.json events.json event-types.json templates.json
```

⚠️ In case you use a Microsoft SQL Server, you will need to install the correct ODBC driver. In our case, this is the [version 17](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16#version-17).

## Frontend

In a new terminal, move to front directory and install

```
cd front
npm i
```

Run your server with vite.

```
vite
```

Open [http://localhost:5173/web/sop/#/login](http://localhost:5173/web/sop/#/login) in your browser. You should see the login page of your application.

# Deployment

## Backend

Follow Installation steps.

Configure Apache if needed

## Frontend

Start by copying your env.<instance>.template to env.<instance> and edit accordingly to your install.

Example:

```
cp env.production.template env.production
```

In your `front` directory, run the following to create the `dist` directory replacing <instance> by production or prepub:

```
npm i
npm run build -- --mode <instance>
```

# Swagger

All views are synthetised in a swagger which is based on the python [`drf.spectacular`](https://drf-spectacular.readthedocs.io/en/latest/index.html) library.
To create the `schema.yml` file, activate your virtual environment, go into `back\ne_sop_backend` and run:
```
python ./manage.py spectacular --color --file schema.yml
```

Then launch the service using the following command line:
```
docker run -p 80:8080 -e SWAGGER_JSON=/schema.yml -v ${PWD}/schema.yml:/schema.yml swaggerapi/swagger-ui
```

You can access the swagger using this url: [http://127.0.0.1:8000/api/schema/docs/](http://127.0.0.1:8000/api/schema/docs/)

