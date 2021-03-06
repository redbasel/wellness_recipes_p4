# Generated by Django 3.2.14 on 2022-07-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoori_recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cooking_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='instructions',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]
