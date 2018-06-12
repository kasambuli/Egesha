from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'lotOwner'

urlpatterns=[
    url(r'^owner/',views.home, name='Lot'),
    url(r'^details/(\d+)',views.Lotdetail,name='Details'),
    url(r'^map/',views.map,name='Map'),
    url(r'^location/',views.location,name='Location')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
