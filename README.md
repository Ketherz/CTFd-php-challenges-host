# CTFd-Upload-php-and-update-dockerfile

This little project aim to give an easy upload of php challenges in CTFd. A docker with apache2 run in background and store the files.
But, take care, no challenges that lead to a docker takeover should be added it's desined to just add challenges that do not need machine compromission like login bypass xss or that kind of stuff.

## Installation :

Start by downloading the docker image that will be the base for the webserver challenge hosting

```bash

docker pull ketherz/base_apache2_php

```
Then copy the php_challenges folder in the plugin folder of CTFd. That it.

## Usage :
