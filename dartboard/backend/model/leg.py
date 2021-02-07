import uuid
from django.db import models
from backend.model.match import Match
from backend.model.match_player import MatchPlayer


class Leg(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player1 = models.ForeignKey(MatchPlayer, related_name="player1", on_delete=models.CASCADE)
    player1_score_remaining = models.IntegerField(default=301)
    player2 = models.ForeignKey(MatchPlayer, related_name="player2", on_delete=models.CASCADE)
    player2_score_remaining = models.IntegerField(default=301)


