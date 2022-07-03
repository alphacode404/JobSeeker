from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField



class Profile(models.Model):
    EMPLOYMENT_STATUS =(
        ('EMPLOYED', 'Employed'),
        ('UNEMPLOYED', 'Unemployed')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200, default='')
    profile_pic = models.ImageField( upload_to='profile_pics', default="defaultprofile.jpg")
    age = models.IntegerField(null=True)
    email = models.EmailField(default='')
    biography = models.CharField(max_length=500, default='')
    country = CountryField('Country', blank_label='(select country)', null=True)
    twitter = models.CharField(max_length=500, default='')
    instagram = models.CharField(max_length=500, default='')
    linkedin = models.CharField(max_length=500, default='')
    facebook = models.CharField(max_length=500, default='')
    employment_status = models.CharField(max_length=200, choices=EMPLOYMENT_STATUS, default=EMPLOYMENT_STATUS[:0])
    occupation = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200, default='')
    
  
   

    def __str__(self):
        return str(self.user)


class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.FileField(upload_to='companylogo', default='companydefault.jpg')
    website = models.CharField(max_length=500, default='')


    class Meta:
        verbose_name='Company'
        verbose_name_plural = 'Companies'

        

    def __str__(self):
        return self.name



class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    salary = models.IntegerField(default=0)
 

    class Meta:
        verbose_name='Job'
        verbose_name_plural = 'Jobs'
        

    def __str__(self):
        return self.name





class Applicant(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField('Date of Birth')
    job = models.ManyToManyField(Job, related_name='applicant')





    class Meta:
        verbose_name='Applicant'
        verbose_name_plural = 'Applicants'
        


    def __str__(self):
        return self.name

