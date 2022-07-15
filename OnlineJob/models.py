from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
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
    twitter = models.CharField(max_length=500, default='', blank=True)
    instagram = models.CharField(max_length=500, default='', blank=True)
    linkedin = models.CharField(max_length=500, default='', blank=True)
    facebook = models.CharField(max_length=500, default='', blank=True)
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

    # def get_absolute_url(self):
    #     return reverse('job:detail', kwargs={
    #         'job_pk': self.id
    #     })


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField('Date of Birth')
    job = models.ForeignKey(Job, on_delete=models.CASCADE )
    document = models.FileField(upload_to='resumes/%Y%m%d')
    submissiondate = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user)



# class Application(models.Model):


#     STATUS = (
#         ('Pending', "Pending"),
#         ('Passed', 'Passed'),
#         ('Rejected', 'Rejected')
#     )

#     name = models.ForeignKey(Applicant, on_delete=models.CASCADE)
#     jobname = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='applicant', null=True)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
#     status = models.CharField(max_length=50, choices=STATUS, default=STATUS[0:1])


#     class Meta:
#         verbose_name='Application'
#         verbose_name_plural = 'Applications'
        


#     def __str__(self):
#         return self.name



class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200, default='')
    position = models.CharField(max_length=200, default='')
    date = models.DateTimeField(auto_now=True)
    text = models.TextField(default='')
    document = models.FileField(upload_to='documents/%Y%m%d', blank=True)


    class Meta:
        verbose_name = "Note"
        verbose_name_plural = 'Notes'


    def __str__(self):
        return str(self.user)


class ControlPanel(models.Model):

    STATUS = (
        ('Pending', "Pending"),
        ('Passed', 'Passed'),
        ('Rejected', 'Rejected')
    )

    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS)
    resume = models.ForeignKey(Note, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        verbose_name = "Control Panel"
        verbose_name_plural = " Control Panels"


    def __str__(self):
        return str(self.applicant)