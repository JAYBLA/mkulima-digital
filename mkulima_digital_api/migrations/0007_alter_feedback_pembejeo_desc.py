# Generated by Django 4.2.5 on 2023-09-30 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkulima_digital_api', '0006_feedback_pembejeo_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='pembejeo_desc',
            field=models.CharField(max_length=180),
        ),
    ]
