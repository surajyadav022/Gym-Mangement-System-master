# Generated by Django 3.1.2 on 2020-11-24 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('emailid', models.EmailField(max_length=60)),
                ('age', models.IntegerField(max_length=5)),
                ('gender', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.FloatField(default=0.0, max_length=10)),
                ('unit', models.IntegerField(default=0, max_length=10)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('emailid', models.EmailField(max_length=60)),
                ('age', models.IntegerField(max_length=5)),
                ('gender', models.CharField(max_length=40)),
                ('plan', models.CharField(max_length=40)),
                ('joindate', models.DateField()),
                ('initialamount', models.FloatField(default=0.0, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.FloatField(default=0.0, max_length=10)),
                ('duration', models.IntegerField(default=0, max_length=10)),
            ],
        ),
    ]
