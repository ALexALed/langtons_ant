# Overview
https://en.wikipedia.org/wiki/Langton%27s_ant

# How to run
`pipenv install` - install dependencies 

`pipenv run python ./main.py` - run CLI application

`pipenv run python -m pytest tests/` - run tests

# Notes
Added only unit and functional tests
Didn't provide test for CLI app, just for avoid unnecessary complexity
It will be better to use separate `Point` class to represent `[x, y]` point
Code formatted by black