# Generated by Django 4.2.9 on 2024-02-01 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(upload_to='')),
                ('descripcion', models.CharField(max_length=256)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
