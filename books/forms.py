from django import forms
from django.forms import (fields, widgets, Textarea, NumberInput, Select, DateField)
from books.models import Book, Author





class bookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields  = ['doc_id', 'name', 'author', 'price', 'pages', 'genre', 
                        'tags', 'published', 'publication', 'vendor']
        
        widgets = {
            'doc_id': Textarea(attrs={'rows': 1,'class': 'form-control col-8'}),
            'name': Textarea(attrs={ 'rows': 1, 'class': 'form-control col-8'}),
            'author': Select(attrs={ 'rows': 1, 'class': 'form-control col-8'}),
            'price': NumberInput(attrs={'rows': 1,'class': 'form-control col-8'}),
            'pages': NumberInput(attrs={'rows': 1,'class': 'form-control col-8'}),
            'genre': Select(attrs={'class': 'form-control col-8'}),
            'tags': Textarea(attrs={'rows': 1,'class': 'form-control col-8'}),
            'published': NumberInput(attrs={'rows': 1,'class': 'form-control col-8'}),
            'publication': Textarea(attrs={'rows': 1,'class': 'form-control col-8'}),
            'vendor': Textarea(attrs={'rows': 1,'class': 'form-control col-8'}),
        }
    

class authorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'dob', 'doe', 'detail']

        widgets = {
            'name': Textarea(attrs={'rows': 1, 'class': 'form-control col-8'}),
            'dob': NumberInput(attrs={'rows': 1, 'class': 'form-control col-8'}),
            'doe': NumberInput(attrs={'rows': 1, 'class': 'form-control col-8'}),
            'detail': Textarea(attrs={'rows': 1, 'class': 'form-control col-8'}),
        }
    