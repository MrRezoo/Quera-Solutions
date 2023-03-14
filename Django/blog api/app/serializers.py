from rest_framework import serializers

from app.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('title', 'body', 'created', 'owner')


class PostDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comment_set = serializers.HyperlinkedRelatedField(view_name='comment_detail', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'created', 'updated', 'owner', 'comment_set')
        read_only_fields = ('created', 'owner', 'comment_set')


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username', read_only=True)
    post = serializers.HyperlinkedRelatedField(view_name='post_detail', read_only=True)

    class Meta:
        model = Comment
        fields = ('post', 'owner', 'body', 'created', 'updated')
        read_only_fields = ('post', 'created', 'owner')
