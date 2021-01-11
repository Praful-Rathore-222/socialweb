from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    description = models.CharField(max_length=255, blank=True)
    pic = models.ImageField(upload_to="path/to/img", blank=True)
    video = models.FileField(upload_to="videos/", blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user_name = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes")

    def __str__(self):
        return self.description

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="details", on_delete=models.CASCADE)
    username = models.ForeignKey(User, related_name="details", on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(default=timezone.now)
