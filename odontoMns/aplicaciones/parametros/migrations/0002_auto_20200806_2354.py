# Generated by Django 3.0.8 on 2020-08-07 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('codEst', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estado', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Urgencia',
            fields=[
                ('codUrg', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_urgencia', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='pais',
            name='nombre_pais',
            field=models.CharField(max_length=60),
        ),
    ]
