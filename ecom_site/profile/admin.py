from django.contrib import admin
from .models import Profile
from .models import FriendRequest
# Register your models here.
admin.site.register(Profile)
admin.site.register(FriendRequest)

