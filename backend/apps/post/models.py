from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel
from core.services.file_service import upload_post_photos

UserModel = get_user_model()


class PostModel(BaseModel):
    class Meta:
        db_table = 'posts'
        ordering = ['id']

    title = models.CharField(max_length=256, blank=False, null=False)
    text = models.TextField(max_length=1024, blank=False, null=False)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')


class PostPhotoModel(models.Model):
    class Meta:
        db_table = 'post_photos'
    photo = models.ImageField(upload_to=upload_post_photos, blank=False)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='photos')
