from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path

from MobileInvitation import settings
from invitationapp.views import InvitationDetailView, InvitaionCreate, InvitaionEdit, InvitationCreateComment, \
    InvitationDeleteComment

app_name = "invitationapp"

urlpatterns = [
    path('create/', InvitaionCreate, name='create'),
    path('edit/<int:pk>', InvitaionEdit, name='edit'),
    path('<int:pk>', InvitationDetailView, name='invitation'),
    path('<int:pk>/comment/create', InvitationCreateComment, name='createComment'),
    path('<int:pk>/comment/delete', InvitationDeleteComment, name='deleteComment')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
