# Generated by Django 5.0.3 on 2024-06-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0028_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='elective',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='graduation_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='major',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mentoring_1A',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='mentoring_2A',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='mentoring_3A',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='nationality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='option',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='promotion',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
