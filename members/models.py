from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.db.models.fields.related import ManyToManyField
from django.utils.translation import gettext_lazy as _

from books.models import Book



# Create your models here.

class MyUserManager(BaseUserManager):

    def create_user(self, email, member_id, password=None, **other_fields):

        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(email = self.normalize_email(email),  member_id= member_id, **other_fields)
        user.set_password(password)
        user.save(using=self._db)        
        return user
    
    def create_superuser(self, email, member_id, password=None, **other_fields):

        user = self.create_user(email, member_id, password=password, **other_fields)
                
        user.is_active = True
        user.is_admin = True

        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser): 

    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True,)
    member_id = models.IntegerField(unique=True,  verbose_name='Member id')
    phone = models.CharField(max_length=10, blank=True, null=True, verbose_name='Phone Number')

    is_active = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)    
    
    fname = models.CharField(max_length=100, blank=True, null=True, verbose_name ='First Name')
    lname = models.CharField(max_length=100, blank=True, null=True, verbose_name='Last Name')
    date_added = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['member_id',]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin    

    def __str__(self):
        return self.email
    
    class Meta:
      abstract = False




# class Profile(models.Model):
#     user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile')
#     wishlist = models.ManyToManyField(Book, blank=True,  )
#     borrowed_book = models.ForeignKey(Book, blank=True, null=True, on_delete=models.SET_NULL, related_name='Borrowed_Book')
#     dob = models.DateField(blank=True, null=True)
#     premium = models.BooleanField(default=False)
#     second_book= models.ForeignKey(Book, blank=True, null=True, on_delete=models.SET_NULL, related_name='second_Book')
#     pic = models.ImageField(null= True)    
    
#     def __str__(self):
#         return str(self.user)





    