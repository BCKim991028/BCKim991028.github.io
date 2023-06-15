# Generated by Django 4.1.9 on 2023-06-14 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_alter_player_playername'),
        ('team', '0003_alter_team_team_leader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='leader_permission',
        ),
        migrations.RemoveField(
            model_name='team',
            name='location',
        ),
        migrations.RemoveField(
            model_name='team',
            name='team_leader',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='is_accepted',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='user',
        ),
        migrations.AddField(
            model_name='teammember',
            name='player',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='players.player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='team.team'),
        ),
        migrations.AlterModelTable(
            name='team',
            table='team_team',
        ),
        migrations.AlterModelTable(
            name='teammember',
            table='team_member',
        ),
        migrations.DeleteModel(
            name='TeamRegistration',
        ),
    ]
