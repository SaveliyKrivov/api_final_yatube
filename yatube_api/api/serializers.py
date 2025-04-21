from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('id', 'author')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('id', 'author', 'post')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = '__all__'
        model = Follow
        read_only_fields = ('id', 'user')

    def validate_following(self, value):
        request = self.context.get('request')
        if request:
            if request.user == value:
                raise serializers.ValidationError(
                    "Нельзя подписаться на самого себя")

        return value
