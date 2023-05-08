from django import forms
from .models import Department
from django.core.exceptions import ValidationError

#
class DateInput(forms.DateInput):
    input_type = "date"
    
    
class AddTimeSlot(forms.Form):
    TIME_CHOICES = (
    ("8 AM", "8 AM"),
    ("8:30 AM", "8:30 AM"),
    ("9 AM", "9 AM"),
    ("9:30 AM", "9:30 AM"),
    ("10 AM", "10 AM"),
    ("10:30 AM", "10:30 AM"),
    ("11 AM", "11 AM"),
    ("11:30 AM", "11:30 AM"),
    ("12 PM", "12 PM"),
    ("12:30 PM", "12:30 PM"),
    ("1 PM", "1 PM"),
    ("1:30 PM", "1:30 PM"),
    ("2 PM", "2 PM"),
    ("2:30 PM", "2:30 PM"),
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
    )
    
    POST_GRADUATE_TIME = (
    ("8 AM - 9 AM", "8 AM - 9 AM"),
    ("9 AM - 10 AM", "9 AM - 10 AM"),
    ("10 AM - 11 AM", "10 AM - 11 AM"),
    ("11 AM - 12 PM", "11 AM - 12 PM"),
    ("12 PM - 1 PM", "12 PM - 1 PM"),
    ("1 PM - 2 PM", "1 PM - 2 PM"),
    ("2 PM - 3 PM", "2 PM - 3 PM"),
    ("3 PM - 4 PM", "3 PM - 4 PM"),
    ("4 PM - 5 PM", "4 PM - 5 PM"),
    ("5 PM - 6 PM", "5 PM - 6 PM"),
)
    Education_level = (
        ('undergraduate', 'undergraduate'),
        ('postgraduate', 'postgraduate'),
    )
    slot_date=forms.DateField(label="Date", widget=DateInput(attrs={"class":"form-control"}))
    education_level=forms.ChoiceField(label="Education Level", choices=Education_level, widget=forms.Select(attrs={"class":"form-control","id":"levels"}))
    undergraduate_time=forms.ChoiceField(label="Undergraduate Time Slot", choices=TIME_CHOICES, widget=forms.Select(attrs={"class":"form-control", "id":"under_graduate"}))
    postgraduate_time=forms.ChoiceField(label="Postgraduate Time Slot", choices=POST_GRADUATE_TIME, widget=forms.Select(attrs={"class":"form-control",  "id":"post_graduate"}))
    
class AddDepartment(forms.Form):
    Department_Choices = (
        ("Department of Computer Science & Engineering (CSE)", "Department of Computer Science & Engineering (CSE)"),
        ("Department of Electronics and Telecommunication Engineering (ETE)", "Department of Electronics and Telecommunication Engineering (ETE)"),
        )
    department_name = forms.ChoiceField(label="Department name", choices=Department_Choices, widget=forms.Select(attrs={"class":"form-control"}))
    
    def clean_department_name(self):
        name = self.cleaned_data.get("department_name")
        if not name:
            raise ValidationError("Department name can not be empty.")
        if Department.objects.filter(department_name=name).exists():
            raise ValidationError('This field already exists.')
        return name
    