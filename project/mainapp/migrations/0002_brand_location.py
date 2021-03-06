# Generated by Django 3.1 on 2020-08-27 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('store', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.brand')),
            ],
        ),
    ]
