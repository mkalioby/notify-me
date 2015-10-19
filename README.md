# notify-me

This program runs a program and notify you by SMTP email, Android push notification through [pushNotification](https://github.com/mkalioby/Python_Notifications) and/or internal notification server.

The internal notification server can be checked on Ubuntu/gnome, KDE or Mac OS X to get a notification, just choose the appropiate client from client folder.

iOS, Browsers and many other application are supported over [pushOver](https://pushover.net/). PushOver is a service where the user buy a one-time license for each platform.


## Installation of notification checker 

### Mac OS X

sudo gem install terminal-notifier

### Ubuntu/gnome
sudo pip install gi

## Options


 notify-me OPTIONS Command

 Options

    --notify-to=mail1,mail2    send an email when done to the following mails
    --notify-push              send a push notification
    --notify-OK=               send this message after success
    --notify-ERR=              send this message after failure
    --notify-topic=            the topic to send on if different than default queue
    --notify-name=             name of the job, to put it subject or push notifications
    --no-notify-send-out       don't send the stderr and stdout in the email.
    
 
 
 **Example**

 notify-me  --notify-to=someone@example.com,someone2@example.com --notify-push --notify-OK="System Updated" --notify-ERR="System Update Failed" --notify-name="System Update" --notify-topic="Admin" sudo apt-get upgrade

# Requirements

This is based on [pushNotification library](https://pypi.python.org/pypi?name=pushNotification), available on pip

# Installation

```sh
pip install pushNotification notify-me
```

# Configuration

You can configure the SMTP and push notification through /etc/notiy-me.cfg or ~/.notify-me.cfg

# Internal Notification Server Installation

Currently the server supports MySQL database as the back-end db. the server needs mod_python to work.

* Install Packages
```sh
$ sudo apt-get install libapache2-mod-python python-simplejson python-mysqldb
```
* Copy server code
```sh
	$ sudo cp SRC/server /var/www/notify
```
* Configure Apache in 000-default
```xml
	<Directory /var/www/notify/py>
         	SetHandler mod_python
                PythonHandler mod_python.publisher
        </Directory>
```

* Reload Apache
  
  ```sh 
 $ sudo service apache2 reload
 ```
 
* Configure Server, Edit the configuration in /var/www/notify/config.cfg
     



