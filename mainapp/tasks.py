from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .models import *
import requests
import json
from django.shortcuts import render
from django.template.loader import render_to_string 
from django.core.mail import EmailMessage




def send_notification(name,mail):
    subject = "Important Notification"
    to_email = mail
    text = "Hey! Dear parent, Image uploaded by your child " + name + " does not contain food."
    message = EmailMessage(subject, text,'your mail id', [to_email])
    message.send()


@periodic_task(run_every=crontab(minute='*/1', day_of_week="*"))
def sendmail():
    obj = Image.objects.filter(is_approved=False)
    for i in obj:
        if i.group == 'Unknown':
            child = i.kid.name
            mailid = i.kid.parentemail
            send_notification(child,mailid)
        i.is_approved=True
        i.save()
    
