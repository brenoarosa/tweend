# Tweet Classifier Endpoint

Stores classified and unclassified tweets.

### Setting up environment

~~~~
mkvirtualenv [venv-name] -p python3
pip install pip --upgrade
pip install -r requirements.txt
~~~~

[**Working with virtualenvs**](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

### Django Configs

A custom setting system based on http://justcramer.com/2011/01/13/settings-in-django/ [(Archived version)](http://web.archive.org/web/20160326133259/http://cramer.io/2011/01/13/settings-in-django)  
This enable us to easily maintain multiple environments (e.g.: dev, stage, production, etc)  
Environments can set by env var: DJANGO_DEPLOY_ENV (e.g.: `export DJANGO_DEPLOY_ENV=prod` will load prod.py)

All configurations will be loaded from siteconfig/{env}.py heavely inheriting from siteconfig/defaults.py

### Starting project
