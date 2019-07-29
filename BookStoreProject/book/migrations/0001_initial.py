# Generated by Django 2.2.3 on 2019-07-11 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='img')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=3)),
                ('net_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('category_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.Category')),
            ],
            options={
                'db_table': 'Book',
            },
        ),
    ]