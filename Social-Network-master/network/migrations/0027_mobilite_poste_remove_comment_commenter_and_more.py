# Generated by Django 5.0.3 on 2024-06-03 14:42

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0026_remove_user_ancienne_ecole_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobilite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecole', models.CharField(default='Inconnu', max_length=100)),
                ('filiere', models.CharField(default='Inconnu', max_length=100)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entreprise', models.CharField(default='Inconnu', max_length=100)),
                ('domaine', models.CharField(default='Inconnu', max_length=100)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commenter',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='CV',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='creater',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likers',
        ),
        migrations.RemoveField(
            model_name='post',
            name='savers',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='titre',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='type',
        ),
        migrations.AddField(
            model_name='stage',
            name='annee',
            field=models.PositiveIntegerField(default=2024),
        ),
        migrations.AddField(
            model_name='stage',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='stage',
            name='date_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='stage',
            name='domaine',
            field=models.CharField(default='Inconnu', max_length=100),
        ),
        migrations.AddField(
            model_name='stage',
            name='entreprise',
            field=models.CharField(default='Inconnu', max_length=100),
        ),
        migrations.AddField(
            model_name='stage',
            name='theme',
            field=models.CharField(default='Inconnu', max_length=200),
        ),
        migrations.AddField(
            model_name='stage',
            name='type_stage',
            field=models.CharField(choices=[('PFE', 'PFE'), ('Cesure', 'Césure'), ('Operateur', 'Opérateur'), ('Academique', 'Académique')], default='PFE', max_length=50),
        ),
        migrations.AddField(
            model_name='stage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/'),
        ),
        migrations.AddField(
            model_name='mobilite',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mobilites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='poste',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='postes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Follower',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
