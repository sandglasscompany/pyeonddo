# Generated by Django 3.1 on 2020-08-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='product',
            field=models.ManyToManyField(related_name='event_product', to='promotions.Product'),
        ),
    ]
