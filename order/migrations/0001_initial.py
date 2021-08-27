# Generated by Django 3.2.1 on 2021-08-27 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orderer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=64, unique=True)),
                ('address', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=512)),
                ('total', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('pay_time', models.DateTimeField(null=True)),
                ('orderer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.orderer')),
            ],
        ),
    ]
