from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('jeanspant/',views.ProductView.as_view(), name='jeanspant'),
    path('lehenga/',views.LehengaView.as_view(), name='lehenga'),
    path('tshirt/',views.TshirtView.as_view(), name='tshirt'),
    path('boyshirt/',views.BoyShirtView.as_view(), name='boyshirt'),
    path('borkha/',views.BorkhaView.as_view(), name='borkha'),
    path('winter/',views.WinterView.as_view(), name='winter'),
    path('phone/',views.PhoneView.as_view(), name='phone'),
    path('elecs/<int:pk>/',views.ProductDetalisView.as_view(), name='elecs'),
    path('shirtview/<int:pk>/',views.ShirtDetalisView.as_view(), name='shirtview'),
    path('form/',views.register,name='form'),
    path('login/',views.loginview,name='login'),



]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)