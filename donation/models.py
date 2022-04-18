from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self) -> str:
        return f"{self.name}"


class Institution(models.Model):
    foundation = 'FD'
    non_governmental_organisation = 'NGO'
    local_collection = 'LC'

    types_of_institutions = (
        (foundation, 'Foundation'),
        (non_governmental_organisation, 'Non-Governmental Organisation'),
        (local_collection, 'Local Collection')
    )
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=40, choices=types_of_institutions, default=foundation)
    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return f"{self.name} {self.description} {self.type}"


class Donation(models.Model):
    quantity = models.IntegerField()
    address = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=12)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=150)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.quantity}"
