# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_remove_players_league'),
        ('ping_pong', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Players')),
            ],
        ),
        migrations.CreateModel(
            name='Relationships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='games',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='leagues',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='relationships',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ping_pong.Leagues'),
        ),
        migrations.AddField(
            model_name='relationships',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Players'),
        ),
    ]
