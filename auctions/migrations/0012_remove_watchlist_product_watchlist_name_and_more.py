# Generated by Django 4.2.2 on 2023-11-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='product',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
