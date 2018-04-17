# sqlalchemy-pagination

[![Build Status](https://travis-ci.org/wizeline/sqlalchemy-pagination.svg)](https://travis-ci.org/wizeline/sqlalchemy-pagination)


## Contents

1. [About](#about)
2. [Install](#install)
3. [Usage](#usage)
4. [Hacking](#hacking)
    1. [Setup](#setup)
    2. [Testing](#testing)
    3. [Coding conventions](#coding-conventions)


## About

A small utility to paginate SqlAlchemy queries..


## Install

Just do:

```
$ pip install git+ssh://git@github.com/wizeline/sqlalchemy-pagination.git
```

## Usage

Just import the paginate method and call it with the query, the current page and the page size

```
from sqlalchemy_pagination import paginate

page = paginate(session.query(User), 1, 25)
```

The pagination objects has the following attributes

* `items`: The items of the current page base on the query
* `total`: Total number of items
* `pages`: Total number of pages
* `has_next`: Boolean indication wether there are more pages to fetch
* `has_previous`: Boolean indicating wether there are previous pages
* `next_page`: Next page number or None if the current page is the last one
* `previous_page`: Previous page number or None if the current page is the last one

## Hacking

### Setup

First install Python 3 from [Homebrew](http://brew.sh/) and virtualenvwrapper:

```
brew install python3
pip3 install virtualenv virtualenvwrapper
```

After installing virtualenvwrapper please add the following line to your shell startup file (e.g. ~/.zshrc):

```
source /usr/local/bin/virtualenvwrapper.sh
```

Then reset your terminal.

Clone this respository and create the virtual environment:

```
$ git clone https://github.com/wizeline/sqlalchemy-pagination
$ cd sqlalchemy-pagination
$ mkvirtualenv -p python3 sqlalchemy-pagination
$ workon sqlalchemy-pagination
$ pip install -r requirements-dev.txt
$ pip install tox
```


### Testing

To run the tests, you just do:

```
$ tox
```


### Coding conventions

We use `editorconfig` to define our coding style. Please [add editorconfig](http://editorconfig.org/#download)
to your editor of choice.

When running `tox` linting will also be run along with the tests. You can also run linting only by doing:

```
$ tox -e flake8
```
