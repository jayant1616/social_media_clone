from django.contrib import admin
from basicapp.models import profile,friends,Comments,Posts
#from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(friends)
admin.site.register(profile)
