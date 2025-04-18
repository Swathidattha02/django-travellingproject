from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'location', 'stay_details', 'food_details', 'transport_details', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'stay_details': forms.Textarea(attrs={'class': 'form-control'}),
            'food_details': forms.Textarea(attrs={'class': 'form-control'}),
            'transport_details': forms.Textarea(attrs={'class': 'form-control'}),
        } 