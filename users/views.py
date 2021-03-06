from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import UserCreationForm,UserAlterForm
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))
def register(request):
	if request.GET.get('newsn') == '1':
		csn = CaptchaStore.generate_key()
		cimageurl = captcha_image_url(csn)
		return HttpResponse(cimageurl)
	if request.method!='POST':
		form=UserCreationForm()
	else:
		form=UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user=form.save()
			#让用户自动登录，再重定向到主页
			authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
			login(request,authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))
	context={'form':form}
	return render(request,'users/register.html',context)
@login_required
def setting(request):
	if request.method!='POST':
		form=UserAlterForm()
	else:
		form = UserAlterForm(data=request.POST)
		if form.is_valid():
			username = request.user.username
			oldpassword = request.POST['password1']
			user = authenticate(username=username, password=oldpassword)
			newpassword = request.POST['password2']
			user.set_password(newpassword)
			user.save(update_fields=['password'])
			login(request, user)
			return HttpResponseRedirect(reverse('learning_logs:index'))
	context = {'form': form}
	return render(request, 'users/setting.html', context)
@csrf_exempt
def check_data(request):
	user=User.objects.filter(username=request.POST['username'])
	cs = CaptchaStore.objects.filter(response=request.POST['response'],hashkey=request.POST['hashkey'])
	if cs.exists() and not user.exists():
		is_validate={'result':False}
	else:
		if user.exists():
			is_validate = {'result': 'username'}
		else:
			is_validate = {'result':'captcha'}
	return HttpResponse(json.dumps(is_validate), content_type="application/json")
@csrf_exempt
def check_pass(request):
	username = request.user.username
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None and user.is_active:
		is_validate={'result':False}
	else:
		is_validate = {'result': True}
	return HttpResponse(json.dumps(is_validate), content_type="application/json")