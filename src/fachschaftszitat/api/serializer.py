from rest_framework import serializers
from fachschaftszitat.models import Quote, Statement, Author, Gif
from django.contrib.auth.models import Group, User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class StatementSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False)

    class Meta:
        model = Statement
        fields = ('id', 'order_id', 'text', 'author')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class QuoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    timestamp = serializers.DateField()
    statements = StatementSerializer(many=True)
    owner = GroupSerializer()
    is_creator = serializers.BooleanField()
    delete_url = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class GifSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    type = serializers.ChoiceField(choices=Gif.TYPE_CHOICES)
    video_url = serializers.URLField()
    creator = UserSerializer(read_only=True)

    def create(self, validated_data):
        return Gif.objects.create(**validated_data)
