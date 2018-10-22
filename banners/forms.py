from django import forms
from .models import Banner, BookingPeriod, PricePeriod

def dates_overlap(startA,endA,startB,endB):
    '''
    Takes 4 required positional argumnets: start and end dates of event A and B
    respectively, and returns true if event A and event B dates_overlap
    '''
    return (startA <= endB) and (endA >= startB)

class BookingPeriodForm(forms.ModelForm):
    class Meta:
        model = BookingPeriod
        fields = "__all__"
    def clean(self):
        if not self.has_changed():
            return
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date > end_date:
            raise forms.ValidationError("Your start date must come before the end date!")
        banner = self.instance.banner
        for period in banner.bookingperiod_set.all():
            if dates_overlap(start_date, end_date,
                period.start_date, period.end_date):
                raise forms.ValidationError("Banner unavailable for this time period")
        return self.cleaned_data

class PeriodFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        for form in self.forms:
            if not form.has_changed():
                print("Not changed")
                continue
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            if any([dates_overlap(start_date,end_date,
                form_.cleaned_data.get('start_date'),form_.cleaned_data.get('end_date')) for form_ in self.forms if (form_.has_changed() and not form_ == form)]):
                print(form.instance)
                raise forms.ValidationError("Ensure that all date ranges are unique!")
