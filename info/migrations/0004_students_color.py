# Generated by Django 5.0.1 on 2024-01-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_alter_students_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='color',
            field=models.CharField(default='white', max_length=20),
        ),
    ]