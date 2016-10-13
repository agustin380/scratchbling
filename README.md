# Scratchbling

Web app for a back scratcher shop.


### How to run

```./src/manage.py runserver``` runs the development server on port 8000 by default.```


## How to use

```POST /api/login``` with a ```username``` and ```password``` to get an authorization token.
This token must be included in the ```Authorization``` header of all subsequent requests,
in the following format: ```JWT {token}```.

```GET /api/products``` returns a list of all back scratchers.

```GET /api/products/{id}``` returns the back scratcher with id ```id```.

```POST /api/products``` creates a new back scratcher.

```PATCH /api/products/{id}``` updates the back scratcher with id ```id```.
