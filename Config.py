import sys,ConfigParser,os

config = ConfigParser.RawConfigParser()
if os.path.exists(os.path.expanduser("~/.notify-me.cfg")):
		config.read(os.path.expanduser("~/.notify-me.cfg"))
elif os.path.exists("/etc/notify-me.cfg"):
    config.read("/etc/notify-me.cfg")
else:
    raise Exception("No config file found, put the configuration in /etc/notify-me.cfg or ~/.notify-me.cfg")

notification_key = config.get("Notification-Key","key")
default_topic=config.get("Notification-Key","default-topic")

smtp_host = config.get("SMTP","SMTP-HOST")
smtp_port = config.get("SMTP","SMTP-PORT")
smtp_user= config.get("SMTP","SMTP-User")
smtp_pass= config.get("SMTP","SMTP-PASS")
default_from=config.get("EMAIL","DEFAULT-FROM")
default_subject=config.get("EMAIL","DEFAULT-SUBJECT")
OK_MESSAGE=config.get("EMAIL","OK-MESSAGE")
ERR_MESSAGE=config.get("EMAIL","ERR-MESSAGE")

