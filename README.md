# college-portal

This is django based web app. In this we used Authentication With email, payment gateway integration for fees and admin portal.

Clone the project

```bash
  git clone https://github.com/jayvpatel112/college-portal.git
```

then make a python <b> virtual enviornment </b> using below command

```bash
  pip install virtualenv
```

```bash
  virtualenv portal
```

```bash
  .\portal\Scripts\activate
```

then install all below python packages

```bash
  pip install Django==4.0.1
```

```bash
  pip install pycryptodome==3.12.0
```

```bash
  pip install asgiref==3.4.1
```

```bash
  pip install sqlparse==0.4.2
```

```bash
  pip install tzdata==2021.5
```

#
then go to CollegeManagement folder then settings.py

line 143 : EMAIL_HOST_USER = 'email_id'

line 144 : EMAIL_HOST_PASSWORD = 'password'

in email_id -> put your email id

#
then go to Payment folder -> views.py add merchant key and id

line 7  : MERCHANT_KEY = 'WRITE_YOUR_MERCHANT_KEY'

line 34 : 'MID': 'WRITE_YOUR_MERCHANT_ID',

in password -> put your corresponding password

#
Start the server

```bash
  python manage.py runserver
```

then go to
http://127.0.0.1:8000/

for admin 
http://127.0.0.1:8000/admin

username- smit 

pass- smit

#
you can create your own superuser by using terminal

```bash
  python manage.py createsuperuser
```
