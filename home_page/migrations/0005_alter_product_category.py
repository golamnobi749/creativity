# Generated by Django 5.0.1 on 2024-01-14 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('TS', 'tshirt'), ('JP', 'jeans pants'), ('BS', 'boys shirt'), ('LE', 'lehenga'), ('BO', 'borkha'), ('WD', 'winter dress'), ('PH', 'phone'), ('LP', 'laptop'), ('EL', 'electic'), ('JF', 'just for')], max_length=16),
        ),
    ]