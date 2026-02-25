from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Newappvarity(models.Model):
    CHAI_TYPE_CHOICE =[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ]
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='newapp/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description=models.TextField(default="",blank=True)

    def __str__(self):
        return self.name
    
# one to many model
class ChaiReview(models.Model):
    chai = models.ForeignKey(Newappvarity,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment= models.TextField()
    date_added = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'   


# Many to Many, there can many stores and many items 


class store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varities= models.ManyToManyField(Newappvarity,related_name='stores')

    def __str__(self):
        return self.name
    

# one to one method

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(Newappvarity,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.chai}'
    