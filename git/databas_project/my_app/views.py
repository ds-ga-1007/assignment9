from django.shortcuts import render
from django.template import loader,RequestContext
from django.shortcuts import get_object_or_404, render, render_to_response
from my_app.models import Cuisines, Review, Recipies, LoginForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
# Create your views here.
def home(request):
    template=loader.get_template('home.html')
    context = {
        'recipies' : Recipies.objects.all(),

    }
    return render(request, "home.html")

from django.contrib.auth import authenticate, login

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/success.html")# Redirect to a success page.

    return render(request, 'home.html', {'login_form': form })

