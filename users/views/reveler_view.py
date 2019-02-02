from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from users.forms import DejaySignupForm, RevelerSignupForm
from users.models import User

class RevelerSignUpView(CreateView):
    model = User
    form_class = RevelerSignupForm
    template_name = 'users/reveler_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'dejay'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('djroll-home')