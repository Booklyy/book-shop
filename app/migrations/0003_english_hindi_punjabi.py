# Generated by Django 4.1.1 on 2023-04-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_arrivals_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='english',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='english/')),
                ('mrp', models.FloatField()),
                ('sellingprice', models.FloatField()),
            ],
            options={
                'db_table': 'english',
            },
        ),
        migrations.CreateModel(
            name='hindi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='hindi/')),
                ('mrp', models.FloatField()),
                ('sellingprice', models.FloatField()),
            ],
            options={
                'db_table': 'hindi',
            },
        ),
        migrations.CreateModel(
            name='punjabi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='punjabi/')),
                ('mrp', models.FloatField()),
                ('sellingprice', models.FloatField()),
            ],
            options={
                'db_table': 'punjabi',
            },
        ),
    ]