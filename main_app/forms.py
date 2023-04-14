from django import forms
from .models import TimeSlot

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
    slot_date=forms.DateField(label="Date", widget=DateInput(attrs={"class":"form-control"}))
    time=forms.ChoiceField(label="Time Slot", choices=TIME_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    
class AddDepartment(forms.Form):
    Department_Choices = (
        ("Department of Computer Science & Engineering (CSE)"),
        ("Department of Electronics and Telecommunication Engineering (ETE)"),
        )
    department_name = forms.CharField(label="Department name", choices=Department_Choices, widget=forms.Select(attrs={"class":"form-control"}))