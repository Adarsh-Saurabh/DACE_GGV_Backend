from django.db import models

# Create your models here.
class Login(models.Model):
    emailId = models.EmailField(max_length=100)
    # password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    phone_no = models.IntegerField()
    profile = models.FileField(upload_to='profile_pics/')
    signature = models.FileField(upload_to='signature_pics/')
    caste_certificate = models.FileField(upload_to='category/caste_certificate/')
    qualification = models.FileField(upload_to='qualification/')
    registration_no = models.CharField(max_length=50)
    


    def __str__(self):
        return self.name



