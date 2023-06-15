# Overview

<!-- {Important! Do not say in this section that this is college assignment. Talk about what you are trying to accomplish as a software engineer to further your learning.} -->

This software was built as a demo database for housing software. The goal with this project was to utilize a SQL relational database using the sqlite3 library in Python. The software is currently setup to be interacted with via a tkinter GUI. The goal is to move this to be interacted with on a web application. To run the software the user will run the app.py file and it should pull up a GUI with several button options. On the left will be a list of leases that can be clicked to view the resident and their lease details. From there you can edit their resident information such as name, email, phone, birthdate. These changes are saved and dynamically updated in the interface. Below this are three buttons to see different reports- rent roll, rent total, and capacity. These each take two date arguments and then return the results with lease start dates within the given date range. More details can be found within the software demo.

<!-- {Provide a description of the software that you wrote and how it integrates with a SQL Relational Database. Describe how to use your program.} -->

Activate environment venv\Scripts\activate
Run Server python manage.py runserver

<!-- {Describe your purpose for writing this software.} -->

<!-- {Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.} -->

[Software Demo Video](https://youtu.be/wWYcYWwYlhw)

# Relational Database

<!-- {Describe the relational database you are using.} -->

This is a SQL Relational Database, which means that the database consists of several tables that are related by the different columns they have. For example, in this database software there currently exists 4 tables: tb_resident_info, tb_housing_complexes, tb_student_housing_units, and tb_leases. All tables store data related to a fictitious student housing company.

<!-- {Describe the structure (tables) of the relational database that you created.} -->

# Development Environment

<!-- {Describe the tools that you used to develop the software} -->

To develop the software specifically related to direct interaction with the database I used the following libraries in python: sqlite3, datetime, and csv. The main library would be sqlite3, which is a C library that allows the developer to create a serverless database. This is useful for this software as I am not looking to create a database that needs to necessarily be shared and is quick for development purposes like this. Another tool I used for this project was Mockaroo. This helped me quickly create mock data to use for my database.

<!-- {Describe the programming language that you used and any libraries.} -->

# Useful Websites

<!-- {Make a list of websites that you found helpful in this project} -->

- [Codemy - SQLite Databases with Python Tutorial](https://www.youtube.com/watch?v=byHcYRpMgI4)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [SQL - W3 Schools](https://www.w3schools.com/sql/)
- [Python sqlite3 Docs](https://docs.python.org/3.8/library/sqlite3.html)
- [Full-stack Web App with Python](https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb)
- [Mockaroo](https://www.mockaroo.com/)
- [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/documentation/)
- [What to do to import files from different folder in Python?](https://pythonhow.com/what/what-to-do-to-import-files-from-different-folder-in-python/)
- [Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)
- [Multiple Databases for Django](https://www.protechtraining.com/blog/post/tutorial-using-djangos-multiple-database-support-477)
- [Database Routers Django Projects](https://docs.djangoproject.com/en/dev/topics/db/multi-db/#automatic-database-routing)
- [Digital Ocean Backend with Django](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)
- [Django Projects Docs](https://docs.djangoproject.com/)
- [Modelviewset Django Rest Framework](https://ilovedjango.com/django/rest-api-framework/views/tips/sub/modelviewset-django-rest-framework/)
- [Django Rest Framework](https://www.django-rest-framework.org/api-guide/)
- [Query Params with Django](https://pythoncircle.com/post/710/getting-query-params-from-request-in-django/)

# Future Work

<!-- {Make a list of things that you need to fix, improve, and add in the future.} -->

- Add Web Application Interface
  A database exists to store things, so its not really meant to be on its own. I want to create a front-end for this software that models what one might actually see when using a student housing software.
- Add additional SQL queries
  As I create a web interface, I would also like to add additional queries that will help improve the type of data that is received on the front-end.
- Improve how changes are made to the database
  Currently there is one init_db.py file that creates the tables for the database, however I would like to improve how future tables may be added to better track the growth/changes to the database itself and not just the software the create the SQL queries.
