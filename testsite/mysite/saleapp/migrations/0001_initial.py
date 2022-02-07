# Generated by Django 4.0.2 on 2022-02-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_publiched', models.BooleanField(default=True)),
            ],
        ),
    ]
