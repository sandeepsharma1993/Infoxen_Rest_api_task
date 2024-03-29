# Generated by Django 3.2.3 on 2021-06-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OxygenCylinder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=255)),
                ('Business_Name', models.CharField(max_length=255)),
                ('Person_Name', models.CharField(max_length=255)),
                ('Contact', models.CharField(max_length=13)),
                ('Verified_Status', models.BooleanField(default=False)),
                ('TimeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
