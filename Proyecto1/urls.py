from django.contrib import admin
from django.urls import path
from Proyecto1.views import home, result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('result/', result, name="result"),
]
