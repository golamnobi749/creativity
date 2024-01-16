# Generated by Django 5.0.1 on 2024-01-11 12:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('courrent_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('meta_title', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('ts', 'tshirt'), ('jp', 'jeans pants'), ('bs', 'boys shirt'), ('le', 'lehenga'), ('bk', ',borkha'), ('ws', 'winter dress'), ('ph', 'phone'), ('lp', 'laptop'), ('el', 'electic')], max_length=2)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='product/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('city', models.CharField(choices=[('dhaka', 'dhaka'), ('Rajshahi', 'Rajshahi'), ('chittagong', 'Chittagong'), ('khulna', 'khulna'), ('Sylhet', 'Sylhet'), ('pabna', 'pabna')], max_length=100)),
                ('house_building', models.CharField(max_length=30)),
                ('zipcode', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.customer')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for Delivery', 'Out For Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Processing', 'Processing')], max_length=16)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('location', models.CharField(max_length=16)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.cart')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.product')),
            ],
        ),
    ]
