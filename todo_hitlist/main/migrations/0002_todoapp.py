# Generated by Django 5.1.3 on 2024-11-22 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.CharField(max_length=32)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('github_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]