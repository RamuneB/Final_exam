# Generated by Django 4.1.1 on 2022-10-05 17:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_alter_uzrasasmano_id_uzrasoperziura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzrasasmano',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unikalus ID knygos kopijai', primary_key=True, serialize=False),
        ),
    ]
