# Generated by Django 4.1.3 on 2023-05-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_remove_jsondata_id_alter_jsondata_intensity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jsondata",
            name="added",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="jsondata",
            name="published",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="jsondata",
            name="start_year",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="jsondata",
            name="url",
            field=models.CharField(max_length=100),
        ),
    ]
