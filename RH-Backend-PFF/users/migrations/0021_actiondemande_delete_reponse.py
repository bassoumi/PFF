# Generated by Django 5.0.6 on 2024-06-13 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_reponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionDemande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('date_reponse', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('demande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.leaverequest')),
            ],
        ),
        migrations.DeleteModel(
            name='Reponse',
        ),
    ]
