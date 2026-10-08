from django import forms
from .models import Item,Category,ItemImage

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ["user", "status", "type"]

        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"style": "resize:None;", "rows":4})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class ItemImageForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = ItemImage
        fields = ["image"]
