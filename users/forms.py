from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import ugettext_lazy as _
class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(
		label=_("Password"),
		strip=True,
		widget=forms.PasswordInput,
		help_text=password_validation.password_validators_help_text_html(),
	)
	password2 = forms.CharField(
		label=_("Password confirmation"),
		widget=forms.PasswordInput,
		strip=True,
		help_text=_("Enter the same password as before, for verification."),
	)
	captcha=CaptchaField()
	class Meta:
		model = User
		fields = ("username",)
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		if self._meta.model.USERNAME_FIELD in self.fields:
			self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user