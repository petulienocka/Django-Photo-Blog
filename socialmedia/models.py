from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User


# crating manager allows me to go off the model and get the comments by instance
class SocialmediaManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(SocialmediaManager, self).filter(
            content_type=content_type, object_id=obj_id)
        return qs


class Socialmedia (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    objects = SocialmediaManager()

    def __str__(self):
        return str(self.user.username)
