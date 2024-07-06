from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, null=False)
    weight = models.IntegerField(null=False, default=1)
    height = models.IntegerField(null=False, default=1)
    
    def __str__(self) -> str:
        return self.name