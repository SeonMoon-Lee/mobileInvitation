import base64

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView

from invitationapp.forms import CreateViewForm, UpdateViewForm, GreetingsViewForm, LocationViewForm
from invitationapp.models import InvitationInfo, InvitationGreetingsInfo, InvitaionFamilyInfo, InvitationLocationInfo, \
    InvitationContactInfo, InvitationAccountInfo, InvitationGallery, InvitationComment


# Create your views here.
def InvitaionCreate(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            baseinfolist = InvitationInfo.objects.filter(user=request.user)

            greetinglist = InvitationGreetingsInfo.objects.filter(user=request.user)
            failylist = InvitaionFamilyInfo.objects.filter(user=request.user)
            locationlist = InvitationLocationInfo.objects.filter(user=request.user)
            contactlist = InvitationContactInfo.objects.filter(user=request.user)
            accountlist = InvitationAccountInfo.objects.filter(user=request.user)
            gallerylist = InvitationGallery.objects.filter(user=request.user)

            if len(baseinfolist) == 0:
                baseinfo = InvitationInfo()
            else:
                baseinfo = baseinfolist[0]

            if len(greetinglist) == 0:
                greetinginfo = InvitationGreetingsInfo()
            else:
                greetinginfo = greetinglist[0]

            if len(failylist) == 0:
                failyinfo = InvitaionFamilyInfo()
            else:
                failyinfo = failylist[0]

            if len(locationlist) == 0:
                locationinfo = InvitationLocationInfo()
            else:
                locationinfo = locationlist[0]

            if len(contactlist) == 0:
                contactinfo = InvitationContactInfo()
            else:
                contactinfo = contactlist[0]

            if len(accountlist) == 0:
                accountinfo = InvitationAccountInfo()
            else:
                accountinfo = accountlist[0]

            if len(accountlist) == 0:
                accountinfo = InvitationAccountInfo()
            else:
                accountinfo = accountlist[0]

            baseinfo.set(request)
            greetinginfo.set(request)
            failyinfo.set(request)
            locationinfo.set(request)
            contactinfo.set(request)
            accountinfo.set(request)

            baseinfo.save()
            greetinginfo.save()
            failyinfo.save()
            locationinfo.save()
            contactinfo.save()
            accountinfo.save()

            images = request.FILES.getlist('gallery_images')  # 다수의 이미지 가져오기
            print(f"images count: {len(images)}")
            if len(images) > 0:
                for galleryitem in gallerylist:
                    galleryitem.delete()
                #gallerylist = []
                for image in images:
                    galleryitem = InvitationGallery(user=request.user, image=image)
                    try:
                        galleryitem.save()
                        image_url = galleryitem.image.url if galleryitem.image else "URL not available"
                    except Exception as e:
                        print(f"Error saving image: {e}")
                        image_url = "Error saving image"

                    # gallerylist.append({
                    #     'id': galleryitem.id,
                    #     'image': galleryitem.image,
                    # })

            # context = {
            #     'greetingform': GreetingsViewForm(instance=greetinginfo),
            #     'locationform': LocationViewForm(instance=locationinfo),
            #
            #     'baseinfo': baseinfo,
            #     'greetinginfo': greetinginfo,
            #     'failyinfo': failyinfo,
            #     'locationinfo': locationinfo,
            #     'contactinfo': contactinfo,
            #     'accountinfo': accountinfo,
            #     'gallerylist': gallerylist
            # }
            #
            # if len(gallerylist) != 0:
            #     context['maingalleryimage'] = gallerylist[0]
            # return render(request, 'invitationapp/create.html', context)
            return redirect('invitationapp:create')

        else:
            baseinfolist = InvitationInfo.objects.filter(user=request.user)
            greetinglist = InvitationGreetingsInfo.objects.filter(user=request.user)
            failylist = InvitaionFamilyInfo.objects.filter(user=request.user)
            locationlist = InvitationLocationInfo.objects.filter(user=request.user)
            contactlist = InvitationContactInfo.objects.filter(user=request.user)
            accountlist = InvitationAccountInfo.objects.filter(user=request.user)
            gallerylist = InvitationGallery.objects.filter(user=request.user)

            if len(baseinfolist) != 0:
                baseinfo = baseinfolist[0]
            else:
                baseinfo = None

            if len(greetinglist) != 0:
                greetinginfo = greetinglist[0]
            else:
                greetinginfo = None

            if len(failylist) != 0:
                failyinfo = failylist[0]
            else:
                failyinfo = None

            if len(locationlist) != 0:
                locationinfo = locationlist[0]
            else:
                locationinfo = None

            if len(contactlist) != 0:
                contactinfo = contactlist[0]
            else:
                contactinfo = None

            if len(accountlist) != 0:
                accountinfo = accountlist[0]
            else:
                accountinfo = None

            context = {
                'greetingform': GreetingsViewForm(instance=greetinginfo),
                'locationform': LocationViewForm(instance=locationinfo),

                'baseinfo': baseinfo,
                'greetinginfo': greetinginfo,
                'failyinfo': failyinfo,
                'locationinfo': locationinfo,
                'contactinfo': contactinfo,
                'accountinfo': accountinfo,
                'gallerylist': gallerylist
            }
            if len(gallerylist) != 0:
                context['maingalleryimage'] = gallerylist[0]
            return render(request, 'invitationapp/create.html', context)
    else:
        return redirect('accountapp:login')


def InvitaionEdit(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":

            husband_name_en = request.POST['husband_name_en']

            print(husband_name_en)

            return HttpResponseRedirect(reverse('invitationapp:edit', args=[request.user.pk]))
        else:
            return render(request, 'invitationapp/edit.html')
    else:
        return redirect('accountapp:login')


def InvitationDetailView(request, pk):
    baseinfolist = InvitationInfo.objects.filter(user=pk)
    greetinglist = InvitationGreetingsInfo.objects.filter(user=pk)
    failylist = InvitaionFamilyInfo.objects.filter(user=pk)
    locationlist = InvitationLocationInfo.objects.filter(user=pk)
    contactlist = InvitationContactInfo.objects.filter(user=pk)
    accountlist = InvitationAccountInfo.objects.filter(user=pk)
    gallerylist = InvitationGallery.objects.filter(user=pk)

    commentlist = InvitationComment.objects.filter(user=pk)

    if len(baseinfolist) != 0:
        baseinfo = baseinfolist[0]
    else:
        baseinfo = None

    if len(greetinglist) != 0:
        greetinginfo = greetinglist[0]
    else:
        greetinginfo = None

    if len(failylist) != 0:
        failyinfo = failylist[0]
    else:
        failyinfo = None

    if len(locationlist) != 0:
        locationinfo = locationlist[0]
    else:
        locationinfo = None

    if len(contactlist) != 0:
        contactinfo = contactlist[0]
    else:
        contactinfo = None

    if len(accountlist) != 0:
        accountinfo = accountlist[0]
    else:
        accountinfo = None

    # 페이지네이터 생성 (5개씩 표시)
    paginator = Paginator(commentlist, 3)
    page_number = request.GET.get('page')  # URL의 'page' 파라미터 가져오기
    page_obj = paginator.get_page(page_number)  # 해당 페이지의 객체 가져오기

    context = {
        'baseinfo': baseinfo,
        'greetinginfo': greetinginfo,
        'failyinfo': failyinfo,
        'locationinfo': locationinfo,
        'contactinfo': contactinfo,
        'accountinfo': accountinfo,
        'gallerylist': gallerylist,
        'commentlist': commentlist,
        'pk': pk,
        'page_obj': page_obj
    }
    if len(gallerylist) != 0:
        context['maingalleryimage'] = gallerylist[0]

    context['isWatermark'] = False

    print(gallerylist.first())
    return render(request, 'invitationapp/invitation.html', context)


def InvitationCreateComment(request, pk):
    commentInfo = InvitationComment()
    user = User.objects.filter(id=pk).first()
    commentInfo.set(request, user)
    commentInfo.save()

    return HttpResponseRedirect(reverse('invitationapp:invitation', args=[pk]))


def InvitationDeleteComment(request, pk):
    if request.method == 'POST':
        cid = request.POST.get("comment_id")
        password = request.POST.get("password")

        print(cid)
        print(password)

        commentInfo = InvitationComment.objects.filter(id=cid).first()
        if commentInfo.user != request.user:
            if commentInfo.password != password:
                messages.error(request, "비밀번호가 올바르지 않습니다.")
                return HttpResponseRedirect(request.path)

        commentInfo.delete()
        messages.success(request, "방명록이 삭제되었습니다.")

    return HttpResponseRedirect(reverse('invitationapp:invitation', args=[pk]))

#class InvitationCreateView(CreateView):
#    model = InvitationInfo
#    form_class = CreateViewForm
#    success_url = reverse_lazy("invitationapp:edit")
#    template_name = "invitationapp/create.html"

#    def __get__(self, request, *args, **kwargs):
#        return render(request, self.template_name)


#class InvitationDetailView(DetailView):
#    model = User
#    context_object_name = 'target_info'
#    template_name = 'invitation/invitation.html'
