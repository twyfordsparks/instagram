# Instagram

## 21 May 2019

## By John Victor Njoroge Karanja

## Description

Instgram is a clone application to the popular photo sharing application, Instagram. It's a version similar to but not the same as the original application. It's my version of Instagram and its simple design delivers quite well. Gram has a layout that mimics the original application, and its functionality is the same. A new user needs to sign up to the application and then successfully login. One can then create a profile and start sharing his/her photo experiences.
A user can follow another user of interest, like their photos and even comment on them.
A user can upload his/her photos and view them in his/her created profile.

## User Stories

1. A user can sign in to the application and start using it.

2. A user can upload his/her pictures to the application.

3. A user can  see his/her profile with all his/her posted pictures.

4. A user can follow other users and see their pictures in his/her profile.
5. A user can like a picture and leave a comment.

## Behaviour Driven Development(BDD)

| Behaviour                                                | Input                                   | Output                                                                                       |
|----------------------------------------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------|
| The Page loads the homepage                              | On application load                     | User views the sign up/login page                                                            |
| User is redirected to the index page                     | User successfully registers and logs in | Images of all users are displayed with the profile name,like & comment                       |
| User is redirected to the specific profile page          | User clicks on profile icon             | A page with all the details about a specific user is displayed including all their posts     |
| User redirected to a page with a form to enable the post | User clicks on create post button       | A template with a form is rendered. The user fills in all the details including image upload |
| User redirected to the edit profile page|User Clicks on the Edit Profile Button|User fills in the appropriate fields and saves that information and is redirected to the homepage|

## Technologies Used

1. Python 3.6
2. HTML and CSS
3. Django
4. Postgres
5. Heroku for deployment

## Set up and Installation

To access this application on your command line, you need to clone it.
`git clone https://github.com/twyfordsparks/instagram.git`

### Prerequisites

A user will require git, Django, postgresql and python3.6+ installed in their machine.
To install these two, you can use the following commands

 #git
    $ sudo apt install git-all
 #python3.6
    $ sudo apt-get install python3.6.
 #django
    $ pip install django==1.11
 #postgres
    $ sudo apt-get install postgresql postgresql-contrib libpq-dev

## Known Bugs

There are no issues or bugs encountered yet while coming up with the programme but incase of anything,feel free to contact the devoloper through johnvictor0002@gmail.com.

## Support and contact details

Incase you want to use the programme and you dont know where to start or what to do,feel free to contact the developer and be sure to receive help as much as you would need.You can do so through johnvictor0002@gmail.com.

## License

*MIT LISENCE.Feel free to use the code in anyway to improve it.
Copyright (c) 2019 John Victor Njoroge Karanja.