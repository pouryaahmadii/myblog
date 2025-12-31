from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='profile_pics/111.png', upload_to='profile_pics')
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=500,blank=True)
    phone = models.CharField(max_length=11, blank=True)
    birth = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.user.username