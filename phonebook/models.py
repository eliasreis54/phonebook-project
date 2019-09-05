from django.db import models

# Create your models here.
class Contacts(models.Model):
    class Meta:
        db_table: 'contacts'
    
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 20, null = True)

    def __str__(self):
        return self.name    
