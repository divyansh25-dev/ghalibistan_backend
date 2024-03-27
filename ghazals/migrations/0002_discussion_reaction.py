# Generated by Django 5.0.3 on 2024-03-27 06:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghazals', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('reply_to_id', models.IntegerField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions_user', to=settings.AUTH_USER_MODEL)),
                ('ghazal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions_ghazals', to='ghazals.ghazal')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions_discussion', to='ghazals.discussion')),
                ('reacted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
