from django.contrib import admin
from .forms import BookingPeriodForm, PeriodFormSet
from .models import Banner, BookingPeriod, PricePeriod

class BookingPeriodInline(admin.StackedInline):
    model = BookingPeriod
    form = BookingPeriodForm
    formset = PeriodFormSet
    extra = 0

class PricePeriodInline(admin.StackedInline):
    model = PricePeriod
    formset = PeriodFormSet
    extra = 0

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    inlines = [BookingPeriodInline, PricePeriodInline]
