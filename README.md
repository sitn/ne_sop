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


## Frontend
Move to front directory.
```
cd ..\..\front\
```


Run your server with vite.
```
vite
```
Open [http://localhost:5173/web/sop/#/login](http://localhost:5173/web/sop/#/login) in your browser. You should see the login page of your application.

# Deployment
## Backend
Follow Installation steps.

## Frontend
In your front directory, run the following to create the `dist` directory:
```
vite build
```
