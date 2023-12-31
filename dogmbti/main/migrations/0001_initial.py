# Generated by Django 5.0 on 2023-12-29 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DogsMbti",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dog_name", models.CharField(max_length=100)),
                (
                    "energy",
                    models.CharField(
                        choices=[("E", "Energetic"), ("I", "Introverted")], max_length=1
                    ),
                ),
                (
                    "mental",
                    models.CharField(
                        choices=[("N", "Intuitive"), ("S", "Sensing")], max_length=1
                    ),
                ),
                (
                    "nature",
                    models.CharField(
                        choices=[("F", "Feeling"), ("T", "Thinking")], max_length=1
                    ),
                ),
                (
                    "tactics",
                    models.CharField(
                        choices=[("J", "Judging"), ("P", "Perceiving")], max_length=1
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip", models.GenericIPAddressField()),
                ("mbti", models.CharField(max_length=4)),
                ("age", models.IntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DogDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("difficulty_level", models.CharField(max_length=3)),
                ("difficulty_description", models.TextField()),
                ("dog_mbti_type", models.CharField(max_length=4)),
                ("dog_mbti_reason", models.TextField()),
                ("health_problems", models.TextField()),
                ("characteristics", models.TextField()),
                ("intelligence", models.TextField()),
                ("opinion_content", models.TextField()),
                ("youtube_link", models.URLField()),
                (
                    "dog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.dogsmbti"
                    ),
                ),
            ],
        ),
    ]
