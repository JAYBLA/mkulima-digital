# Generated by Django 4.2.5 on 2023-09-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkulima_digital_api', '0007_alter_feedback_pembejeo_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='pembejeo_desc',
            field=models.CharField(blank=True, max_length=180),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='pembejeo_type',
            field=models.CharField(blank=True, max_length=180),
        ),
    ]