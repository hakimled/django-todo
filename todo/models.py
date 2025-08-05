from django.db import models

from datetime import datetime, timezone

class Task(models.Model):
    task = models.CharField(max_length=250)
    is_Completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.task}) created on {self.created_at}'
    
    
    
    
    def published_at(self):
        months = [None, 'Janvier', 'Fevrier', 'Mars', 'Avril',
                'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre',
                'Octobre', 'Novembre', 'Decembre']
        month = self.created_at.month
        year = self.created_at.year
        current_year = datetime.now(timezone.utc).year

        if year == current_year:
            return f'{self.created_at.day} {months[month]}'
        else:
            return f'{self.created_at.day} {months[month]} {year}'

    # def published_at(self):
    #     months = [None, 'Janvier', 'Fevrier', 'Mars', 'Avril',
    #               'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre',
    #               'Octobre', 'Novembre', 'Decembre']
    #     month = self.created_at.month
        
    #     return f'{self.created_at.day} {months[month]} {self.created_at.year}'
    
    
    def published_since(self):
        now = datetime.now(timezone.utc)
        diff = now - self.created_at

        seconds = int(diff.total_seconds())
        minutes = seconds // 60
        hours = minutes // 60
        days = diff.days

        if seconds < 60:
            # return f'{seconds} second{"s" if seconds != 1 else ""}'
            return f"A l'instant"
        elif minutes < 60:
            return f'{minutes} minute{"s" if minutes != 1 else ""}'
        elif hours < 24:
            return f'{hours} hour{"s" if hours != 1 else ""}'
        elif days < 3:
            return f'{days} day{"s" if days != 1 else ""}'
        else:
            return self.published_at()

