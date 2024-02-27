import psutil

from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request):
        cpu = psutil.cpu_percent()
        battery = psutil.sensors_battery()
        print(cpu, battery)
        return render(request, 'index.html')


class Clock(View):
    def get(self, request):
        return render(request, 'soat.html')


class PythonAnywhere(View):
    def get(self, request):
        return render(request, 'inner-page.html')