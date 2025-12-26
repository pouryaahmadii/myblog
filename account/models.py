from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='profile_pics/111.png', upload_to='profile_pics')

    def __str__(self):
        return self.user.username