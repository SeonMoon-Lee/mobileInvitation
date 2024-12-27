from django.contrib import admin

from invitationapp.models import InvitationInfo, InvitationGreetingsInfo, InvitaionFamilyInfo, InvitationLocationInfo, \
    InvitationContactInfo, InvitationAccountInfo, InvitationGallery, InvitationComment

# Register your models here.

admin.site.register(InvitationInfo)
admin.site.register(InvitationGreetingsInfo)
admin.site.register(InvitaionFamilyInfo)
admin.site.register(InvitationLocationInfo)
admin.site.register(InvitationContactInfo)
admin.site.register(InvitationAccountInfo)
admin.site.register(InvitationGallery)
admin.site.register(InvitationComment)