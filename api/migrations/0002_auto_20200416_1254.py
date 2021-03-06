# Generated by Django 3.0.2 on 2020-04-16 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(default='', max_length=30)),
                ('producer', models.CharField(default='', max_length=30)),
                ('movie', models.ManyToManyField(to='api.Movie')),
            ],
        ),
    ]
