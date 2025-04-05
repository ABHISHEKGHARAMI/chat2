from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


# user profile
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/',default='avatars/default.png')
    bio = models.TextField(max_length=500,blank=True)
    online_status = models.BooleanField(default=False)
    last_active = models.DateTimeField(null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
    
# automatically creates the user profile when user is created
@receiver(post_save, sender = User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


# save the created user in the db
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
