from django import forms
from .models import Image, ImageCategory


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('image_id', 'title', 'category_id','image')
        labels = {'image_id':"Image ID", 'title': "Image Title", "category_id": "Category ID", "image":"Image URL",}


class CategoryForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = ImageCategory
        fields = ('category_id', 'category')
        labels = {'category_id': "Category ID", "category": "Category Name",}
