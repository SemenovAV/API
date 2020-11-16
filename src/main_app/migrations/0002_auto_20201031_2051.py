# Generated by Django 3.1.2 on 2020-10-31 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="expert",
            name="course",
        ),
        migrations.RemoveField(
            model_name="expert",
            name="person",
        ),
        migrations.AddField(
            model_name="group",
            name="lecture",
            field=models.ManyToManyField(related_name="group", to="main_app.WebConference"),
        ),
        migrations.AddField(
            model_name="person",
            name="coordinater",
            field=models.ManyToManyField(related_name="coordinaters", to="main_app.Course"),
        ),
        migrations.AddField(
            model_name="person",
            name="expert_lecture",
            field=models.ManyToManyField(related_name="experts", to="main_app.WebConference"),
        ),
        migrations.AlterField(
            model_name="course",
            name="direction",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="courses", to="main_app.direction"),
        ),
        migrations.AlterField(
            model_name="person",
            name="middle_name",
            field=models.CharField(blank=True, default="", max_length=20),
        ),
        migrations.DeleteModel(
            name="Coordinater",
        ),
        migrations.DeleteModel(
            name="Expert",
        ),
    ]
