from django.contrib import admin
from django.urls import path, include
from portfolio import views 
#from quote_generator import views
#from exchange_rate import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #path('about/', views.about, name='about'),
    path('blogs/', include('blog.urls')),
    #path('exchange_rate/', views.index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)