from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction
from django.contrib import auth
from django.forms.utils import ValidationError
from songr.models import PlaylistUpload, PickSong
#from songr.models import PickSong
#from django.utils.translation import ugettext_lazy as _

from users.models import User
#from songr.models import PlaylistUpload
class DejaySignupForm(UserCreationForm):
	"""docstring for DejaySignupForm"""
	email = forms.EmailField()

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		
	# Function overriding some field defaults from the usercreationform
	def __init__(self, *args, **kwargs):
		super(DejaySignupForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={'placeholder':"Username"})
		self.fields['email'].widget = forms.EmailInput(attrs={'placeholder':"Enter your email"})
		self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':"Password"})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':"Confirm password"})
		self.fields['email'].label = ''

		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
			self.fields[fieldname].label = ''


	def save(self, commit=True):
		user = super().save(commit = False)
		user.is_dejay = True
		if commit:
			user.save()
		return user

class RevelerSignupForm(UserCreationForm):
	"""docstring for DejaySignupForm"""
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super(RevelerSignupForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={'placeholder':"Username"})
		self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':"Password"})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':"Confirm password"})

		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
			self.fields[fieldname].label = ''

	def save(self):
		user = super().save(commit=False)
		user.is_reveler = True
		user.save()
		return user


class PlaylistForm(forms.ModelForm):
	class Meta:
		model = PlaylistUpload
		fields = ['song_file']

		widgets = {	
			'song_file':forms.FileInput(attrs={'multiple':True}),
		}

class PickSongForm(forms.ModelForm):
	# interests = forms.ModelMultipleChoiceField(
	# 	queryset = PlaylistUpload.objects.all(),
	# 	widget   = forms.CheckboxSelectMultiple(),
	# 	required = False
	# 	)
	class Meta:
		model = PickSong
		fields = ['interests']

		widgets = {	
			'interests':forms.CheckboxSelectMultiple,

		}

	# @classmethod
	# def files_are_valid(cls, request):
	# 	"""Takes a request and returns True if the uploaded files are valid. Otherwise returns found errors."""
	# 	uploaded_files = request.FILES.getlist('song_file')
	# 	if len(uploaded_files) >= 2:
	# 		# Django's validation does only work for a single file. When uploading multiple files only the last one gets
	# 		# checked for validity. We could subclass FileField to suit our needs. Somebody did that already:
	# 		# https://github.com/Chive/django-multiupload
	# 		# However, the pain of the following workaround is not strong enough to add another dependency.
	# 		# As we have multiple files we create a new form with the same data but only a single file for each file
	# 		# and check the new form's validity.
	# 		# Another alternative would be not relying on Django's automatic FileField validation at all and just do
	# 		# that tiny bit of validation ourselves for all files in request.FILES.
	# 		for uploaded_file in uploaded_files:
	# 			request.FILES['song_file'] = uploaded_file
	# 			temp_form = cls(request.POST, request.FILES)
	# 			if not temp_form.is_valid():
	# 				return temp_form.errors
	# 	return True
			
class myAuthenticationForm(AuthenticationForm):
	"""docstring for DejaySignupForm"""

	def __init__(self, *args, **kwargs):
		super(myAuthenticationForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={'placeholder':"Username"})
		self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':"Password"})


		for fieldname in ['username', 'password']:
			self.fields[fieldname].label = ''
