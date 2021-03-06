# Generated by Django 3.2.9 on 2021-11-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, unique=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('profile_image', models.ImageField(upload_to='pinterest/actor/images')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Movie Name')),
                ('description', models.TextField()),
                ('release_date', models.DateField(blank=True, null=True)),
                ('poster', models.ImageField(null=True, upload_to='pinterest/images')),
                ('season', models.CharField(max_length=255)),
                ('episode', models.CharField(max_length=255)),
                ('casts', models.ManyToManyField(to='pinterest.Casts')),
                ('categories', models.ManyToManyField(to='pinterest.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Movie Name')),
                ('description', models.TextField()),
                ('release_date', models.DateField(blank=True, null=True)),
                ('poster', models.ImageField(null=True, upload_to='pinterest/images')),
                ('casts', models.ManyToManyField(to='pinterest.Casts')),
                ('categories', models.ManyToManyField(to='pinterest.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
