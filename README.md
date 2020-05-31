# Python Pagination


Supported CSS: `bootstrap2&3&4`, `foundation`, `semanticui`, `ink`, `uikit` and `metro4`

Supported web frameworks: Flask, Tornado and Sanic

```
Note:
I have used CSVKIT to import csv to postgresql DB
Check db.sh file for this
Setup.py is not currently configured we can use it to create commands to perform functions. Ex. $python setup.py init-db or
$python setup.py fill-populate-data
```

## Installation

`pip install python-paginate`
`pip install csvkit`

## Usage

see examples and source code for details.

Create DB:

    Run Bash File
    Configure Bash according to your db configuration
    Check If Date, Season, FT are capital rename to small else it will give error for query
    After Successful Completion of Importing DB Run Application

Run Application:

    $cd example
    $virtualenv venv
    $. venv/bin/activate
    $pip install -r requirements.txt
    $python myapp.py

Open <http://localhost:8000> to see the Home page.

## Screenshots

![Desktop](/ss/ss.jpg "Desktop")
![Mobile](/ss/ss-mobile.jpg "Mobile")

If Any Error Arises Feel Free To Contact Me
Hope its close to expected solution