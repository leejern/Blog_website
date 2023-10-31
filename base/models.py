from django.db import models
from datetime import datetime

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True, )

    

    def __str__(self):
        return self.name
