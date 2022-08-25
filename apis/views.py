from rest_framework import status
from datetime import datetime
from django.shortcuts import render
from books.models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from passbook.models import PassBook
from members.models import MyUser
from .serializers import BookSerializer, MyUserSerializer, PassbookSerializers
from rest_framework import status


@api_view(['GET'])
def book_list(request):
    if request.method == "GET":
        book_obj = Book.objects.all()
        book_ser = BookSerializer(book_obj, many= True)
        return Response(book_ser.data)


@api_view(['GET'])
def book_detail(request, pk):
    if request.method == "GET":
        book_obj = Book.objects.get(id= pk)
        if book_obj:
            book_ser = BookSerializer(book_obj)
            return Response(book_ser.data)
        else:
            return Response(status= status.HTTP_404_NOT_FOUND)


@api_view(['DELETE', 'PUT'])
def book_det(request, pk):
    if request.user.is_employee == False:
        return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        if request.method == "DELETE":
            book_obj = Book.objects.get(id= pk)
            book_obj.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        elif request.method == "PUT":
            book_obj = Book.objects.get(id= pk)
            book_ser = BookSerializer(instance=book_obj, data= request.data)
            if book_ser.is_valid():
                book_ser.save()
                return Response(book_ser.data)



@api_view(['POST'])
def book_create(request):
    if request.user.is_employee:
        book_ser = BookSerializer(data=request.data)
        if book_ser.is_valid():
            book_ser.save()
        return Response(book_ser.data)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)



@api_view(['GET'])
def user_list(request):
    if request.user.is_employee:
        user_list = MyUser.objects.all()
        user_ser = MyUserSerializer(user_list, many=True)
        return Response(user_ser.data)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'PUT', 'DELETE'])
def user_det(request, pk):
    if request.user.is_employee:
        user = MyUser.objects.get(id=pk)
        if request.method == 'GET':
            user = MyUser.objects.get(id=pk)
            user_ser = MyUserSerializer(user, )
            return Response(user_ser.data)
        elif request.method == 'PUT':
            user_ser = MyUserSerializer(instance=user, data=request.data)
            if user_ser.is_valid():
                user_ser.save()
                return Response(user_ser.data)
        elif request.method == 'DELETE':
            user.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
        


@api_view(['POST'])
def borrow(request, pk):
    book = Book.objects.get(id = pk)
    user = request.user
    if request.method == 'POST':
        book.in_stock = False
        prof = user.profile
        prof.borrowed_book = book
        prof.save()
        book.save()
        passentry = PassBook.objects.create(member=user, book = book)
        passentry.save()


@api_view(['POST'])
def return_book(request, pk):
    pass_obj = PassBook.objects.get(id=pk)
    book = Book.objects.get(id = pass_obj.book.id)
    user = request.user
    prof_obj = user.profile
    if request.method == 'POST':
        book.in_stock = True
        pass_obj.return_date = datetime.now()
        pass_obj.complete = True
        prof_obj.borrowed_book = None
        prof_obj.save()
        pass_obj.save()
        return Response()


@api_view(['GET'])
def passbook(request):
    user = request.user
    pass_obj = PassBook.objects.filter(member = user)
    pass_obj_ser = PassbookSerializers(pass_obj, many = True)

