from django import forms
from django.db.models import fields

from BlogApp.models import PostComments,register
class loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    
    
    
    
class register(forms.ModelForm):
    class Meta:
        model = register
        fields = ('username','email','first_name','last_name','password','confirm_password')
        widget = {'password':forms.PasswordInput,'password':forms.PasswordInput,
        'username':forms.TextInput(attrs={'class':'form-control','placeholder':'yaha name lekheya '}),'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'yaha name lekheya '}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'yaha name lekheya '})}
        def clean(self):
            cleaned_data = super().clean()
            valpass = self.cleaned_data['password']
            valrpass = self.cleaned_data['confirm_password']
            if valpass != valrpass:
                raise forms.ValidationError("Password not match........")
class PostCommentsforms(forms.ModelForm):
    class Meta:
        model = PostComments
        fields = ['name','email','subject','comments']
        widget = {'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),'email':forms.EmailField(),'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Subject Line'}),'Comments':forms.Textarea(attrs={'class':'form-control','placeholder':'Write comments here'})}            