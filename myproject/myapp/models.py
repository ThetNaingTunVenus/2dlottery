from django.db import models

# Create your models here.
class customer(models.Model):
    customer_name = models.CharField(max_length=225)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=225)

class lot(models.Model):
    lot_no = models.CharField(max_length=100)
    amount_limit = models.PositiveIntegerField(default=0)

class Report(models.Model):
    customer_name = models.CharField(max_length=225)
    lot_no = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(default=0)
    lot_date = models.DateField()
    am_pm = models.PositiveIntegerField(default=0)
    member_id = models.CharField(max_length=225)
    remark = models.CharField(max_length=225)
    date = models.DateTimeField(auto_now=True)

class lot_history(models.Model):
    lot_no = models.CharField(max_length=100)
    lot_date = models.DateField()
    am_pm = models.PositiveIntegerField(default=0)


