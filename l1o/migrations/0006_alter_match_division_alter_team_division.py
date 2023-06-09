# Generated by Django 4.2.1 on 2023-06-08 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("l1o", "0005_match_scheduled_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="match",
            name="division",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="matches",
                to="l1o.division",
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="division",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teams",
                to="l1o.division",
            ),
        ),
    ]
