import datetime
import os
from io import BytesIO

from PIL import Image
from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from django.utils.timezone import now


# Create your models here.
def GetTitleImagePath(instance, filename):
    return 'res/image/{0}/{1}'.format(instance.user.username, filename)


def GetGalleryImagePath(instance, filename):
    return 'res/image/{0}/gallery/{1}'.format(instance.user.username, filename)


class InvitationInfo(models.Model):
    # 신랑 위치(장남 등)
    # 신부 위치(장녀 등)
    # 기본정보

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)

    husband_name_en = models.CharField(max_length=16, blank=True)

    husband_firstname = models.CharField(max_length=16, blank=True)
    husband_lastname = models.CharField(max_length=4, blank=True)
    husband_pos = models.CharField(max_length=4, blank=True)

    wife_name_en = models.CharField(max_length=16, blank=True)

    wife_firstname = models.CharField(max_length=16, blank=True)
    wife_lastname = models.CharField(max_length=4, blank=True)
    wife_pos = models.CharField(max_length=4, blank=True)

    title_image = models.ImageField(upload_to=GetTitleImagePath, blank=True)
    wedding_datetime = models.DateTimeField(blank=True)

    def set(self, request):
        self.user = request.user

        self.husband_name_en = request.POST["husband_name_en"]

        self.husband_firstname = request.POST["husband_firstname"]
        self.husband_lastname = request.POST["husband_lastname"]
        self.husband_pos = request.POST["husband_pos"]

        self.wife_name_en = request.POST["wife_name_en"]

        self.wife_firstname = request.POST["wife_firstname"]
        self.wife_lastname = request.POST["wife_lastname"]
        self.wife_pos = request.POST["wife_pos"]




        if request.FILES.get("title_image"):
            if self.title_image:
                if os.path.isfile(self.title_image.path):
                    os.remove(self.title_image.path)
            self.title_image = request.FILES["title_image"]

        if request.POST.get("wedding_datetime"):
            self.wedding_datetime = request.POST["wedding_datetime"]
            print(self.wedding_datetime)
        elif self.wedding_datetime is None:
            self.wedding_datetime = now()
            print(self.wedding_datetime)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        #self.title_image = compress_image(self.title_image,512)

        super().save(*args, **kwargs)



class InvitationGreetingsInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=128, blank=True)
    greetings = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return self.user.username

    def set(self, request):
        self.user = request.user
        self.title = request.POST["title"]
        self.greetings = request.POST["greetings"]


class InvitaionFamilyInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    husband_father_name = models.CharField(max_length=16, blank=True)
    husband_mother_name = models.CharField(max_length=16, blank=True)
    husband_father_isdead = models.BooleanField(default=False, blank=True)
    husband_mother_isdead = models.BooleanField(default=False, blank=True)

    wife_father_name = models.CharField(max_length=16, blank=True)
    wife_mother_name = models.CharField(max_length=16, blank=True)
    wife_father_isdead = models.BooleanField(default=False, blank=True)
    wife_mother_isdead = models.BooleanField(default=False, blank=True)

    chrysanthemum_display = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.user.username

    def set(self, request):
        self.user = request.user
        self.husband_father_name = request.POST["husband_father_name"]
        self.husband_mother_name = request.POST["husband_mother_name"]

        self.husband_father_isdead = request.POST.get('husband_father_isdead') == 'on'
        self.husband_mother_isdead = request.POST.get('husband_mother_isdead') == 'on'

        self.wife_father_name = request.POST["wife_father_name"]
        self.wife_mother_name = request.POST["wife_mother_name"]

        self.wife_father_isdead = request.POST.get('wife_father_isdead') == 'on'
        self.wife_mother_isdead = request.POST.get('wife_mother_isdead') == 'on'

        if request.POST.get("chrysanthemum_display") == '(故)':
            self.chrysanthemum_display = False
        else:
            self.chrysanthemum_display = True


class InvitationLocationInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    location = models.TextField(max_length=256, blank=True)

    address = models.TextField(max_length=256, blank=True)

    weddinghall_name = models.CharField(max_length=32, blank=True)
    floor_or_hall = models.CharField(max_length=32, blank=True)
    weddinghall_tel = models.CharField(max_length=16, blank=True)

    transportation = models.TextField(max_length=1024, blank=True, null=True)
    #
    # subway = models.TextField(max_length=1024, blank=True, null=True)
    # bus = models.TextField(max_length=1024, blank=True, null=True)
    # car = models.TextField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def set(self, request):
        self.user = request.user
        #self.location = request.POST["location_1"]
        self.address = request.POST["location_2"]
        self.weddinghall_name = request.POST["location_3"]
        #self.floor_or_hall = request.POST["floor_or_hall"]
        #self.weddinghall_tel = request.POST["weddinghall_tel"]
        self.transportation = request.POST["transportation"]


class InvitationContactInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    husband_tel = models.CharField(max_length=16, blank=True)
    husband_father_tel = models.CharField(max_length=16, blank=True)
    husband_mother_tel = models.CharField(max_length=16, blank=True)
    wife_tel = models.CharField(max_length=16, blank=True)
    wife_father_tel = models.CharField(max_length=16, blank=True)
    wife_mother_tel = models.CharField(max_length=16, blank=True)
    notice = models.TextField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def set(self, request):
        self.user = request.user
        self.husband_tel = request.POST["husband_tel"]
        self.husband_father_tel = request.POST["husband_father_tel"]
        self.husband_mother_tel = request.POST["husband_mother_tel"]

        self.wife_tel = request.POST["wife_tel"]
        self.wife_father_tel = request.POST["wife_father_tel"]
        self.wife_mother_tel = request.POST["wife_mother_tel"]

        #self.notice = request.POST["notice"]


class InvitationAccountInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    # 은행종류
    BANK_TYPE = [
        '신한은행'
        '국민은행'
        '우리은행'
        '하나은행'
    ]
    husband_bank = models.CharField(max_length=8, blank=True)
    husband_account = models.CharField(max_length=32, blank=True)
    husband_depositor = models.CharField(max_length=32, blank=True)

    husband_father_bank = models.CharField(max_length=8, blank=True)
    husband_father_account = models.CharField(max_length=32, blank=True)
    husband_father_depositor = models.CharField(max_length=32, blank=True)

    husband_mother_bank = models.CharField(max_length=8, blank=True)
    husband_mother_account = models.CharField(max_length=32, blank=True)
    husband_mother_depositor = models.CharField(max_length=32, blank=True)

    wife_bank = models.CharField(max_length=8, blank=True)
    wife_account = models.CharField(max_length=32, blank=True)
    wife_depositor = models.CharField(max_length=32, blank=True)

    wife_father_bank = models.CharField(max_length=8, blank=True)
    wife_father_account = models.CharField(max_length=32, blank=True)
    wife_father_depositor = models.CharField(max_length=32, blank=True)

    wife_mother_bank = models.CharField(max_length=8, blank=True)
    wife_mother_account = models.CharField(max_length=32, blank=True)
    wife_mother_depositor = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.user.username

    def set(self, request):
        self.user = request.user
        self.husband_account = request.POST["husband_account"]
        self.husband_bank = request.POST["husband_bank"]
        self.husband_depositor = request.POST["husband_depositor"]

        self.husband_father_account = request.POST["husband_father_account"]
        self.husband_father_bank = request.POST["husband_father_bank"]
        self.husband_father_depositor = request.POST["husband_father_depositor"]

        self.husband_mother_account = request.POST["husband_mother_account"]
        self.husband_mother_bank = request.POST["husband_mother_bank"]
        self.husband_mother_depositor = request.POST["husband_mother_depositor"]

        self.wife_account = request.POST["wife_account"]
        self.wife_bank = request.POST["wife_bank"]
        self.wife_depositor = request.POST["wife_depositor"]

        self.wife_father_account = request.POST["wife_father_account"]
        self.wife_father_bank = request.POST["wife_father_bank"]
        self.wife_father_depositor = request.POST["wife_father_depositor"]

        self.wife_mother_account = request.POST["wife_mother_account"]
        self.wife_mother_bank = request.POST["wife_mother_bank"]
        self.wife_mother_depositor = request.POST["wife_mother_depositor"]


class InvitationGallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to=GetGalleryImagePath, blank=True)

    def __str__(self):
        return "{0}_{1}".format(self.user.username, self.image)

    def set(self, request, imagepath):
        self.user = request.user
        self.image = imagepath

    def save(self, *args, **kwargs):
        #self.image = compress_image(self.image,512)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # 이미지 파일 삭제
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

def compress_image(image, width):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img_output = BytesIO()

    src_width, src_height = img.size
    src_ratio = float(src_height) / float(src_width)
    dst_height = round(src_ratio * width)

    img = img.resize((width, dst_height))

    img.save(img_output, 'JPEG', quality=80)
    compressed_image = File(img_output, name=image.name)
    return compressed_image