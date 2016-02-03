# PyBankID Example Web Application

**Version 1.1.0**

Simple example web application showing how [pybankid](https://github.com/hbldh/pybankid)
can be used for web applications.

A running instance of it can be found at 
[https://bankid-example-app.herokuapp.com/](https://bankid-example-app.herokuapp.com/).

## What is this repository for?

This web application originated as a learning tool for testing how to build a 
BankID-powered application. It serves as simple example of how authentication and 
signing with BankID can be implemented on a web application, to allow for signing
with a BankID application on desktop, on mobile or on other device than the one
the application is accessed on. See the
[Notes on Launching the BankID app from a browser](#notes-on-launching-the-bankid-app-from-a-browser)
section below for more details.

It is prepared for being deployed on [Heroku](https://www.heroku.com), but it can be
run as a standalone Flask application as well.

## How do I get set up?

### Standalone Flask application

First, clone this repo and install the requirements:
    
    pip install -r requirements.txt

Then run

    python run.py

in the root folder of the repo to start up a development server on 
[http://127.0.0.1:5000](http://127.0.0.1:5000).

### On Heroku

Read [Heroku's Flask deployment guide](https://devcenter.heroku.com/articles/getting-started-with-python-o#deploy-your-application-to-heroku) to learn how to deploy this application there.


## Notes on Launching the BankID app from a browser
 
In the [official documentation](https://www.bankid.com/assets/bankid/rp/bankid-relying-party-guidelines-v2.9.pdf) 
regarding BankID, one section is titled **Launching the BankID app from a browser** and discusses differences
between different operating systems and browsers. The main part of this application came into being to have a 
simple and transparent means of testing different solutions for handling the `redirect=` option of the URL 
for starting the BankID application on a device.

Version 2.9 of the BankID documentation states "**The general recommendation is to use 
`redirect=null` when it is possible.**" This application does exactly that, and displays the behaviour of
such a setup. Below are described how different operating systems respond to this.

### Browsers

#### Chrome

TBD.

#### Firefox

TBD.

#### Internet Explorer

TBD.

#### Edge

TBD.

### Mobile device operating systems

#### iOS

Using `redirect=null` on iOS results in a correct opening of the BankID app, but never closes it after signing
is complete. On iOS > 9.0, a "Back to *BrowserName*"-option is present in the top left corner of the screen, but on 
earlier versions one is left with the only opportunity to reopen the used browser manually.
 
#### Android

TBD.

#### Windows Phone

TBD.
