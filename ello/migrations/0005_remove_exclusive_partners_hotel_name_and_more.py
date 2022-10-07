# Generated by Django 4.1 on 2022-10-07 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ello', '0004_exclusive_partners_holiday_packages_promotions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exclusive_partners',
            name='hotel_name',
        ),
        migrations.RemoveField(
            model_name='holiday_packages',
            name='hotel_name',
        ),
        migrations.AlterField(
            model_name='promotions',
            name='promotions_images1',
            field=models.ImageField(blank=True, null=True, upload_to='media/promotions'),
        ),
        migrations.AlterField(
            model_name='promotions',
            name='promotions_images2',
            field=models.ImageField(blank=True, null=True, upload_to='media/promotions'),
        ),
        migrations.AlterField(
            model_name='promotions',
            name='promotions_images3',
            field=models.ImageField(blank=True, null=True, upload_to='media/promotions'),
        ),
        migrations.AlterField(
            model_name='promotions',
            name='promotions_images4',
            field=models.ImageField(blank=True, null=True, upload_to='media/promotions'),
        ),
    ]
