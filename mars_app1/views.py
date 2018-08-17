
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Spacians

from .forms import SpaciansForm

def description(request):
	t_name='d_index.html'
	return render(request, t_name, )

def _form_view(request, template_name='basic.html', form_class=SpaciansForm):
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			name = request.POST.get('name','')
			email = request.POST.get('email','')
			mobile_no = request.POST.get('mobile_no','')
			state = request.POST.get('state','')
			city = request.POST.get('city','')
			age = request.POST.get('age','') 
			s_obj = Spacians(name = name , email = email , mobile_no = mobile_no , state = state , city = city , age = age)
			s_obj.save()
			return render(request,"thanku.html",)
			#pass  # does nothing, just trigger the validation
	else:
		form = form_class()
	return render(request, template_name, {'form': form})


def achievment(request):
	t_name='ac_index.html'
	return render(request, t_name, )


def timeline(request):
	t_name='time_index.html'
	return render(request, t_name, )

def home(request):
	t_name='home_index.html'
	return render(request, t_name, )


