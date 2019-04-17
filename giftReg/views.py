from django.shortcuts import render
from django.views import View
from giftReg.models import User


class Home(View):

    def get(self, request):
        return render(request, "main/index.html")

    def post(self, request):
        username = request.POST['userName']
        password = request.POST['userPassword']

        already_logged_in = False

        try:
            user = User.objects.get(user_authenticated=True)
            already_logged_in = True
        except User.DoesNotExist:
            already_logged_in = False

        if already_logged_in:
            return render(request, "main/index.html", {"message": "User already logged in."})

        try:
            user = User.objects.get(user_username=username)
        except User.DoesNotExist:
            return render(request, "main/index.html", {"message": "Username not found."})

        if user.user_password != password:
            return render(request, "main/index.html", {"message": "Invalid password."})
        else:
            User.objects.filter(user_username=username).update(user_authenticated=True)
            return render(request, "main/index.html", {"message": "Login successful."})


class Success(View):

    def get(self, request):
        return render(request, "main/success.html")


class Users(View):

    def get(self, request):
        return render(request, "main/users.html")


class Gifts(View):

    def get(self, request):
        return render(request, "main/gifts.html")


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
            return render(request, "main/success.html")
        else:
            return render(request, "main/registration.html", {"message": "Failure, username or email address already "
                                                                         + "taken"})
