from dataclasses import field
from http import client
import imp
from rest_framework import serializers
from books.models import Book
from members.models import MyUser
from passbook.models import PassBook

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields= '__all__'

class PassbookSerializers(serializers.ModelSerializer):
    class Meta:
        model = PassBook
        fields= '__all__'


