# Generated by Django 5.1.1 on 2024-11-06 23:13

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_email', models.EmailField(max_length=50)),
                ('customer_address', models.TextField()),
                ('customer_number', models.CharField(max_length=15)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_city', models.CharField(max_length=50)),
                ('customer_state', models.CharField(max_length=50)),
                ('customer_country', models.CharField(max_length=50)),
                ('order_completed', models.BooleanField(default=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_id', models.UUIDField()),
                ('product_quantity', models.PositiveIntegerField()),
                ('product_size', models.CharField(max_length=10)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.orders')),
            ],
        ),
    ]
