# Generated by Django 5.0 on 2024-01-19 05:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_dogdetails_name_alter_dogdetails_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dogdetails",
            name="dog",
        ),
        migrations.AlterField(
            model_name="dogdetails",
            name="difficulty_level",
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name="dogdetails",
            name="youtube_link",
            field=models.URLField(default=" "),
        ),
        migrations.DeleteModel(
            name="DogsMbti",
        ),
    ]