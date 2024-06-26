# Generated by Django 5.0.3 on 2024-03-31 10:14

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
            name='Poem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('author', models.TextField(blank=True)),
                ('interpretation', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='poems', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PoemReactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.TextField()),
                ('poem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poem_reaction_2', to='ghazals.poem')),
                ('reacted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poem_reaction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
