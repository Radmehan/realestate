
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('booking now/',views.booking_now,name='booking_now'),
    path('service/',views.service,name='service'),

    path("house/",include('house.urls'))
    # path("cssdesign/",include('cssdesign.urls'))
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
