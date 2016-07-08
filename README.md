# office_map
[![Build Status](https://travis-ci.org/VolVoz/office_map.svg?branch=master)](https://travis-ci.org/VolVoz/office_map)
## Building instructions
Clone repo
```
git clone https://github.com/VolVoz/office_map.git
```
Make virtualenv
```
virtualenv env
source env/bin/activate
```
Install requirements
```
pip install -r requirements.txt
```
Make migrations
```
python manage.py migrate
python manage.py makemigrations map
python manage.py migrate
```
Done.Then just run server
```
python manage.py runserver
```
