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
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user
class UserAlterForm(forms.Form):
	password1 = forms.CharField(
		label=_("Original Password"),
		strip=True,
		widget=forms.PasswordInput,
		help_text=_("Please enter your original password."),
	)
	password2 = forms.CharField(
		label=_("New Password"),
		widget=forms.PasswordInput,
		strip=True,
		help_text=password_validation.password_validators_help_text_html(),
	)
	password3 = forms.CharField(
		label=_("Password confirmation"),
		widget=forms.PasswordInput,
		strip=True,
		help_text=_("Enter the same password as before, for verification."),
	)