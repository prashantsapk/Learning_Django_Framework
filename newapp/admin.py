from django.contrib import admin
from .models import Newappvarity,store,ChaiReview,ChaiCertificate

# Register your models here.


class ChaiReviewinline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added')
    inlines=[ChaiReviewinline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal=('chai_varities',)


class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')


admin.site.register(Newappvarity,ChaiVarietyAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)
admin.site.register(store,StoreAdmin)
