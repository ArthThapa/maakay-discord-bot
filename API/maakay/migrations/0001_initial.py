# Generated by Django 3.2.6 on 2021-09-04 05:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, null=True)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(choices=[('NEW', 'New'), ('ONGOING', 'Ongoing'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed')], max_length=255)),
                ('hosted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hosted_by', to='core.user')),
                ('referee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tournament_referee', to='core.user')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='winner', to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='MaakayUser',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_won_in_challenges', models.IntegerField(default=0)),
                ('total_lost_in_challenges', models.IntegerField(default=0)),
                ('total_won_in_tournaments', models.IntegerField(default=0)),
                ('total_tournaments_won', models.IntegerField(default=0)),
                ('total_challenges_won', models.IntegerField(default=0)),
                ('total_referred', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('contender_accepted', models.BooleanField(default=False)),
                ('referee_accepted', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('ONGOING', 'Ongoing'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed')], max_length=255)),
                ('challenger', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='challenger', to='core.user')),
                ('contender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contender', to='core.user')),
                ('referee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='challenge_referee', to='core.user')),
            ],
        ),
    ]