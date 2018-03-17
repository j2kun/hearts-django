# Generated by Django 2.0.3 on 2018-03-17 21:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hearts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suit', models.CharField(choices=[('H', 'Hearts'), ('S', 'Spades'), ('C', 'Clubs'), ('D', 'Diamonds')], default='H', max_length=1)),
                ('rank', models.CharField(choices=[('A', 'Ace'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five'), ('6', 'Six'), ('7', 'Seven'), ('8', 'Eight'), ('9', 'Nine'), ('T', 'Ten'), ('J', 'Jack'), ('Q', 'Queen'), ('K', 'King')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CardHand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_played', models.BooleanField(default=False)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hearts.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Hand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hearts.RoomMember')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_hearts_broken', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hearts.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Trick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hearts.Round')),
            ],
        ),
        migrations.CreateModel(
            name='TrickCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hearts.Card')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hearts.RoomMember')),
                ('trick', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cards_in_trick', to='hearts.Trick')),
            ],
        ),
        migrations.AddField(
            model_name='hand',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hearts.Round'),
        ),
        migrations.AddField(
            model_name='cardhand',
            name='hand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hearts.Hand'),
        ),
    ]
