from django import forms

from weddingapp.models import Guest


class ExtraForm(forms.ModelForm):
    diet = forms.CharField(max_length=128,
                           help_text="Please enter any dietary requirements for :",
                           required=False)
    transport = forms.BooleanField(
        initial=False,
        help_text="Would /guest name/ be interested in transport from the church to the reception?",
        required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Guest
        fields = ('diet', 'transport')