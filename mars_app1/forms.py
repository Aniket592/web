# from django import forms


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=254)
#     message = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(),
#         help_text='Write here your message!'
#     )
#     source = forms.CharField(
#         max_length=50,
#         widget=forms.HiddenInput()
#     )

    # def clean(self):
    #     cleaned_data = super(ContactForm, self).clean()
    #     name = cleaned_data.get('name')
    #     email = cleaned_data.get('email')
    #     message = cleaned_data.get('message')
    #     if not name and not email and not message:
    #         raise forms.ValidationError('You have to write something!')




# class ColorfulContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'style': 'border-color: blue;',
#                 'placeholder': 'Write your name here'
#                 }
#             )
#         )
#     email = forms.EmailField(
#         max_length=254,
#         widget=forms.TextInput(attrs={'style': 'border-color: green;'})
#     )
#     message = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(attrs={'style': 'border-color: orange;'}),
#         help_text='Write here your message!'
#     )


from django.forms import ModelForm
from mars_app1.models import Spacians

# Create the form class.
class SpaciansForm(ModelForm):
    class Meta:
        model = Spacians
        fields = ['name','email','mobile_no','state','city','age']


            


    def clean(self):
        cleaned_data = super(SpaciansForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        mobile_no = cleaned_data.get('mobile_no')
        state = cleaned_data.get('state')
        city = cleaned_data.get('city')
        age = cleaned_data.get('age')
        if not name and not email and not age:
            raise forms.ValidationError('You have to write something!')