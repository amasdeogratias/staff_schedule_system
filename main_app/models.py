from django.contrib.auth.models import AbstractUser
from django.db import models
from  django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
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

class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Staff"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)
    
class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
class Department(models.Model):
    id=models.AutoField(primary_key=True)
    department_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    

class Blocks(models.Model):
    id = models.AutoField(primary_key=True)
    block_name = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.block_name

class Office(models.Model):
    id = models.AutoField(primary_key=True)
    block = models.ForeignKey(Blocks, on_delete=models.CASCADE)
    office_number = models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table='main_app_offices'
    
class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    office = models.ForeignKey(Office,on_delete=models.CASCADE)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
       
    
class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    course_code=models.CharField(max_length=255)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
     
    
class Students(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    student_id=models.CharField(max_length=255, unique=True, blank=False)
    program=models.CharField(max_length=255,default='')
    gender=models.CharField(max_length=255)
    profile_pic=models.FileField()
    session_start_year=models.DateField()
    session_end_year=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
class TimeSlot(models.Model):
    staff=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    slot_date = models.DateField()
    time=models.CharField(max_length=10, choices=TIME_CHOICES,default="")
    status = models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
   

    class Meta:
        db_table='time_slots'
        
class Appointment(models.Model):
    id=models.AutoField(primary_key=True)
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=10, choices=TIME_CHOICES, default="")
    staffId=models.PositiveIntegerField(null=True)
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=40,null=True)
    status = models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "appointments"
    
        
   
@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance,address="", department=Department.objects.get(id=1))
        if instance.user_type == 3:
            Students.objects.create(admin=instance,session_start_year="2020-01-01",session_end_year="2021-01-01",profile_pic="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.staffs.save()
    if instance.user_type==3:
        instance.students.save()