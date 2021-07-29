from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('overseas/', views.overseas, name="overseas"),
    path('activity/', views.activity, name="activity"),
    path('contest/', views.contest, name="contest"),
    path('school/', views.school, name="school"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)