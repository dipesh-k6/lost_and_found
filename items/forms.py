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

# form validation for items
    def clean_title(self):
        title = self.cleaned_data.get("title").strip()

        if  len(title)<2:
            raise forms.ValidationError("invlaid title")
        return title.title()

    def clean_description(self):
        description = self.cleaned_data.get("description").strip()

        if  len(description)<5:
            raise forms.ValidationError("description must be longer")

        return description

    def clean_district(self):
        district = self.cleaned_data.get("district").strip()

        if len(district)<3:
            raise forms.ValidationError("district name must be longer")

        return district.title()

    def clean_city(self):
        city = self.cleaned_data.get("city").strip()

        if len(city)<3:
            raise forms.ValidationError("city name must be longer")

        return city.title()

    def clean_specific_location(self):
        specific_location = self.cleaned_data.get("specific_location")

        if specific_location :
            specific_location = specific_location.strip()
            if len(specific_location)<5:
                raise forms.ValidationError("specific location name must be longer")

        return specific_location


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

# form validation for category
    def clean_name(self):
        name = self.cleaned_data.get("name").strip()

        if len(name)<2:
            raise forms.ValidationError("category name must be longer")

        return name.title()

class ItemImageForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = ItemImage
        fields = ["image"]

# form validation for image
    def clean_image(self):
        image = self.cleaned_data.get("image")

        if not image:
            raise forms.ValidationError("please include an image")
        else:
            valid_extensions = ["jpg", "jpeg", "png"]
            url = image.name.rsplit('.',1)[1].lower()

            if url not in valid_extensions:
                raise forms.ValidationError(f"invalid file uploaded | allowed extensions => {', '.join(valid_extensions)}")

            if image.size > 5*1024*1024:
                raise forms.ValidationError("image size must be 5MB or smaller")

            return image
