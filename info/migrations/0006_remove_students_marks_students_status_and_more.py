# Generated by Django 5.0.1 on 2024-01-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_students_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='marks',
        ),
        migrations.AddField(
            model_name='students',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='students',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]