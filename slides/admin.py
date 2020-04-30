from django.contrib import admin
from .models import Presentation, Slide, FeedBack

# Register your models here.
admin.site.register(Presentation)
admin.site.register(Slide)
admin.site.register(FeedBack)
