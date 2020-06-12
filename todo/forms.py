from django import forms
from .models import Item


# Form class that inherrits from Django forms class
class ItemForm(forms.ModelForm):
    # Meta class tells the form which model it will be associated with
    class Meta:
        # Model associated with form
        model = Item
        # Form fields from model fields
        fields = ['name', 'done']