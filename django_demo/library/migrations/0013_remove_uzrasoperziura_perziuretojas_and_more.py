# Generated by Django 4.1.1 on 2022-10-07 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_alter_uzrasasmano_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uzrasoperziura',
            name='perziuretojas',
        ),
        migrations.RemoveField(
            model_name='uzrasoperziura',
            name='uzrasas',
        ),
        migrations.DeleteModel(
            name='UzrasasMano',
        ),
        migrations.DeleteModel(
            name='UzrasoPerziura',
        ),
    ]
