# Generated by Django 3.2 on 2021-05-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meters", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meterreading",
            name="flow_file",
            field=models.CharField(
                help_text="Flow file this reading was taken from.", max_length=255
            ),
        ),
        migrations.AlterField(
            model_name="meterreading",
            name="meter_serial_number",
            field=models.TextField(
                help_text="Serial number of the meter this reading was taken from."
            ),
        ),
        migrations.AlterField(
            model_name="meterreading",
            name="mpan",
            field=models.CharField(
                help_text="Meter Point Administration Number.",
                max_length=21,
                verbose_name="MPAN",
            ),
        ),
    ]
