from django.db import models

# Create your models here.
class Contacts(models.Model):
    class Meta:
        db_table: 'contacts'
    
    name: models.CharField(max_length = 200)
    email: models.CharField(max_length = 200)
    phone: models.CharField(max_length = 20)

    def __str__(self):
        return self.name    
