
from django import forms



class borrowForm(forms.Form):
    member_id = forms.IntegerField(required=True)