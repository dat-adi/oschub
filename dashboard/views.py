from django.shortcuts import render
from django.views.generic import TemplateView
from dashboard.forms import UserForm


class WelcomeView(TemplateView):
    template_name = "dashboard/welcome.html"


def registration(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'dashboard/registration.html', context={'registered': registered,
                                                                   'user_form': user_form})
