# PyBankID Example Web Application

**Version 1.0.0**

Simple example web application showing how [pybankid](https://github.com/hbldh/pybankid)
can be used for web applications.

A running instance of it can be found at 
[https://bankid-example-app.herokuapp.com/](https://bankid-example-app.herokuapp.com/).

### What is this repository for?

This web application originated as a learning tool for testing how to build a 
BankID-powered application. It serves as simple example of how authentication and 
signing with BankID can be implemented on a web application, to allow for signing
with a BankID application on desktop, on mobile or on other device than the one
the application is accessed on.

It is prepared for being deployed on [Heroku](https://www.heroku.com), but it can be
run as a standalone Flask application as well.

### How do I get set up? ###

#### Standalone Flask application

First, clone this repo and install the requirements:
    
    pip install -r requirements.txt

Then run

    python run.py

in the root folder of the repo to start up a development server on 
[http://127.0.0.1:5000](http://127.0.0.1:5000).

#### On Heroku

Read [Heroku's Flask deployment guide](https://devcenter.heroku.com/articles/getting-started-with-python-o#deploy-your-application-to-heroku) to learn how to deploy this application there.

