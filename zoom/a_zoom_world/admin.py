from django.contrib import admin
from .models import *
# Register your models here.
#
admin.site.register(DomicileType)
admin.site.register(Address)

admin.site.register(Amenity)
admin.site.register(PotentialAllergen)
admin.site.register(Property)
admin.site.register(NeedException)
admin.site.register(AccessibilityNeed)
admin.site.register(Vehicle)
admin.site.register(PropertyNeed)
admin.site.register(ZoomUser)


class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('image_object',)


admin.site.register(Photo, PhotoAdmin)
