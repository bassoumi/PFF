# Generated by Django 5.0.6 on 2024-06-01 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_salaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='salaire',
        ),
    ]
