from django.contrib.auth.models import User
from hearts.models import Game
from hearts.models import Room
from hearts.models import RoomMember
import pytest


@pytest.mark.django_db
def test_get_players_only_selects_playing_players():
    user1 = User.objects.create(username='j2kun')
    user2 = User.objects.create(username='dnghiem')
    room = Room.objects.create(url='blah')

    RoomMember.objects.create(room=room, user=user1, is_playing=True)
    RoomMember.objects.create(room=room, user=user2, is_playing=False)
    game = Game.objects.create(room=room)

    players_queryset = game.get_players()
    assert players_queryset.exists()
    assert players_queryset.get().user == user1
