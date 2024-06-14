# Generated by Django 5.0.6 on 2024-06-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_consignor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Consignee",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("consignee_name", models.CharField(max_length=200, null=True)),
                ("consignee_phno", models.CharField(max_length=200, null=True)),
                ("consignee_addr", models.CharField(max_length=200, null=True)),
                ("consignee_gst", models.CharField(max_length=200, null=True)),
            ],
        ),
    ]