from django.db import models
from django.contrib.auth.models import User

# "One-To-One" modela una relación de uno a uno.
# "ForeignKey" modela una relación de uno a muchos.
# "ManyToMany" modela una relación de muchos a muchos.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  
    biography = models.TextField(null=True, blank=True, max_length=255)
    avatar = models.ImageField(null=True, blank=True, upload_to='images/profile/')

    def __str__(self):
        return str(self.user)