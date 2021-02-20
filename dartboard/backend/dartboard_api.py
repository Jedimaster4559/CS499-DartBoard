from backend.models import *


def create_player(first_name, last_name):
    player = Player(first_name=first_name, last_name=last_name, current_league_rank=Player.objects.count())
    player.save()
    return player


def get_players_by_name(first_name, last_name):
    return Player.objects.get(first_name=first_name, last_name=last_name)


def get_players_by_id(player_id):
    return Player.objects.get(id=player_id)


def create_match(player1, player2, num_legs=1, leg_score=301):
    # Create the new Match
    match = Match()
    match.save()

    # Setup the new players and add them to the match
    player1_stats = MatchPlayer(match=match.id, player=player1)
    player1_stats.save()
    player2_stats = MatchPlayer(match=match.id, player=player2)
    player2_stats.save()

    # Add all the legs
    for x in range(num_legs):
        leg = Leg(match=match.id, player1=player1_stats, player1_score_remaining=leg_score, player2=player2_stats, player2_score_remaining=leg_score)
        leg.save()

    return match


def start_new_turn(leg, player):
    turn = Turn(game=leg, player=player)
    turn.save()
    return turn


def add_hit(turn, value):
    hit = DartboardHit(turn=turn, score=value)
    hit.save()
    return hit


def mark_bounce_out(hit_id):
    hit = DartboardHit.objects.get(id=hit_id)
    hit.is_bounce_out = True
    hit.save()
    return hit


def mark_knock_out(hit_id):
    hit = DartboardHit.objects.get(id=hit_id)
    hit.is_knock_out = True
    hit.save()
    return hit


def commit_turn(turn, leg):
    # Should return true if the turn can be committed, and false if not.
    hits = DartboardHit.objects.filter(turn=turn)

    # Get the players current score
    if turn.player.id == leg.player1.id:
        score_remaining = leg.player1_score_remaining
    else:
        score_remaining = leg.player2_score_remaining

    # Calculate Score for the turn
    score = 0
    for hit in hits:
        if not hit.is_bounce_out and not hit.is_knock_out:
            score += hit.score
            # Check that this turn wasn't a bust
            if score_remaining - score < 0 or score_remaining - score == 1:
                turn.is_bust = True
                turn.save()
                return False

    # Update Player's leg score
    if turn.player.id == leg.player1.id:
        leg.player1_score_remaining -= score
    else:
        leg.player2_score_remaining -= score

    leg.save()

    # Update Player's In-game statistics
    turn.player.update(hits)
    turn.player.save()

    # Update Player's Lifetime statistics
    turn.player.player.update(hits)
    turn.player.player.save()

    return True
