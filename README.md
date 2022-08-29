# To-Do API

This is a basic To-Do App API developed in Flask.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and manual testing purposes. 

### Prerequisites

Requirements for the software and other tools to build, test and push 
- Python3.8

### Installing

A step by step series of examples that tell you how to get a development
environment running

If you are using Windows:
```
$ . venv/Scripts/activate
$ flask run
```

If you are using Linux:
```
$ source venv/bin/activate
$ flask run
```

## Routing

### GET /todos
This route will return all To-Do registered in our database.

### POST /todos
Use this route to register a new task. You will need to send a JSON body with:

```
{
  "title": str
}
```


## Built With

  - Python3.8
  - Flask
  - SQLite3

