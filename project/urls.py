from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('summernote/', include('django_summernote.urls')),

    path('admin/', admin.site.urls),
    path('meals/',include('meals.urls',namespace='meals')),
    path('blog/',include('blog.urls',namespace='blog')),
    path('contact/',include('contact.urls',namespace='contact')),
    path('reserve_table/',include('reservation.urls',namespace='reservation')),
    path('about-us/',include('aboutus.urls',namespace='aboutus')),
    path('',include('home.urls',namespace='home')),
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = "Resturant AdminPanel"
admin.site.site_header = "Resturant App Admin"
admin.site.index_title = "Welcome to Resturant Admin Panel"







