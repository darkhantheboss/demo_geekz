from django.conf.urls import include, url
from django.contrib import admin
from .views import CheckView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^check/$', CheckView.as_view()),
]