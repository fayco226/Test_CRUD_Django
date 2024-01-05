from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField( max_length=50)
    status = models.BooleanField(default=False)
    def __str__(self):
        pass

    class Meta:
        ordering=['title']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        
        