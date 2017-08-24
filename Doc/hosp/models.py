from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hospital(models.Model):
    h_name = models.CharField(max_length=120)
    image=models.ImageField(upload_to=upload_location, null=True,blank=True,
                            width_field="width_field",height_field="height_field")
    h_content=models.TextField()
    address=models.TextField()
    
    def __str__(self):
        return self.h_name

 #   def get_absolute_url(self):
 #      return reverse("posts:detail",kwargs={"slug":self.slug})


        
