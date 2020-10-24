# Sending_Mail_with_Django

## Technology Stack

* Frontend
  * HTML
  * CSS
  * Bootstrap
* Backend
  * Django
* Database
  * SQLite3

## Tech Stack Involved

<div style="display: flex;justify-content: center;">

<img height="64px" width="auto" src="https://image.flaticon.com/icons/svg/919/919852.svg">
<img height="64px" width="auto" src="https://www.w3schools.com/whatis/img_css.jpg">
<img height="64px" width="auto" src="https://www.drupal.org/files/project-images/bootstrap-stack.png">
<img height="64px" width="auto" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/1200px-HTML5_logo_and_wordmark.svg.png">
<img height="64px" width="auto" src=m"https://twilio-cms-prod.s3.amazonaws.com/images/django-dark.width-808.png">

<div/>

<br/>
<br/>


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


## Useful Resources

- [Django Docs](https://docs.djangoproject.com/en/3.0/)
- [Bootstrap Docs](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
- [Django_Mail](https://docs.djangoproject.com/en/3.1/topics/email/)
- [Git and GitHub](https://www.digitalocean.com/community/tutorials/how-to-use-git-a-reference-guide)

