from django.db import models
from project import settings

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=250)
    is_Completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    
    def __str__(self):
        return f'({self.task}) created on {self.created_at}'
    
    def published_at(self):
        months = [None, 'Janvier', 'Fevrier', 'Mars', 'Avril',
                  'Mai', 'Juin','Juillet','Aout', 'Septembre',
                  'Octobre', 'Novembre', 'Decembre']
        month = self.created_at.month
        
        return f'{self.created_at.day} {months[month]} {self.created_at.year}'
        
    