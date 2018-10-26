from django.contrib import admin
from .forms import PricePeriodForm, BookingPeriodForm, PeriodFormSet
from .models import Banner, BookingPeriod, PricePeriod

class BookingPeriodInline(admin.StackedInline):
    model = BookingPeriod
    form = BookingPeriodForm
    formset = PeriodFormSet
    extra = 0

class PricePeriodInline(admin.StackedInline):
    model = PricePeriod
    form = PricePeriodForm
    formset = PeriodFormSet
    extra = 0

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            self.inlines = []
        else:
            self.inlines = [BookingPeriodInline, PricePeriodInline]
        return super(BannerAdmin, self).get_form(request, obj, **kwargs)
