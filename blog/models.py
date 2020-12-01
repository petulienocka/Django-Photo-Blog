from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from socialmedia.models import Socialmedia, SocialmediaManager
from django.contrib.contenttypes.models import ContentType


def upload_location(instance, filename):
    return '%s/%s' % (instance.id, filename)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              height_field="height_field",
                              width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("photo_detail", kwargs={"id": self.id})


@property
def socialmedia(self):
    instance = self
    qs = Socialmedia.objects.filter_by_instance(instance)
    return qs


@property
def get_content_type(self):
    instance = self
    content_type = ContentType.objects.get_for_model(instance.__class__)
    return content_type
