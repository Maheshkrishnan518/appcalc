from django.db import models

# Create your models here.
# Create your models here.
from django.db import models  

class Appcalculator(models.Model):   
    category = models.CharField(max_length=100)     
    class Meta:  
        db_table = "appcalculator"  
    def __str__(self):
         return (f"{self.category}")
    
class Feature(models.Model):
    feature = models.CharField(max_length=100)  
    hours= models.IntegerField() 
    category = models.ForeignKey(Appcalculator, on_delete=models.CASCADE)

    class Meta:  
        db_table = "feature"  
    def __str__(self):
        return self.feature
        