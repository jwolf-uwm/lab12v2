from django.shortcuts import render
from django.views import View

from giftReg.models import User

# Create your views here.


class Home(View):

    def get(self, request):
        return render(request, "main/index.html")


class Registration(View):

    def get(self, request):
        return render(request, "main/registration.html")

    def post(self, request):
        user = User(user_email=request.POST['userEmail'], user_username=request.POST['userName'],
                    user_password=request.POST['userPassword'])

        does_exist = True

        try:
            check_email = User.objects.get(user_email=user.user_email)
            does_exist = True
        except User.DoesNotExist:
            does_exist = False

            try:
                check_username = User.objects.get(user_username=user.user_username)
                does_exist = True
            except User.DoesNotExist:
                does_exist = False

        if not does_exist:
            user.save()
            return render(request, "main/registration.html", {"message": "Success!"})
        else:
            return render(request, "main/registration.html", {"message": "Failure, username or email address already "
                                                                         + "taken"})
