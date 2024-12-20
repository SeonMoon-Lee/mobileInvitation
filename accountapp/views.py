import os
import shutil

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView

from MobileInvitation import settings
from invitationapp.models import InvitationInfo, InvitationGallery


# Create your views here.

class AccountLoginView(LoginView):
    model = User
    success_url = reverse_lazy("invitationapp:create")
    template_name = "accountapp/login.html"

    def get(self, request, *args, **kwargs):
        print(f"Authenticated: {request.user.is_authenticated}")
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("accountapp:login")
    template_name = "accountapp/create.html"


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = "accountapp/delete.html"

    def post(self, request, *args, **kwargs):
        media_path = os.path.join(settings.MEDIA_ROOT, 'res', 'image', request.user.username)

        # 디렉토리가 존재하는지 확인하고 삭제
        if os.path.isdir(media_path):
            shutil.rmtree(media_path)  # 디렉토리와 내부 파일 삭제
            print(f"Deleted media directory: {media_path}")
        else:
            print(f"Directory does not exist: {media_path}")

        return super().delete(request, *args, **kwargs)