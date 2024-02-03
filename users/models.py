from django.db import models
from django.db.models import Q

# Create your models here.

class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.name} - {self.description}'
    
class UserRecord(models.Model):
    SUPER_ADMIN = 1
    SUB_ADMIN = 2
    WORKER = 3
    CUSTOMER = 4
    USER_TYPES = [
        (SUPER_ADMIN, 'Super_admin'),
        (SUB_ADMIN, 'Sub_admin'),
        (WORKER, 'Worker'),
        (CUSTOMER, 'Customer'),
    ]
    name = models.CharField(max_length=100,null=True,blank=True)
    username = models.OneToOneField('auth.User',on_delete=models.CASCADE,related_name='associated_user',null=True,blank=True)
    phoneNo = models.CharField(max_length=10,null=True,blank=True)
    image = models.URLField(null=True,blank=True)
    address = models.TextField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(default = "Tamilnadu",max_length=100,null=True,blank=True)
    area = models.CharField(max_length=100,blank=True,null=True)
    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
    is_active = models.BooleanField(default=False)  
    user_type = models.PositiveSmallIntegerField(choices = USER_TYPES, default = 4)
    subadmin = models.ForeignKey('Subadmins', on_delete=models.CASCADE, blank=True, null=True)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f'{self.name}'

    
class Subadmins(models.Model):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    DAYS_CHOICES = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]

    company_name = models.CharField(max_length=100,null=True,blank=True)
    company_description = models.TextField(null=True,blank=True)
    user = models.ForeignKey(UserRecord, on_delete=models.CASCADE,limit_choices_to={'user_type': 2})
    company_address = models.CharField(max_length=100,null=True,blank=True)
    company_city = models.CharField(max_length=100,null=True,blank=True)
    company_state = models.CharField(max_length=100)
    company_area = models.CharField(max_length=100)
    company_image = models.URLField(null=True,blank=True)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, blank=True, null=True)
    working_hrs = models.IntegerField(null=True,blank=True)
    holidays = models.PositiveSmallIntegerField(choices=DAYS_CHOICES,default=None,null=True,blank=True)

    def __str__(self):
        return f'{self.company_name} - {self.company_address}'
    

    
class ratings_reviews(models.Model):
    company = models.ForeignKey(Subadmins, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    
    def __str__(self):
        return f'{self.user} - {self.subadmin}'
    

class problem(models.Model):
    MORNING = 1
    MIDMORNING = 2
    AFTERNOON = 3
    MIDAFTERNOON = 4
    EVENING = 5
    NIGHT = 6
    TIME_CHOICES = [
        (MORNING, '9:00 AM - 11:00 AM'),
        (MIDMORNING, '11:00 AM - 1:00 PM'),
        (AFTERNOON, '1:00 PM - 3:00 PM'),
        (MIDAFTERNOON, '3:00 PM - 5:00 PM'),
        (EVENING, '5:00 PM - 7:00 PM'),
        (NIGHT, '7:00 PM - 9:00 PM'),

    ]

    date = models.DateField(null=True,blank=True)
    problem_discription = models.TextField(null=True,blank=True)
    time = models.PositiveSmallIntegerField(choices=TIME_CHOICES,default=None,null=True,blank=True)
    customer = models.ForeignKey(UserRecord, on_delete=models.CASCADE,limit_choices_to={'user_type': 4},null=True,blank=True)
    company_name = models.ForeignKey(Subadmins, on_delete=models.CASCADE,null=True,blank=True)
    tagged_worker = models.ForeignKey(UserRecord,related_name="tagged_to", on_delete=models.CASCADE,limit_choices_to={'user_type': 3},null=True,blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.company_name} - {self.customer}'