# Generated by Django 2.2.3 on 2019-07-11 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
