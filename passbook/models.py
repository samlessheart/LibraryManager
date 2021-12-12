from django.db import models
import datetime
from django.conf import settings
from books.models import Book





# Create your models here.


class PassBook(models.Model):
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True,)
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, 
                                limit_choices_to={'is_employee': True}, related_name="staff")

    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    late_charges = models.DecimalField(default= 0, decimal_places=2, max_digits=8)
    complete = models.BooleanField(default= False)

    @property
    def due_date(self):
        return self.borrow_date + datetime.timedelta(days= 15)

    
    @property
    def due_charges(self):
        if self.due_date < datetime.date.today() and self.complete==False:
            return  (datetime.date.today()-self.due_date).days
        else:
            return 0
