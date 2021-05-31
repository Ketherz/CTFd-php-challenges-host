# CTFd-php-challenges-host

This little project aim to give an easy upload of php challenges in CTFd. A docker with apache2 run in background and store the files.
But, take care, no challenges that lead to a docker takeover should be added it's designed to just add challenges that do not need machine full take-over of the machine like login bypass xss or that kind of stuff.

## Installation :

Start by downloading the docker image that will be the base for the webserver challenge hosting

```bash

docker pull ketherz/base_apache2_php

```
Then copy the php_challenges folder in the plugin folder of CTFd. That it.

## Usage :

When you go to add challenge, you will se a challenge named php. 

![image](https://user-images.githubusercontent.com/1362237/114372227-981c2580-9b81-11eb-8656-dbc3c4f3d356.png)

The creator is quite the same, but you can add a zip folder containing the php challenge inside for exemple this kind of file tree :



```
challenge.zip
|
|-_challenge
  |
  |-helloworld.php
  |-style.css
  |-flag.php
```


After the regeneration of the docker container, you can access your challenge at the address http://:4001/challenges/challenge/helloworld.php for exemple. 

Hope it will be usefull, thanks for using the plugin.

