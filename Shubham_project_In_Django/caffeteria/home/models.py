from django.db import models

# Create your models here.
class Order_Menu(models.Model):
    User_id = models.IntegerField()
    name = models.CharField(max_length=100)
    select_product = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Mob_num = models.IntegerField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return f'Message From {self.name}'

      