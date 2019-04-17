from django.shortcuts import render
from django.views import View


# Create your views here.

class Home(View):

    def get(self, request):
        return render(request, "main/index.html")


class Registration(View):

    def get(self, request):
        return render(request, "main/registration.html")
