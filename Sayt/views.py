import platform
import psutil
# import android

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


class WhiteNoise(View):
    def get(self, request):
        def get_system_info():
            system_info = {
                "Operatsion tizim": platform.system(),
                "Operatsion tizimning chiqarilishi": platform.release(),
                "Arxitektura": platform.machine(),
                "Protsessor": platform.processor(),
                "Xotira": psutil.virtual_memory().total,
                "Disk": psutil.disk_usage('/').total,
            }
            return system_info
    
        system_info = get_system_info()
        for key, value in system_info.items():
            print(f"{key}: {value}")
        return render(request, 'whitenoise.html')


class AboutGadget(View):
    def get(self, request):
        def get_system_info():
            system_info = {
                "Operatsion_tizim": platform.system(),
                "Operatsion_tizimning_chiqarilishi": platform.release(),
                "Platforma": platform.platform(),
                "Arxitektura": platform.machine(),
                "Bit": platform.architecture()[0],
                "Versiya": platform.version(),
                "Tarmoq_Nomi": platform.node(),
                "Protsessor": platform.processor(),
                "Xotira": psutil.virtual_memory().total,
                "Disk": psutil.disk_usage('/').total,
            }
            return system_info

        # def get_device_info():
        #     droid = android.Android()
        #     info = {}

        #     model = droid.getDeviceModel().result
        #     info["Model"] = model

        #     manufacturer = droid.getManufacturer().result
        #     info["Manufacturer"] = manufacturer

        #     android_version = droid.getApiVersion().result
        #     info["Android Version"] = android_version

        #     battery_level = droid.batteryGetLevel().result
        #     info["Battery Level"] = battery_level

        #     display_info = droid.getDisplayInfo().result
        #     width = display_info["width"]
        #     height = display_info["height"]
        #     info["Screen Resolution"] = f"{width}x{height}"

        #     return info

        # device_info = get_device_info()
        # for key, value in device_info.items():
        #     print(f"{key}: {value}")
    
        pc = {
            'pcplatform': get_system_info()
        }
        return render(request, 'about-gadget.html', pc)