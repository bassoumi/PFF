# Generated by Django 5.0.6 on 2024-06-14 22:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_alter_employe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actiondemande',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
