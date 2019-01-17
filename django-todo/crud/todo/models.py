from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)

    class Meta:  
    	verbose_name='Employee'
    	verbose_name_plural='Employees'
    def __str__(self):

    	return self.name  