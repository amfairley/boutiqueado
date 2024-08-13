
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    # Tell DJango which model it relates to
    class Meta:
        model = Order
        # Fields we want to render (no automatically calculated ones)
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    # Overwrite init
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        # Init method to set the form as it should be by default
        super().__init__(*args, **kwargs)
        # Template for input displays
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Autofocus so that the cursor is already here
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # Iterate through, add star for required, set placeholder to above
        # Defined ones, add css class
        # Remove form field labels (now we have placeholders set)
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
