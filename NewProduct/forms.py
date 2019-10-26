from django import forms
from Run.models import Product
from ckeditor.widgets import CKEditorWidget



class ProductCreateForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Product
        fields = ['category',
                  'slug',
                  'name',
                  'Image',
                  'description',
                  'model_number']
