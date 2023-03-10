# Generated by Django 3.2.12 on 2022-12-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20201130_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherimages',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Accessories', 'Accessories'), ('Men', 'Men'), ('Courtwear', 'Courtwear'), ('Ceremonial', 'Ceremonial'), ('Women', 'Women')], default='Accessories', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='size',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
