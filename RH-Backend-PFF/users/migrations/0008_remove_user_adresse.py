# Generated by Django 5.0.6 on 2024-06-01 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_salaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='adresse',
        ),
    ]
