# Generated by Django 3.0.3 on 2020-02-05 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almajlis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='almajlis.Session'),
            preserve_default=False,
        ),
    ]