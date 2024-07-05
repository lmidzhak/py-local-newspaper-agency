# Generated by Django 4.1 on 2024-06-24 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0005_newspaperedition_edition"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="redactor",
            options={
                "ordering": ["username"],
                "verbose_name": "redactor",
                "verbose_name_plural": "redactors",
            },
        ),
        migrations.AlterModelOptions(
            name="topic",
            options={"ordering": ["name"]},
        ),
        migrations.RenameField(
            model_name="article",
            old_name="publishers",
            new_name="redactors",
        ),
    ]
