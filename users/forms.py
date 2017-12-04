from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm

class CaptchaModelForm(UserCreationForm):
	captcha = CaptchaField()
	def clean(self):
		try:
			self.cleaned_data['captcha']
		except Exception as e:
			'except: ' + str(e)
			raise forms.ValidationError(u"验证码有误，请重新输入!")
		return self.cleaned_data