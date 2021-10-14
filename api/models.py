from django.db import models

# Create your models here.

class Note(models.Model):
    body = models.TextField(null = True, blank = True)
    updated = models.DateTimeField(auto_now = True) # Auto_now automatically saves current time
    created = models.DateTimeField(auto_now_add = True) # Auto_now_add takes first creation time

    def __str__(self):
        return self.body[0:50]   # Retrieve first 50 char
    
    class Meta():
        ordering = ['-updated']

    