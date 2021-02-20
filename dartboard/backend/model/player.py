###################
# Describes a player's lifetime data
###################
import uuid
from django.db import models


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    current_league_rank = models.IntegerField()
    average_season_score = models.DecimalField(default=0, decimal_places=10, max_digits=15)
    average_lifetime_score = models.DecimalField(default=0, decimal_places=10, max_digits=15)
    number_of_180s = models.IntegerField(default=0)
    number_of_season_turns = models.IntegerField(default=0)
    number_of_lifetime_turns = models.IntegerField(default=0)

    def update(self, hits):
        # Generate Score
        score = 0
        for hit in hits:
            score += hit

        # Update Season Average
        total_score = self.average_season_score * self.number_of_season_turns
        total_score += score
        self.number_of_season_turns += 1
        self.average_season_score = total_score / self.number_of_season_turns

        # Update Lifetime Average
        total_score = self.average_turn_score * self.number_of_lifetime_turns
        total_score += score
        self.number_of_lifetime_turns += 1
        self.average_turn_score = total_score / self.number_of_lifetime_turns

        # Update 180s
        if score == 180:
            self.number_of_180s += 1

        # Save Results
        self.save()
