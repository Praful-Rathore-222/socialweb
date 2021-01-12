# socialweb
This application is built for developing a social network with people. In this application there are many features that is sharing a post with the friends , family, colleagues, etc. And User can write a post,  do comments, likes on a post through their account and build a custom profile and get the updates about the world.

# Features
```
1) User can check everyone's post and also like and comment on the photos.
2) Users can edit or delete their photos too.
3) Users can search for posts by their username.
4) Without authentication, users can view the posts but cannot like or comment.
5) Registeration system is complete with password reset option also available to users.
6) Users can edit their profile including profile pic, first name , last name, email, country and a short bio about them.
7) Users can view profile of others users and can send them friend requests.
8) Users can send friend request, cancel requests, accept requests, reject requests or even unfriend their friends.


```

# Technology Stack :
I have used in my application,

```
1. Python 3
2. Django 3
3. sqlite3 Database
4. Google Chrome v.83.0.4103.61    
5. Google Chrome driver v.83.0.4103.61
6. Frontend - HTML, CSS, Javascript, Bootstrap
```
# Project Structure :
```
.
├── ecom_site
│   ├── ecom_site
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── images
│   │   └── avatar.png
│   ├── manage.py
│   ├── media
│   │   ├── images
│   │   │   ├── 249609.jpg
│   │   │   ├── avatar.png
│   │   │   ├── io.jpg
│   │   │   ├── Screenshot_2019-09-02_SecondProject.png
│   │   │   ├── spring-5016266_1920.jpg
│   │   │   └── tree-276014_1920.jpg
│   │   ├── path
│   │   │   └── to
│   │   │       └── img
│   │   │           ├── 249609.jpg
│   │   │           ├── 67.jpg
│   │   │           ├── 99_81cGbE9.jpg
│   │   │           ├── 99.jpg
│   │   │           └── sincerely-media-CXYPfveiuis-unsplash_DMT2mBf.jpg
│   │   │       
│   │   └── post_images
│   │       └── Screenshot_from_2020-12-10_16-00-47.png
│   ├── profile
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_friendrequest.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── signals.py
│   │   ├── tests.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── requirements.txt
│   └── templates
│       ├── base.html
│       ├── feed
│       │   ├── create_post.html
│       │   ├── home.html
│       │   ├── post_detail.html
│       │   └── user_posts.html
│       ├── registration
│       │   ├── edit_profile.html
│       │   ├── friend_list.html
│       │   ├── logged_out.html
│       │   ├── login.html
│       │   ├── password_change_done.html
│       │   ├── password_change_form.html
│       │   ├── password_reset_complete.html
│       │   ├── password_reset_confirm.html
│       │   ├── password_reset_done.html
│       │   ├── password_reset_email.html
│       │   ├── password_reset_form.html
│       │   ├── profile1.html
│       │   ├── search_users.html
│       │   ├── signup.html
│       │   └── users_list.html
│       └── welcome.html
├── LICENSE
└── README.md


```
# Running Locally

Firstly, create virtual environment and create a django project then clone the repository to your local machine:

```
git clone https://github.com/Praful-Rathore-222/socailweb.git

cd socialweb
```

Install the requirements:

```
pip install -r requirements.txt
```
Apply the database migrations:

```
python manage.py migrate
```

Load the initial data:
``
Create administrator/super user:
```
python manage.py createsuperuser 

```

Finally, run the development server:

```
python manage.py runserver
```

Note- The site will be available at 127.0.0.1:8000. `
