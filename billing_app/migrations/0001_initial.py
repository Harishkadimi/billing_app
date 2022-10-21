# Generated by Django 4.1.2 on 2022-10-19 15:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=250, null=True)),
                ('status', models.IntegerField(db_index=True, null=True)),
                ('created_by', models.IntegerField(db_index=True, null=True)),
                ('created_at', models.CharField(default=datetime.datetime.now, max_length=100, null=True)),
                ('updated_by', models.IntegerField(db_index=True, null=True)),
                ('updated_at', models.CharField(max_length=100, null=True)),
                ('brand_price', models.IntegerField(db_index=True, null=True)),
            ],
            options={
                'db_table': 'brand_details',
            },
        ),
        migrations.CreateModel(
            name='Error_log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('error_code', models.IntegerField(db_index=True, null=True)),
                ('error', models.TextField(null=True)),
                ('created_at', models.CharField(default=datetime.datetime.now, max_length=100, null=True)),
                ('created_by', models.IntegerField(db_index=True, null=True)),
            ],
            options={
                'db_table': 'error_log',
            },
        ),
        migrations.CreateModel(
            name='Product_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_type_name', models.CharField(max_length=250, null=True)),
                ('status', models.IntegerField(db_index=True, null=True)),
                ('created_by', models.IntegerField(db_index=True, null=True)),
                ('created_at', models.CharField(default=datetime.datetime.now, max_length=100, null=True)),
                ('updated_by', models.IntegerField(db_index=True, null=True)),
                ('updated_at', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'product_type',
            },
        ),
        migrations.CreateModel(
            name='Shop_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_id', models.IntegerField(db_index=True, null=True)),
                ('shop_name', models.CharField(max_length=250, null=True)),
                ('shop_address', models.TextField(null=True)),
                ('landmark', models.CharField(max_length=250, null=True)),
                ('status', models.IntegerField(db_index=True, null=True)),
                ('created_by', models.IntegerField(db_index=True, null=True)),
                ('created_at', models.CharField(default=datetime.datetime.now, max_length=100, null=True)),
                ('updated_by', models.IntegerField(db_index=True, null=True)),
                ('updated_at', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'shop_details',
            },
        ),
        migrations.CreateModel(
            name='User_log_table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(db_index=True, null=True)),
                ('login_at', models.CharField(max_length=100, null=True)),
                ('logout_at', models.CharField(max_length=100, null=True)),
                ('login_duration', models.CharField(max_length=100, null=True)),
                ('status', models.IntegerField(db_index=True, null=True)),
            ],
            options={
                'db_table': 'user_log_table',
            },
        ),
        migrations.CreateModel(
            name='User_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_type_name', models.CharField(max_length=250, null=True)),
                ('status', models.IntegerField(db_index=True, null=True)),
                ('created_at', models.CharField(default=datetime.datetime.now, max_length=100, null=True)),
            ],
            options={
                'db_table': 'user_type',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=250, null=True)),
                ('username', models.CharField(max_length=250, null=True)),
                ('password', models.CharField(max_length=250, null=True)),
                ('mobile_number', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=250, null=True)),
                ('user_type', models.IntegerField(db_index=True, null=True)),
                ('created_at', models.CharField(default=datetime.datetime.now, max_length=100, null=True)),
                ('updated_by', models.IntegerField(db_index=True, null=True)),
                ('updated_at', models.CharField(max_length=100, null=True)),
                ('created_by', models.IntegerField(db_index=True, null=True)),
                ('status', models.IntegerField(db_index=True, null=True)),
                ('shop_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.shop_details')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Stock_recived_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recived_datetime', models.CharField(max_length=100, null=True)),
                ('stock_recived_quantity', models.IntegerField(db_index=True, null=True)),
                ('status', models.IntegerField(db_index=True, null=True)),
                ('created_at', models.IntegerField(db_index=True, default=datetime.datetime.now, null=True)),
                ('created_by', models.CharField(max_length=250, null=True)),
                ('updated_at', models.IntegerField(db_index=True, null=True)),
                ('updated_by', models.CharField(max_length=250, null=True)),
                ('brand_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.brand_details')),
                ('product_type_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.product_type')),
                ('shop_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.shop_details')),
            ],
            options={
                'db_table': 'stock_recived_details',
            },
        ),
        migrations.CreateModel(
            name='Stock_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_type_id_fk', models.IntegerField(db_index=True, null=True)),
                ('total_quantity', models.IntegerField(db_index=True, null=True)),
                ('remaining_quantity', models.IntegerField(db_index=True, null=True)),
                ('status', models.IntegerField(db_index=True, null=True)),
                ('created_by', models.IntegerField(db_index=True, null=True)),
                ('created_at', models.CharField(default=datetime.datetime.now, max_length=100, null=True)),
                ('updated_by', models.IntegerField(db_index=True, null=True)),
                ('updated_at', models.CharField(max_length=100, null=True)),
                ('product_type_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.product_type')),
                ('shop_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.shop_details')),
            ],
            options={
                'db_table': 'stock_details',
            },
        ),
        migrations.CreateModel(
            name='Sale_transactions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unit', models.IntegerField(db_index=True, null=True)),
                ('status', models.IntegerField(db_index=True, null=True)),
                ('created_by', models.IntegerField(db_index=True, null=True)),
                ('created_at', models.CharField(default=datetime.datetime.now, max_length=100, null=True)),
                ('brand_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.brand_details')),
                ('product_type_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.product_type')),
                ('shop_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.shop_details')),
            ],
            options={
                'db_table': 'sale_transactions',
            },
        ),
        migrations.AddField(
            model_name='brand_details',
            name='product_type_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.product_type'),
        ),
    ]