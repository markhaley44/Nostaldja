# Generated by Django 2.1.5 on 2019-02-12 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fads',
            name='decade',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Decades', to='nostaldja_app.Decades'),
        ),
        migrations.AlterField(
            model_name='decades',
            name='start_year',
            field=models.CharField(max_length=100),
        ),
    ]