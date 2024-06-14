from django.db import models

# Create your models here.


class Insert(models.Model):
    gc_no=models.CharField(max_length=200, null=True)
    gc_dt=models.CharField(max_length=200, null=True)
    invoice_dt=models.CharField(max_length=200, null=True)
    consignor_name=models.CharField(max_length=200, null=True)
    consignee_name=models.CharField(max_length=200, null=True)
    vechile_no=models.CharField(max_length=200, null=True)
    from_addr=models.CharField(max_length=200, null=True)
    to_addr=models.CharField(max_length=200, null=True)
    invoice_no=models.CharField(max_length=200, null=True)
    invoice_amount=models.CharField(max_length=200, null=True)
    note=models.CharField(max_length=200, null=True)
    articles=models.CharField(max_length=200, null=True)
    topay=models.CharField(max_length=200, null=True)
    paid=models.CharField(max_length=200, null=True)

class Party_gc(models.Model):
    gc_no=models.CharField(max_length=200, null=True)
    gc_dt=models.CharField(max_length=200, null=True)
    invoice_dt=models.CharField(max_length=200, null=True)
    consignor_name=models.CharField(max_length=200, null=True)
    consignee_name=models.CharField(max_length=200, null=True)
    vechile_no=models.CharField(max_length=200, null=True)
    from_addr=models.CharField(max_length=200, null=True)
    to_addr=models.CharField(max_length=200, null=True)
    invoice_no=models.CharField(max_length=200, null=True)
    invoice_amount=models.CharField(max_length=200, null=True)
    note=models.CharField(max_length=200, null=True)
    articles=models.CharField(max_length=200, null=True)
    topay=models.CharField(max_length=200, null=True)
    paid=models.CharField(max_length=200, null=True)


class Consignor(models.Model):
    consignor_name=models.CharField(max_length=200, null=True)
    consignor_phno=models.CharField(max_length=200, null=True)
    consignor_addr=models.CharField(max_length=200, null=True)
    consignor_gst=models.CharField(max_length=200, null=True)


class Consignee(models.Model):
    consignee_name=models.CharField(max_length=200, null=True)
    consignee_phno=models.CharField(max_length=200, null=True)
    consignee_addr=models.CharField(max_length=200, null=True)
    consignee_gst=models.CharField(max_length=200, null=True)