# Generated by Django 4.0.6 on 2023-05-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_blog_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(default='', upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(),
        ),
    ]
