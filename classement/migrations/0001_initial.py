# Generated by Django 4.2.15 on 2025-05-30 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('judokas', '0002_remove_judokas_date_naissance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField()),
                ('classements', models.IntegerField()),
                ('judokas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judokas.judokas')),
            ],
        ),
    ]
