from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Room(models.Model):
    url = models.CharField(max_length=1024)

    def get_playing_members(self):
        return self.members.filter(is_playing=True)


class RoomMember(models.Model):
    room = models.ForeignKey('Room', related_name='members', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_playing = models.BooleanField(default=True)


class Game(models.Model):
    created = models.DateTimeField(default=timezone.now)
    room = models.ForeignKey('Room', on_delete=models.PROTECT)

    def get_players(self):
        return self.room.members.filter(is_playing=True)


class Round(models.Model):
    created = models.DateTimeField(default=timezone.now)
    game = models.ForeignKey('Game', on_delete=models.PROTECT)
    is_hearts_broken = models.BooleanField(default=False)


class Hand(models.Model):
    player = models.ForeignKey('RoomMember', on_delete=models.PROTECT)
    round = models.ForeignKey('Round', on_delete=models.PROTECT)


class CardHand(models.Model):
    card = models.ForeignKey('Card', on_delete=models.PROTECT)
    hand = models.ForeignKey('Hand', on_delete=models.PROTECT)
    is_played = models.BooleanField(default=False)


class Trick(models.Model):
    round = models.ForeignKey('Round', on_delete=models.PROTECT)

    def ordered_cards(self):
        return self.cards_in_trick.order_by('id')


class TrickCard(models.Model):
    trick = models.ForeignKey('Trick', on_delete=models.PROTECT, related_name='cards_in_trick')
    card = models.ForeignKey('Card', on_delete=models.PROTECT)
    player = models.ForeignKey('RoomMember', on_delete=models.PROTECT)


class Card(models.Model):
    SUIT_CHOICES = (
        ('H', 'Hearts'),
        ('S', 'Spades'),
        ('C', 'Clubs'),
        ('D', 'Diamonds'),
    )
    RANK_CHOICES = (
        ('A', 'Ace'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
        ('6', 'Six'),
        ('7', 'Seven'),
        ('8', 'Eight'),
        ('9', 'Nine'),
        ('T', 'Ten'),
        ('J', 'Jack'),
        ('Q', 'Queen'),
        ('K', 'King'),
    )
    suit = models.CharField(
        max_length=1, choices=SUIT_CHOICES, default=SUIT_CHOICES[0][0])
    rank = models.CharField(
        max_length=1, choices=RANK_CHOICES, default=RANK_CHOICES[0][0])

    def __repr__(self):
        return self.rank + self.suit.lower()
