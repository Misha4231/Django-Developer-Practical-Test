# Generated by Django 5.2.3 on 2025-06-26 22:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('HTTP_method', models.CharField(max_length=10)),
                ('path', models.CharField(max_length=2048)),
                ('query_string', models.CharField(blank=True, max_length=1024)),
                ('remote_IP', models.CharField(max_length=45)),
                ('logged_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
