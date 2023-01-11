from django.shortcuts import render, redirect
from . forms import RegisterForm

# Create your views here.

# register handles the /POST endpoint for registering a user.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()   

        redirect('admin/')  # After registering, and submiting the form, 
                            # the page re-routes to the admin page.
    else:
        form = RegisterForm()

    return render(response, "authentication/register.html", {"form":form})    


