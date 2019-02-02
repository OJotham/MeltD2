from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from users.forms import DejaySignupForm, RevelerSignupForm
from users.models import User
from songr.models import PlaylistUpload

class DejaySignUpView(CreateView):
    model = User
    form_class = DejaySignupForm
    template_name = 'users/dejay_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'dejay'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('djroll-home')


class SignUpView(TemplateView):
	template_name = 'users/signup.html'

# def upload_song(request):
#     if request.method == 'POST':
#         form = PlaylistUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             songs_saved = form.save(commit=False)
#             songs_saved.user = request.user
#             songs_saved.save()
#             return HttpResponseRedirect('')
#     else:
#         form = PlaylistUploadForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'users/dj_profile.html', context)


        


