from django import forms
from.models import tbl


class todoform(forms.ModelForm):
    class Meta:
        model=tbl
        fields=['username','password','email']
