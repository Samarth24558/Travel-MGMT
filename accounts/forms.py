
from django.forms import ModelForm
from .models import *
from django import forms



class InsertForm(ModelForm):
    class Meta:
         model=Insert
         fields ='__all__'

         
class Party_gcForm(ModelForm):
    class Meta:
         model=Party_gc
         fields ='__all__'

class ConsignorForm(ModelForm):
    class Meta:
         model=Consignor
         fields ='__all__'


class ConsigneeForm(ModelForm):
    class Meta:
         model=Consignee
         fields ='__all__'