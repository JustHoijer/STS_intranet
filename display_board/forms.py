from django import forms

from .models import Carousel, Slide


class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ["name"]


class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ["name", "label", "caption", "image", "duration"]
        labels = {"duration": "Duration (seconds)"}


# class CarouselForm(forms.ModelForm):
#     class Meta:
#         model = Carousel
#         fields = ['name']

#         labels = {
#             'name': 'Carousel Name'

#         }
#         # Define widget attributes to control form field rendering
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#         }

# class SlideForm(forms.ModelForm):
#     class Meta:
#         model = Slide
#         fields = ['name', 'label', 'caption', 'image', 'duration']

#         labels = {
#             'name': 'Slide Name',
#             'label': 'Label',
#             'caption': 'Caption',
#             'image': 'Background Image',
#             'duration': 'Duration On Screen'

#         }
#         # Define widget attributes to control form field rendering
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'label': forms.TextInput(attrs={'class': 'form-control'}),
#             'caption': forms.TextInput(attrs={'class': 'form-control'}),
#             'image': forms.FileInput(attrs={'class': 'form-control'}),
#             'duration': forms.NumberInput(attrs={'class': 'form-control'}),

#         }

# CarouselFormSet = forms.inlineformset_factory(
#     Carousel,
#     Slide,
#     form=SlideForm,
#     min_num=1,
#     extra=1,
#     can_delete=False
# )
