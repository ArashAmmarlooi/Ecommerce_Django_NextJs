# Generated by Django 4.2.5 on 2024-01-02 09:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0006_alter_user_phone_number_alter_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="verification_code",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]