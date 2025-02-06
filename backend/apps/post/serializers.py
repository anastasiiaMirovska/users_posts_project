from rest_framework.serializers import ModelSerializer

from apps.post.models import PostModel, PostPhotoModel


class PostPhotoSerializer(ModelSerializer):
    class Meta:
        model = PostPhotoModel
        fields = (
            'id',
            'photo',
            'post'
        )
        read_only_fields = ('id', 'post')


class PostSerializer(ModelSerializer):
    photos = PostPhotoSerializer(many=True)

    class Meta:
        model = PostModel
        fields = (
            'id',
            'title',
            'text',
            'author',
            'photos',
            'created_at',
            'updated_at'
        )
        read_only_fields = (
            'id',
            'author',
            'created_at',
            'updated_at'
        )
