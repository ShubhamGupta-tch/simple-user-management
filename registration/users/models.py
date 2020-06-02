from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib import messages
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', default='avatar.svg')

    def __str__(self):
        return self.user.username + " Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # img = Image.open(self.image.path)
        # if img.height > 300 or img.width > 300:
        #     output = (450, 450)
        #     img.thumbnail(output)
        #     img.save(self.image.path)

def create_profile(sender, instance, **kwargs):
    u = User.objects.get(username=f"{instance.username}")
    try:
        p = Profile.objects.get(user=instance)
    except:
        p = Profile(user=u)
        p.save()
        print(f"{p.user.username} Profile Created.")

post_save.connect(create_profile, sender=User)
