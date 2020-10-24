# Sending_Mail_with_Django
## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone git@github.com:samir321-pixel/Sending_Mail_with_Django.git
```

## Install Requirements:

```bash
pip install -r requirements.txt
```

## Apply the migrations:

```bash
python manage.py migrate
```
## Add your GmailID and Password in settings.py
```
EMAIL_HOST_USER = 'yourgmailid.com'
EMAIL_HOST_PASSWORD = 'yourgmailpassword'
```

## Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **http://127.0.0.1:8000/**.

