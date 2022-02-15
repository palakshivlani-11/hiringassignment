from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
# Create your models here.


Food_choices=(
    ('vegetarian','vegetarian'),
    ('Fruit','Fruit'),
    ('Unknown','Unknown'),
)

class Kid(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    parentphone = PhoneNumberField(null=False, blank=False, unique=True)
    parentemail = models.EmailField()

    def __str__(self):
        return self.name

class Image(models.Model):
    kid = models.ForeignKey(Kid,on_delete=models.CASCADE)
    imgurl = models.URLField()
    group = models.CharField(max_length=100,choices=Food_choices)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_approved = models.BooleanField(default=False)
    approved_by = models.CharField(max_length=100)


# @receiver(post_save, sender=Image)
# def send_mail_to_user(sender, instance, created, **kwargs):
#     if instance.group == 'Unknown':
#         subject = "Important Notification"
#         to_email = instance.kid.parentemail
#         text = "Hey! Dear parent, Image uploaded by your child " + instance.kid.name + " does not contain food."
#         message = EmailMessage(subject, text,'shivlanipalak@gmail.com', [to_email])
#         message.send()