# Generated by Django 3.2.8 on 2021-12-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paymentDetail',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=2000)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=10)),
                ('fees', models.IntegerField(default=0)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
