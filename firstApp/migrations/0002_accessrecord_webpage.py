# Generated by Django 3.2.7 on 2021-09-15 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('url', models.URLField(unique=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstApp.topic')),
            ],
        ),
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstApp.webpage')),
            ],
        ),
    ]
