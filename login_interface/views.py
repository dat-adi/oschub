from django.shortcuts import render
from login_interface.forms import UserForm
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "login_interface/main_page.html"


def registration_portal(request):
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

    return render(request, 'login_interface/registration_portal.html', context={'registered': registered,
                                                                                'user_form': user_form})


