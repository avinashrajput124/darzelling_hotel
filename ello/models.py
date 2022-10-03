# from mapbox_location_field.models import LocationField  
# from mapbox_location_field.spatial.models import SpatialLocationField  

from distutils import text_file
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
       is_pastudent = models.BooleanField(default=False)
       phone = models.IntegerField(default=000000000)
       address = models.TextField(max_length=120)
       first_name = models.CharField(max_length=100)
       last_name = models.CharField(max_length=100)
       

       def __str__(self):
              return self.username 



class Add_Hotal(models.Model): 
    Hotal_id = models.AutoField(primary_key=True) 
    Hotal_Name = models.CharField(max_length=50)
    hotal_new_price = models.CharField(max_length=255 ,default="")
    hotal_discreption = models.TextField(max_length=500)
    # Hotal_Location = models.CharField(max_length=200)
    Hotal_Location = models.CharField(max_length=200)
    Hotal_Latitude = models.FloatField()
    Hotal_Longitude = models.FloatField()
    # Hotal_Location = SpatialLocationField(null=True)
    # hotel images
    Hotal_images1 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    Hotal_images2 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    Hotal_images3 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    Hotal_images4= models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    Hotal_images5 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    # garden images
    garden_images1 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    garden_images2 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    garden_images3 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    garden_images4= models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    garden_images5 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)

    # reception images
    reception_images1 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    reception_images2 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    reception_images3 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    reception_images4= models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    reception_images5 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)

    # bedroom Images
    bedroom_images1 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    bedroom_images2 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    bedroom_images3 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    bedroom_images4= models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    bedroom_images5 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    # washroom Images
    washroom_images1 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    washroom_images2 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    washroom_images3 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    washroom_images4= models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    washroom_images5 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)

    # Exterior Images
    Exterior_images1 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    Exterior_images2 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    Exterior_images3 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    Exterior_images4= models.ImageField(upload_to='hotalmedia', null=True, blank=True)
    Exterior_images5 = models.ImageField(upload_to='hotalmedia', null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True, null=True)
    hotal_ratting = models.ImageField(default=0)
 
    def __str__(self):
        return str(self.Hotal_Name)

    class Meta:
        ordering = ('-date',)




# class PA(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
#     phone_number = models.CharField(max_length=20)
#     state = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
