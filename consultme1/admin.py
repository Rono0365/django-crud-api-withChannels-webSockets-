from django.contrib import admin
from unicodedata import category
from consultme1.models import *

admin.site.register(Client)
admin.site.register(lawyer)
admin.site.register(lawfirm)
admin.site.register(Categry)
admin.site.register(verified)
admin.site.register(rating)
admin.site.register(active)
admin.site.register(ProfilePicture)