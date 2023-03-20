from django import forms

from Users.models import CustomUser


def validate_national_code(value):
    if len(value) != 10:
        raise forms.ValidationError("National code must be 10 digits")


def validate_full_name(value):
    if len(value.split(" ")) != 2:
        raise forms.ValidationError("Full name must be in format: 'first_name last_name'")
    if not value.split(" ")[0].istitle() and not value.split(" ")[1].istitle():
        raise forms.ValidationError("First name must be in title format")


class CustomUserForm(forms.ModelForm):
    national_code = forms.CharField(validators=[validate_national_code])
    full_name = forms.CharField(validators=[validate_full_name])

    class Meta:
        model = CustomUser
        fields = [
            'username', "full_name", "gender", "national_code",
            "birthday_date", "ceremony_datetime", "country",
        ]
