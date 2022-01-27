from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from exchange_rate import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('exchange_rate/', views.index, name='index'),
    #path('about/', views.about, name='about'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)