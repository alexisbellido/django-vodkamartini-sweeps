from django import forms
#from django.core.urlresolvers import reverse
from .models import Sweep, SweepEntry

class SweepEntryForm(forms.Form):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField()
    date_of_birth = forms.DateField(required=True)
    zip_code = forms.CharField(max_length=10, required=True)
    gender = forms.ChoiceField(choices=[(0, 'Choose your gender')] + SweepEntry.GENDER_CHOICES)
    receive_email = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        """
        Notice how we need to call __init__ from superclass first, if we don't do this
        then we won't be able to access attributes such as fields and instance.
        """
        super(SweepEntryForm, self).__init__(*args, **kwargs)
        if self.initial:
            self.sweep = self.initial['sweep']

    def save(self):
        # TODO one entry per day , sweepentry = SweepEntry.objects.get(pk=self.quiz_id)
        # TODO date_of_birth using nicer widget
        sweepentry = SweepEntry(
                        sweep=self.sweep,
                        first_name=self.cleaned_data['first_name'],
                        last_name=self.cleaned_data['last_name'],
                        email=self.cleaned_data['email'],
                        date_of_birth=self.cleaned_data['date_of_birth'],
                        zip_code=self.cleaned_data['zip_code'],
                        gender=self.cleaned_data['gender'],
                        receive_email=self.cleaned_data['receive_email'],
                     )

        sweepentry.save()
        return sweepentry

    def clean_gender(self):
        value = self.cleaned_data["gender"]
        if value == '0':
            raise forms.ValidationError("Please choose your gender")
        return value

    #def clean(self):
    #    cleaned_data = super(SweepEntryForm, self).clean()
    #    print "receive email", cleaned_data["receive_email"]
    #    raise forms.ValidationError("Did not send for 'help' in the subject despite CC'ing yourself.")
    #    return cleaned_data
