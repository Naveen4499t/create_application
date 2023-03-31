from django import forms

class CompanyForm(forms.Form):
    mobile=forms.IntegerField()
    password=forms.CharField(max_length=100)
    confirmpassword=forms.CharField(max_length=100)