from rest_framework import serializers
from fachschaftszitat.models import Quote, Statement, Author
from django.contrib.auth.models import Group


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


class QuoteSerializer(serializers.ModelSerializer):
    statements = StatementSerializer(many=True)
    owner = GroupSerializer()

    class Meta:
        model = Quote
        fields = ('id', 'timestamp', 'statements', 'owner')
