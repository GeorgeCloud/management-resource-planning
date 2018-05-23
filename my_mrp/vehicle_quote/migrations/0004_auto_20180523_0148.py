# Generated by Django 2.0.5 on 2018-05-23 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_vehicle', '0002_auto_20180523_0127'),
        ('vehicle_quote', '0003_auto_20180523_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclequote',
            name='model_name',
        ),
        migrations.AddField(
            model_name='vehiclequote',
            name='model_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vehicle_quotes', to='product_vehicle.Vehicle'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehiclequote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vehicle_quotes', to=settings.AUTH_USER_MODEL),
        ),
    ]