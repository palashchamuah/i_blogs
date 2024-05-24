from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.urls import path, include
from .views import Home, post

urlpatterns = [
    path('', views.Home, name ='Home'),
    path('about/', views.About, name='About'),
    path('contact/', views.ContactPage, name ='ContactPage'),
    path('form', views.contactData, name ='contactData'),

    ## for single blog view, we are fetching the slug in urls
    path('blog/<slug:url>', views.post),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
