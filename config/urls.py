from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth import get_user_model

def create_admin(request):
    User = get_user_model()
    user, created = User.objects.get_or_create(username='fonevia')
    user.is_superuser = True
    user.is_staff = True
    user.set_password('Fonevia@123')
    user.save()
    return HttpResponse("Admin Ready: fonevia / Fonevia@123")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('create-admin/', create_admin),
]