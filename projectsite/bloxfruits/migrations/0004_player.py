# Generated by Django 4.2.7 on 2024-01-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloxfruits', '0003_delete_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('player_type', models.CharField(blank=True, max_length=100, null=True)),
                ('bloxfruit', models.ManyToManyField(blank=True, to='bloxfruits.bloxfruit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
