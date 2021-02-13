from django import forms

class memePostForm(forms.Form):
    name     = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    caption  = forms.CharField(widget=forms.Textarea(attrs={'rows' : 2, 'class' : 'form-control'}))
    url      = forms.URLField(widget=forms.URLInput(attrs={'class' : 'form-control'}))
    
class editForm(forms.Form):
    #id       = forms.IntegerField(widget=forms.HiddenInput())
    name     = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'readonly' : 'readonly'}))
    caption  = forms.CharField(widget=forms.Textarea(attrs={'rows' : 2, 'class' : 'form-control'}))
    url      = forms.URLField(widget=forms.URLInput(attrs={'class' : 'form-control'}))