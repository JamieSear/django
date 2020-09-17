# Generated by Django 3.1.1 on 2020-09-16 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='players',
            name='wins',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tennis.wins'),
        ),
    ]