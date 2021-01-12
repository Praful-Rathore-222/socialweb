from django.contrib import admin
from .models import Post

from .models import Comments

# Register your models here.
class CommentsInline(admin.StackedInline):
    model = Comments
    extra = 3


class PostA(admin.ModelAdmin):
    list_display = ("description", "date_posted")
    search_fields = ["description"]
    inlines = [CommentsInline]
    # class meta :
    #     model = Posts


admin.site.register(Post, PostA)

admin.site.register(Comments)
