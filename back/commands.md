

Allow to GET a full object but POST/PUT/DELETE with only an id on related fields
https://github.com/encode/django-rest-framework/issues/5206


# https://github.com/encode/django-rest-framework/issues/1337

# Packages

django
python-dotenv
djangorestframework
drf-spectacular
django-cors-headers

# Commands

## create list of packages:
pip freeze > requirements.txt

## install packages from list:
pip install -r requirement.txt

# create swagger documentation
py manage.py spectacular --file schema.yml

# run coverage analysis
coverage run -m pytest
or
pytest --cov