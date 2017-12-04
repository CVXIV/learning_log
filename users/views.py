from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import CaptchaModelForm
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import json
from django.http import HttpResponse
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))
def register(request):
	if request.GET.get('newsn') == '1':
		csn = CaptchaStore.generate_key()
		cimageurl = captcha_image_url(csn)
		return HttpResponse(cimageurl)
	if request.method!='POST':
		form=CaptchaModelForm()
	else:
		form=CaptchaModelForm(data=request.POST)
		if form.is_valid():
			new_user=form.save()
			#让用户自动登录，再重定向到主页
			authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
			login(request,authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))
	context={'form':form}
	return render(request,'users/register.html',context)