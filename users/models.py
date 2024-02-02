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
    name = models.CharField(max_length=100)
    username = models.OneToOneField('auth.User', on_delete=models.CASCADE,related_name="associated_user")
    phoneNo = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/')
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(default = "Tamilnadu",max_length=100)
    area = models.CharField(max_length=100,blank=True,null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_active = models.BooleanField(default=False)
    user_type = models.PositiveSmallIntegerField(choices = USER_TYPES, default = 1)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f'{self.name} - {self.email}'
    
    
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

    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    user = models.ForeignKey(UserRecord, on_delete=models.CASCADE,limit_choices_to={'user_type': 2})
    company_address = models.CharField(max_length=100)
    company_city = models.CharField(max_length=100)
    company_state = models.CharField(max_length=100)
    comapany_area = models.CharField(max_length=100)
    comapany_image = models.ImageField(upload_to='company_images')
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, blank=True, null=True)
    working_hrs = models.IntegerField()
    holidays = models.PositiveSmallIntegerField(choices=DAYS_CHOICES,default=None)

    def __str__(self):
        return f'{self.company_name} - {self.company_address}'
    
class ratings_reviews(models.Model):
    company = models.ForeignKey(Subadmins, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    
    def __str__(self):
        return f'{self.user} - {self.subadmin}'