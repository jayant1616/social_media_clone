from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null =True,related_name='profile_user')
    portfolio_site = models.URLField(null =True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True,default='/media/profile_pics/default.png')

class friends(models.Model):
    tag = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    #name=models.CharField(max_length=240,default='def')
    following=models.ManyToManyField(User,related_name='followers')

class Posts(models.Model):
    for_user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_post= models.CharField(max_length=240,default='Tell People about your day...')
    #pos0t_image = models.ImageField(upload_to='')
class Comments(models.Model):
    for_comment = models.ForeignKey(Posts,on_delete=models.CASCADE)
    user_comment = models.CharField(max_length=64,default='comment something')
    user = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE,null ='True')
