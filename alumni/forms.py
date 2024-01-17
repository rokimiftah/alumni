from django import forms

from alumni.models import Alumni


class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = [
            "alumni_number",
            "first_name",
            "last_name",
            "email",
            "field_of_study",
            "gpa",
        ]
        labels = {
            "alumni_number": "Alumni Number",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "field_of_study": "Field of Study",
            "gpa": "GPA",
        }
        widgets = {
            "alumni_number": forms.NumberInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "field_of_study": forms.TextInput(attrs={"class": "form-control"}),
            "gpa": forms.NumberInput(attrs={"class": "form-control"}),
        }
