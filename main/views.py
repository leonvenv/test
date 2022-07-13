from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


from .models import ShortUrls
from .forms import UrlForm, RegisterUserForm, LoginUserForm
from .shortener import shortener

# Create your views here.
def Home(request, token):
    long_url = ShortUrls.objects.filter(ShortUrls=token)[0]
    return redirect(long_url.long_url)


def Make(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == "POST":
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortener().issue_token()
            NewUrl.ShortUrls = a
            NewUrl.save()
        else:
            form = UrlForm()
            a = "Invalid URL"
    return render(request, 'home.html', {'form': form, 'a': a})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    def get_success_url(self):
        return reverse_lazy('Make new')

def logout_user(request):
    logout(request)
    return redirect('Make new')
