from django import forms

from .models import Customers


class ReportForm(forms.Form):

    download_as_csv = forms.BooleanField(
        label="Download Report",
        help_text="Generates a CSV file that you can download.",
        required=False,
    )
