# AccuKnox_Dhanbd
# AccuKnox_Assignment
# Social Networking API
Create an API for social networking application using Django Rest Framework with
below functionalities.
Constraints
• Use any database of your choice
• You are free to design Request/Response fields/formats
User Login/Signup
• Users should be able to login with their email and password(email should be case
insensitive)
• User should be able to signup with their email only(no otp verification required, valid
email format is sufficient)
• Except signup and login every api should be called for authenticated users only
1
Develop API for following functionalities:
• API to search other users by email and name(paginate up to 10 records per page).
a) If search keyword matches exact email then return user associated with the
email.
b) If the search keyword contains any part of the name then return a list of all
users.
eg:- Amarendra, Amar, aman, Abhirama are three users and if users search with "am"
then all of these users should be shown in the search result because "am"
substring is part of all of these names.
c) There will be only one search keyword that will search either by name or email.
• API to send/accept/reject friend request
• API to list friends(list of users who have accepted friend request)
• List pending friend requests(received friend request)
• Users can not send more than 3 friend requests within a minute.


## How to Download a Project and **Clone the Repository**
You can clone this project using git
   git clone https://github.com/khushboo-hub/AccuKnox_Dhanbd
   cd your-repository 
   
## Installation Steps
1.Create a Virtual Environment
   python -m venv env 
2.Activate the Virtual Environment
   env\Scripts\activate 
3.Install the Dependencies
   pip install -r requirements.txt 
4.Apply Database Migrations
   python manage.py migrate 
5.Create a Superuser (Optional)
   python manage.py createsuperuser 
6.Run the Development Server
   python manage.py runserver
   Access the API
7.sql Install
create database in PHPadmin and import the file ''myapp_customuser.sql'' into phpmyadmin for the structure of project data. `
You might have some problem installing mysqlclient. To solve this problem you need to download
the wheel for the above from 
[Download Mysql Client](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)
You need to download a client with respect to the python version you are using.


### How to install downloaded mysqlclient

    pip install  <absolute path to your downloaded mysqlclient>

##API Endpoints:
Base URL: `http://127.0.0.1:8000/api/`
POST /api/signup/ - User registration
POST /api/login/ - User login
GET /api/search/ - Search for users
POST /api/friend-request/send/ - Send a friend request
POST /api/friend-request/accept/<request_id>/ - Accept a friend request
POST /api/friend-request/reject/<request_id>/ - Reject a friend request
GET /api/friends/ - List friends
GET /api/pending-requests/ - List pending friend requests
###Postman Collection
Open Postman and create a new collection.
Add each API endpoint to the collection with the relevant HTTP method, URL, request body, and headers.
Click on the collection name in Postman.
Click on the three dots (more options) and select Export.
Choose the format (e.g., Collection v2.1 (recommended)).
Save the file (e.g., myprojectAPI.postman_collection.json).
You  can see "MyprojectAPi.postman_collection.json "  added in this project directory.

##Requirements
Python 3.8 or higher
Django 4.2 or higher
Django REST Framework
MySQL
