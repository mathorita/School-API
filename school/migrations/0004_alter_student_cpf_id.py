# Generated by Django 5.2.1 on 2025-05-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cpf_id',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
