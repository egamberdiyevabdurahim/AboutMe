from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, 'index.html')


class Clock(View):
    def get(self, request):
        return render(request, 'soat.html')


class PythonAnywhere(View):
    def get(self, request):
        return render(request, 'inner-page.html')


class GitHub(View):
    def get(self, request):
        return render(request, 'github.html')