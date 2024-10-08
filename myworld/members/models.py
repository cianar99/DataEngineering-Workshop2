from django.db import models

BRANCH_CHOICES = (
    ("BA", "BA"),
    ("B.COM", "B.COM"),
    ("MBA", "MBA"),
    ("CA", "CA"),
)

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    roll_number = models.IntegerField()
    mobile = models.CharField(max_length=10)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES,null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    emp_id = models.IntegerField(max_length=10, primary_key= True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.first_name + " " + self.last_name