# Generated by Django 4.0.1 on 2022-11-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_tguser_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='verification_code',
            field=models.IntegerField(verbose_name='Код для верификации'),
        ),
    ]