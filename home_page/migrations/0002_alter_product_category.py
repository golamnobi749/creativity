# Generated by Django 5.0.1 on 2024-01-13 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('tshirt', 'tshirt'), ('jeanspant', 'jeans pants'), ('boysshirt', 'boys shirt'), ('lehenga', 'lehenga'), ('borkha', ',borkha'), ('winterdress', 'winter dress'), ('phone', 'phone'), ('laptop', 'laptop'), ('electic', 'electic')], max_length=16),
        ),
    ]
