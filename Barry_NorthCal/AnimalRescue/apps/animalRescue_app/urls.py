from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'home'),
    url(r'^registerAnimal$', views.registerAnimal, name = 'registerAnimal'),
    url(r'^adopt$', views.adoptaPet, name = 'adoptaPet'),
    url(r'^adopt/(?P<id>\d+)$', views.adopt_animal, name = 'adopt_animal'),
    url(r'^successStories$', views.successStories, name = 'successStories'),
    url(r'^donate$', views.donate, name = 'donate'),
    url(r'^volunteer$', views.volunteer, name = 'volunteer'),
    url(r'^contactUs$', views.contactUs, name = 'contactUs'),
    url(r'^aboutUs$', views.aboutUs, name = 'aboutUs'),
    url(r'^staff$', views.ourStaff, name = 'ourStaff'),
    url(r'^uploads$', views.upload_file, name = 'upload_file'),
    url(r'^signup/(?P<return_site>[a-z]+)$', views.signup, name='signup'),
    url(r'^update/(?P<id>\d+)$', views.update_animal, name='update_animal'),
    url(r'^delete/(?P<id>\d+)$', views.delete_animal, name='delete_animal'),
    url(r'^login/(?P<return_site>[a-z]+)$', views.loginUser, name='loginUser'),
    url(r'^administrator/all_animals$', views.viewAllAnimals, name = 'viewAllAnimals'),
    url(r'^logout$', views.logoutUser, name='logoutUser'),
    url(r'^load$', views.loadContent, name='loadContent'),
    url(r'^loadContent$', views.loadAnyContent, name = 'loadAnyContent'),
    url(r'^uploadImage$', views.loadImage, name='loadImage'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
