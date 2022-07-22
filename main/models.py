from django.db import models
from main.helpers import video_upload_to,image_upload_to
from django.core.validators import MinValueValidator,MinLengthValidator
from account.models import User
from .validators import validate_video_extension,validate_minimum_size
from django.core.exceptions import ValidationError
class User(User):
    photo = models.ImageField(upload_to=video_upload_to,validators = [validate_minimum_size])
    
    
    


class Category(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0    
    name=models.CharField(max_length=100)
    text=models.TextField(max_length=255)
    background=models.ImageField(upload_to=image_upload_to,validators=[validate_minimum_size])
    status=models.SmallIntegerField(choices=(
        (STATUS_ACTIVE,"Active"),
        (STATUS_INACTIVE,"Inactive")
    ),default=STATUS_ACTIVE)


    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name


class Course(models.Model):    
    
    user = models.ManyToManyField(User)
    name=models.CharField(max_length=50,validators=[MinLengthValidator(6)])
    price=models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)])
    
    text = models.TextField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.RESTRICT)
    duration=models.CharField(max_length=10)
    rating = models.SmallIntegerField(validators=[MinValueValidator(0)])
    total_sold = models.IntegerField(default=0)
   
    class Meta:
        verbose_name='Course'
        verbose_name_plural='Courses'
    def __str__(self):
        return self.name
class Video(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0
    
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    video = models.FileField(upload_to=video_upload_to,validators=[validate_video_extension])
    image = models.ImageField(upload_to=image_upload_to,blank=True,validators=[validate_minimum_size])
    
    status = models.SmallIntegerField(choices=(
        (STATUS_ACTIVE, 'ACTIVE'),
        (STATUS_INACTIVE,'INACTIVE')
    ),default=STATUS_INACTIVE)
 

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.RESTRICT)
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=255)
    




class Card(models.Model):
    def only_int(value): 
        if value.isdigit()==False and len(value)==16:
            raise ValidationError('ID contains characters')  
    card_name = models.CharField(max_length=25,validators=[MinLengthValidator(3)])
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5,validators=[MinLengthValidator(5)])


    

class Payment(models.Model):
    
    course = models.ForeignKey(Course,on_delete=models.RESTRICT)
    