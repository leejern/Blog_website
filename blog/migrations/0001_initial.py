# Generated by Django 4.2.6 on 2023-10-20 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('intro', models.TextField(max_length=500)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='media')),
                ('body', models.TextField()),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], max_length=255)),
            ],
        ),
    ]