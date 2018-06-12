from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    url(r'^edit-profile/',views.edit_profile, name = 'edit_profile'),
    url(r'^car-details/',views.car_details, name = 'car_details'),
    url(r'^$',views.home, name ='home'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
