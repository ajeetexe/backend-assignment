from django.db import models

# Create your models here.


class UserModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=255)
    zip = models.PositiveIntegerField()
    email = models.EmailField()
    web = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + self.last_name
