# Python on Replit

This is a template to get you started with Python on Replit. It's ready to go so you can just hit run and start coding!

# Schedule planner web app

 - the purpose is to automate dayli dutty schedule plan for group of persons
 - export planned dates to Excel file (named table Excel)
 - add abylity to rearange duties
 - add statistics 
 - add highlight to preview by date and person
 - eport as Google or Outlook calendar .ics file to be able import 
 - add summary notification as telegram bot message ( q: who? (who is dutty today); answ: list of persons and their role)

![Application web site preview](/static/Readme/Preview.png "Preview")


# ABOUT

this it my pet project to get use to Django framework and python itself.

## how to start

   - pip install --requirement requirements.txt
   - python manage.py migrate
   - python manage.py runserver

or try to reuse REPL.it~

## USAGE FLOW

it should be quite simple, as far as plan to reuse REPL.it hosting for demo.
1. created REPL.it repostory
2. publish source code to github public repository
3. import github to local (Windows Subsytem Linux + VScode for Pytho)
4. commit changes, push to Github, fetch or pull to REPL.it for online [preview](https://locallibrary-4.tarashalaka.repl.co/monthlyschedule/)

the way it was done like this - I could not won fight with REPL.it when try to import Django project published on github, so I exported Django ready repl.it templete to be able run it in REPL.it WEB hosting.

VSCOde extention to work directly with REPL.it was not tested by me, may be this will be much easier.

## Running the repl

1. Setup a new secret environment variable (the lock icon) where the key is `SECRET_KEY` and the value is
   a randomly generated token of 32 bits of randomnese. To generate such a token type this into the shell and hit Enter:
```
python
import secrets
secrets.token_urlsafe(32)
```
2. Hit run!

See this 1 minute video for a walkthrough: [https://www.loom.com/share/ecc4e738149f4d1db3bcff01758b3e71](https://www.loom.com/share/341b5574d12040fb9fcbbff150777f1c)

## Installing packages

To add packages to your repl, you can just import directly in the file you want to use the package in, and it will automatically be installed when you press the run button. Like below:
```python
import math
import pandas as pd
```

You could also install packages by using the Replit packager interface in the left sidebar.

## Help

If you need help you might be able to find an answer on our [docs](https://docs.replit.com) page. Feel free to report bugs and give us feedback [here](https://replit.com/support).