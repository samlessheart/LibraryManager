from django.db import models
from django.db.models import indexes
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth import get_user_model
import datetime
from django.urls import reverse 

#from members.models import MyUser

# Create your models here.
genre = [('ch', 'Charitra'), ('sci', 'science' ), ('hea','health'), ('nov','novel'), ('sto', 'stories'), ]

class Author(models.Model):
    name = models.CharField(max_length=300,)
    dob = models.IntegerField(blank=True, null=True,)
    doe = models.IntegerField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)

    class Meta:
        indexes = [models.Index(fields=['name', 'detail', ]),]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('authordetail', args=[str(self.id)]) 


class Publication(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    class Meta:
        ordering = ['-name']
        indexes = [models.Index(fields=['name', ]),]

class Book(models.Model):
    doc_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200, )
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL, )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pages = models.IntegerField()
    genre = models.CharField(max_length=3, choices=genre, default='Novel')
    tags = models.CharField(max_length=300, blank=True, null= True)
    published = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    Wished_by = models.IntegerField(default=0)
    read_by = models.IntegerField(default=0)
    publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, blank=True, null=True,)
    vendor = models.CharField(max_length=200, blank=True, null=True,) 

    class Meta:
        ordering = ['-doc_id']
        indexes = [models.Index(fields=['name', 'tags', 'genre']),]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bookdetail', args=[str(self.id)]) 







    

     
    
