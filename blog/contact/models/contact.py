from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Customer name")
    surname = models.CharField(max_length=50, verbose_name = "Customer surname")
    email = models.EmailField(max_length=60, verbose_name="Customer contact email")
    number = models.CharField(max_length=20, verbose_name="Customer phone number")

    class Meta:
        verbose_name = "Customer Contact Detail"
        verbose_name_plural = "Customer Contact Details"
    
    def __str__(self):
        return f'{self.name} {self.surname}'

