# Generated by Django 3.2.3 on 2021-06-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CouncilSampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payload_object', models.TextField()),
                ('transaction_status', models.BooleanField(default=0)),
                ('error_message', models.TextField()),
            ],
        ),
    ]
