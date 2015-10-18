# notify-me

This program runs a program and notify you by SMTP email, Android push notification and/or internal notification server.

The internal notification sever can be checked on Ubuntu to get genome notification and Mac OS X to get a notification.


## Installation of notification checker 

### Mac OS X

sudo gem install terminal-notifier


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
