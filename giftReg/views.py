from django.shortcuts import render
from django.views import View
from giftReg.models import User


class Home(View):

    def get(self, request):
        return render(request, "main/index.html")


class Registration(View):

    def get(self, request):
        return render(request, "main/registration.html")

    def post(self, request):
        user = User(user_email=request.POST['userEmail'], user_username=request.POST['userName'],
                    user_password=request.POST['userPassword'])
        user.save()

        return render(request, "main/registration.html")
