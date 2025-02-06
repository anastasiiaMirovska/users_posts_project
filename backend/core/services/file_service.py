import os
from uuid import uuid1


def upload_user_photos(instance, filename: str) -> str:
    ext = filename.split('.')[-1]
    return os.path.join('user_profile_photos', instance.user.email, f'{uuid1()}.{ext}')


def upload_post_photos(instance, filename: str) -> str:
    ext = filename.split('.')[-1]
    folder_name = instance.post.author.email + '- post -' + str(instance.post.id)
    return os.path.join('post_photos', folder_name, f'{uuid1()}.{ext}')

