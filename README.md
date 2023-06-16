# Overview

<!-- {Important! Do not say in this section that this is college assignment. Talk about what you are trying to accomplish as a software engineer to further your learning.} -->

This software was built as a demo database and backend for housing software. The goal with this project was to utilize a SQL relational database using the sqlite3 library in Python. There is a simple script that can be ran to interact on a minimal level with the databse via a Tkinter GUI. The goal is to move this to be interacted with on a web application. This can be done by running
`python app.py` in the main directory. This should pull up a GUI with several button options. On the left will be a list of leases that can be clicked to view the resident and their lease details. From there you can edit their resident information such as name, email, phone, birthdate. These changes are saved and dynamically updated in the interface. Below this are three buttons to see different reports- rent roll, rent total, and capacity. These each take two date arguments and then return the results with lease start dates within the given date range. More details can be found within the following [demo video](https://youtu.be/wWYcYWwYlhw).

This backend API was built using the Django python framework. After some research I found that Django was more commonly used for building the backend of sites, and wanted to give that more focus on this side of the project. The sqlite database built previously was integrated into the housingapi which holds all of the models for the tables, as well as the routes for accessing the api. The admin route is still intact and the database can be interacted with via that after a user with permissions is made.

To run the application as the backend for the [Housing Software Application](https://github.com/Myapi314/StudentHousingWebApp) you will need to make sure you are in the development environment with the following command:

`venv\Scripts\activate`

After that go into the myhousingsite directory and run the following:

`python manage.py runserver`

<!-- {Describe your purpose for writing this software.} -->

<!-- {Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.} -->

[Software Demo Video]()

# Relational Database

<!-- {Describe the relational database you are using.} -->

This is a SQL Relational Database, which means that the database consists of several tables that are related by the different columns they have. For example, in this database software there currently exists 4 tables: tb_resident_info, tb_housing_complexes, tb_student_housing_units, and tb_leases. All tables store data related to a fictitious student housing company.

<!-- {Describe the structure (tables) of the relational database that you created.} -->

# Backend API

The project has several endpoints that can be accessed, including the ability to get all records from each of the 4 tables in the database. There is also a url that takes in a couple of query parameters that is utilized by the frontend application. The models represent the data coming out of the database and allow us to utilize the Django ORM. The views are basically the queries we create and I utilized several imports from the Django rest-framework library to build these. The serializers take the views we created and parse it into the data we send from the database.

# Development Environment

<!-- {Describe the tools that you used to develop the software} -->

To develop the software specifically related to direct interaction with the database I used the following libraries in python: sqlite3, datetime, and csv. The main library would be sqlite3, which is a C library that allows the developer to create a serverless database. This is useful for this software as I am not looking to create a database that needs to necessarily be shared and is quick for development purposes like this. Another tool I used for this project was Mockaroo. This helped me quickly create mock data to use for my database.

To develop the REST API framework I used the Django rest_framework library as well as venv for my development environment.

<!-- {Describe the programming language that you used and any libraries.} -->

# Useful Websites

<!-- {Make a list of websites that you found helpful in this project} -->

### SQL and SQLite

- [Codemy - SQLite Databases with Python Tutorial](https://www.youtube.com/watch?v=byHcYRpMgI4)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [SQL - W3 Schools](https://www.w3schools.com/sql/)
- [Python sqlite3 Docs](https://docs.python.org/3.8/library/sqlite3.html)

### Backend with Django

- [Full-stack Web App with Python](https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb)
- [Multiple Databases for Django](https://www.protechtraining.com/blog/post/tutorial-using-djangos-multiple-database-support-477)
- [Database Routers Django Projects](https://docs.djangoproject.com/en/dev/topics/db/multi-db/#automatic-database-routing)
- [Digital Ocean Backend with Django](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)
- [Django Projects Docs](https://docs.djangoproject.com/)
- [Modelviewset Django Rest Framework](https://ilovedjango.com/django/rest-api-framework/views/tips/sub/modelviewset-django-rest-framework/)
- [Django Rest Framework](https://www.django-rest-framework.org/api-guide/)
- [Query Params with Django](https://pythoncircle.com/post/710/getting-query-params-from-request-in-django/)
- [Real Python - Django Tutorial](https://realpython.com/get-started-with-django-1/)
- [Programming with Mosh Django Tutorial](https://www.youtube.com/watch?v=rHux0gMZ3Eg)

### Additional

- [Mockaroo](https://www.mockaroo.com/)
- [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/documentation/)
- [What to do to import files from different folder in Python?](https://pythonhow.com/what/what-to-do-to-import-files-from-different-folder-in-python/)
- [Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

# Future Work

<!-- {Make a list of things that you need to fix, improve, and add in the future.} -->

- Add additional SQL queries

  As I continue to develop the web interface, I would also like to add additional queries that will help improve the type of data that is received on the front-end. I also want to research further into more complex queries using the Django ORM. It seems like it can do a lot, but is limited in complexity when it comes to joining tables.

- Improve how changes are made to the database

  Currently there is one init_db.py file that creates the tables for the database, however I would like to improve how future tables may be added to better track the growth/changes to the database itself and not just the software the create the SQL queries. I've seen the Django migrations and that may be a good way to go about future changes.

- Understand views/viewsets

  Since I utilized the Django rest framework, I ended up using the parent classes that it provides, but I wasn't able to fully grasp what it was doing/accomplishing and I would like to better understand and learn how to be effective and efficient with using those.
