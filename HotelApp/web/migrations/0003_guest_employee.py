# Generated by Django 4.1.7 on 2023-04-16 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.employee'),
        ),
    ]