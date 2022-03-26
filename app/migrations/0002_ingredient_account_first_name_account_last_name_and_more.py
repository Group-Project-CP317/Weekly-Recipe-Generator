# Generated by Django 4.0.1 on 2022-03-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('amount', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ingredients', models.ManyToManyField(to='app.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='favorites',
            field=models.ManyToManyField(to='app.Recipe'),
        ),
    ]