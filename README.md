# college-portal

first download project from github
then make a python virtual enviornment

pip install virtualenv
virtualenv portal
.\portal\Scripts\activate

then install all below python packages
asgiref==3.4.1
Django==4.0.1
pycryptodome==3.12.0
sqlparse==0.4.2
tzdata==2021.5

then go to CollegeManagement folder then settings.py

at last
line 143 : EMAIL_HOST_USER = 'email_id'
line 144 : EMAIL_HOST_PASSWORD = 'password'

in email_id -> put your email id
in password -> put your corresponding password

then go to Payment folder -> views.py add merchant key and id
line 7  : MERCHANT_KEY = 'WRITE_YOUR_MERCHANT_KEY'
line 34 : 'MID': 'WRITE_YOUR_MERCHANT_ID',


then in terminal go to college-portal folder
then run
python manage.py runserver

then go to
http://127.0.0.1:8000/

for admin 
http://127.0.0.1:8000/admin

username- smit 
pass- smit

you can create your own superuser by using terminal

python manage.py createsuperuser
