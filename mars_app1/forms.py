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