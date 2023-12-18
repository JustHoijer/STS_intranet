import django
from django.contrib import admin

django.setup()
from .models import Carousel, Slide


# Register your models here.


class SlideInLineAdmin(admin.TabularInline):
    model = Slide


class CarouselAdmin(admin.ModelAdmin):
    inlines = [SlideInLineAdmin]


admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Slide)
