from django.contrib import admin
from .models import Profile
from .models import FriendRequest

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "image", "bio", "email", "created"]
    list_filter = ["first_name", "last_name", "email", "created"]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(FriendRequest)
