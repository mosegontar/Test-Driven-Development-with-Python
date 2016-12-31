Provisioning a new site
=======================

## Required packages:

* nginx
* Python
* Git
* pip
* virtualenv

## On Ubuntu:
    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* See nginx.template.conf
* replace SITENAME & USER with proper address and user

## Upstart Job

* See gunicorn-upstart.template.conf
* replace SITENAME & USER

## Folder Structure:
### Assume we have a user account at /home/USER
    
    /home/username
    |——sites
        |——SITENAME
            |——database
            |——source
            |——static
            |——virtualenv

