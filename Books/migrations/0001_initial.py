# Generated by Django 4.1.1 on 2023-01-09 01:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('is_free', models.BooleanField(default=False)),
                ('_type', models.CharField(choices=[('e-book', 'e-book'), ('hard-book', 'hard-book')], max_length=250)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
    ]
