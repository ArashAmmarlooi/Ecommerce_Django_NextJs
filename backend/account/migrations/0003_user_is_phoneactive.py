# Generated by Django 4.2.5 on 2023-12-28 09:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_remove_user_firstname_remove_user_lastname"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_phoneactive",
            field=models.BooleanField(default=False),
        ),
    ]
