from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from NewsHub.models import WorldData, UserClass
from NewsHub.forms import SignUpForm


# Create your views here.
def newsfeed(request):
    """
    Root page view
    """
    worlds = WorldData.objects.order_by('world_name')

    # User details - world country and role
    if request.user.is_authenticated:
        # Redirect to Newsfeed page
        url_string = 'NewsFeed/newsfeed.html'
    else:
        # Redirect to Login Page
        url_string = 'registration/login.html'

    return render(request,
                  url_string,
                  {
                      "worlds": worlds,
                  }
                  )


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)
            email = form.cleaned_data['email']
            username = email.split('@')[0]
            raw_pwd = form.cleaned_data['password1']
            user = authenticate(email=email,
                                password=raw_pwd,)
            temp_form.username = username
            temp_form.save()
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        form = SignUpForm()
        return render(request,
                      'registration/signup.html',
                      {'form': form}
                      )
