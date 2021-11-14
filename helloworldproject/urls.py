from django.contrib import admin
from django.urls import path, include
from .views import helloworldfunc
from .views import HelloworldClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworldurl/', helloworldfunc),
    path('helloworldurl2/', HelloworldClass.as_view()),
    path('', include('helloworldapp.urls'))
]
