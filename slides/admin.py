from django.contrib import admin
from .models import Presentation, Slide, FeedBack


# Register your models here.
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email', 'agreement', 'suggestion',
                    'comment', 'slide', 'presentation']
    list_filter = ['mobile', 'agreement', 'slide', 'slide__presentation']
    search_fields = ['name', 'mobile', 'email', ]

    def presentation(self, obj):
        return obj.slide.presentation


class PresentationAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']
    list_filter = ['author']


class SlideAdmin(admin.ModelAdmin):
    list_display = ['name', 'presentation']
    list_filter = ['presentation']


admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(FeedBack, FeedBackAdmin)
