from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from MobileInvitation import settings
from accountapp.views import AccountCreateView, AccountDeleteView, AccountLoginView

app_name = "accountapp"

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view() , name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    #path('update/', login , name='main'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
