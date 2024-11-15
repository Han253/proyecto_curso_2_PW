# Generated by Django 5.1.3 on 2024-11-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('peso', models.IntegerField()),
                ('altura', models.FloatField()),
                ('imagen', models.FileField(upload_to='pokemones/')),
            ],
        ),
    ]