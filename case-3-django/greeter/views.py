from django.shortcuts import render
from .forms import UserNameForm
from .models import UserName


def home(request):
    greeting_name = None

    if request.method == "POST":
        form = UserNameForm(request.POST)
        if form.is_valid():
            greeting_name = form.cleaned_data["name"]
            UserName.objects.create(name=greeting_name)
    else:
        form = UserNameForm()

    return render(
        request, "greeter/home.html", {"form": form, "greeting_name": greeting_name}
    )
