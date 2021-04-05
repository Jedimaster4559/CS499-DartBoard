from backend.models import *


def create_player(first_name, last_name):
    full_name = first_name + " " + last_name
    player = Player(first_name=first_name, last_name=last_name, full_name=full_name,
                    current_league_rank=Player.objects.count())
    player.save()
    return player


def get_player_by_full_name(full_name):
    return Player.objects.filter(full_name=full_name).first()


def get_players_by_name(first_name, last_name):
    return Player.objects.get(first_name=first_name, last_name=last_name)


def get_all_players():
    return Player.objects.all()


def search_players(search):
    first_name_search_results = Player.objects.filter(first_name__contains=search)
    last_name_search_results = Player.objects.filter(last_name__contains=search)
    return last_name_search_results | first_name_search_results


def get_players_by_id(player_id):
    return Player.objects.get(id=player_id)


def get_match_by_id(match_id):
    return Match.objects.get(id=match_id)


def get_match_by_id(match_id):
    return Match.objects.get(id=match_id)


def get_players_by_match_id(match_id):
    match = get_match_by_id(match_id)
    first_leg = Leg.objects.filter(match=match).first()
    return [first_leg.player1, first_leg.player2]


def get_number_of_legs_by_match_id(match_id):
    match = get_match_by_id(match_id)
    first_set = Set.objects.filter(match=match).first()
    return first_set.best_of_legs_number


def create_match(player1, player2, num_sets=13, num_legs=5, game_mode=301):
    # Create the new Match
    match = Match(best_of_sets_number=num_sets)
    match.save()

    # Setup the new players and add them to the match
    player1_stats = MatchPlayer(match=match, player=player1, score_remaining=game_mode)
    player1_stats.save()
    player2_stats = MatchPlayer(match=match, player=player2, score_remaining=game_mode)
    player2_stats.save()

    # Add all the sets
    for x in range(num_sets):
        darts_set = Set(match=match, best_of_legs_number=num_legs, set_number=x)
        darts_set.save()

        # Add all the legs
        for y in range(num_legs):
            leg = Leg(set=darts_set, match=match, game_mode=game_mode, player1=player1_stats, player2=player2_stats,
                      leg_number=y)
            leg.save()

        darts_set.save()

    return match


def start_new_turn(leg, player):
    turn = Turn(game=leg, player=player)
    turn.save()
    return turn


def add_hit(turn, value, is_double=False, is_triple=False, is_bullseye=False):
    hit = DartboardHit(turn=turn, score=value, is_double=is_double, is_triple=is_triple, is_bullseye=is_bullseye)
    hit.save()
    return hit

def get_hits(turn):
    return DartboardHit.objects.filter(turn=turn)


def remove_hit(dart):
    dart.delete()
    return True


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


# Checks if a given turn causes that player to win (true if win,
# false if not win). If the turn is uncommitted, then it will
# calculate score remaining to determine win, if it is committed
# it just checks if the score remaining is 0. It also checks to
# make sure that the last throw was a double, triple, or bullseye
def check_win(turn):
    # Get hits
    hits = DartboardHit.objects.filter(turn=turn)

    # Determine if last throw was one that could win
    last_hit = hits[hits.count() - 1]
    is_winnable = last_hit.is_double or last_hit.is_bullseye

    # If turn is committed, win occurs when score = 0
    if turn.is_committed:
        return turn.player.score_remaining == 0 and is_winnable
    else:
        # Get the players current score
        score_remaining = turn.player.score_remaining

        # Calculate Score for the turn
        for hit in hits:
            if not hit.is_bounce_out and not hit.is_knock_out:
                score_remaining -= hit.score

        return score_remaining == 0 and is_winnable


def add_leg_win(winning_player, losing_player, leg):
    # Mark Winner
    winning_player.leg_wins = winning_player.leg_wins + 1
    winning_player.save()

    # Increment Number of Legs Played
    leg.set.num_legs_complete = leg.set.num_legs_complete + 1
    leg.set.save()
    leg.save()

    # Increment Player Stats
    winning_player.score_remaining = leg.game_mode
    winning_player.player.number_of_legs_won = winning_player.player.number_of_legs_won + 1
    winning_player.save()
    winning_player.player.save()
    losing_player.score_remaining = leg.game_mode
    losing_player.player.number_of_legs_lost = losing_player.player.number_of_legs_lost + 1
    losing_player.save()
    losing_player.player.save()


def add_match_win(winning_player, losing_player, match):
    # Mark winner
    winning_player.match_wins = winning_player.match_wins + 1
    winning_player.save()

    # No need to increment number of matches for match

    # Increment player stats
    winning_player.player.number_of_matches_won = winning_player.player.number_of_matches_won + 1
    winning_player.save()
    losing_player.player.number_of_matches_won = losing_player.player.number_of_matches_won + 1
    losing_player.save()


def add_set_win(winning_player, losing_player, set):
    # Mark Winner
    winning_player.set_wins = winning_player.set_wins + 1
    winning_player.save()

    # Increment number of sets played
    set.match.num_sets_complete = set.match.num_sets_complete + 1
    set.save()

    # Increment Player Stats
    winning_player.leg_wins = 0
    winning_player.player.number_of_sets_won = winning_player.player.number_of_sets_won + 1
    winning_player.save()
    winning_player.player.save()
    losing_player.leg_wins = 0
    losing_player.player.number_of_sets_lost = losing_player.player.number_of_sets_lost + 1
    losing_player.save()
    losing_player.player.save()


def get_set_by_number(match_id, set_number):
    match = get_match_by_id(match_id=match_id)
    return Set.objects.filter(match=match, set_number=set_number - 1).first()


def get_leg_by_number(match_id, set_number, leg_number):
    darts_set = get_set_by_number(match_id=match_id, set_number=set_number)
    return Leg.objects.filter(set=darts_set, leg_number=leg_number - 1).first()


# Checks if a turn is a bust or not
# Returns true if it is a bust and false if not
def is_turn_bust(turn):
    # Get hits
    hits = DartboardHit.objects.filter(turn=turn)

    # Get the players current score
    score_remaining = turn.player.score_remaining

    # Calculate Score for the turn
    for hit in hits:
        if not hit.is_bounce_out and not hit.is_knock_out:
            score_remaining -= hit.score

    return score_remaining == 1 or score_remaining < 0

# Commits a turn to the database. Returns True if the turn could
# be committed and false if the turn was a bust.
def commit_turn(turn):
    # Get hits
    hits = DartboardHit.objects.filter(turn=turn)

    # Determine if last throw was one that could win
    last_hit = hits[hits.count() - 1]
    is_winnable = last_hit.is_double or last_hit.is_bullseye

    # Get the players current score
    score_remaining = turn.player.score_remaining
    print(score_remaining)

    # Calculate Score for the turn
    score = 0
    for hit in hits:
        if not hit.is_bounce_out and not hit.is_knock_out:
            score += hit.score
            print(str(hit.score) + " " + str(score))
            # Check that this turn wasn't a bust
            if score_remaining - score < 0 or score_remaining - score == 1 or (
                    score_remaining == 0 and not is_winnable):
                turn.is_bust = True
                turn.is_committed = True
                turn.save()
                return False

    # Update Player's leg score
    turn.player.score_remaining -= score
    turn.save()

    # Update Player's In-game statistics
    turn.player.update(hits)
    turn.player.save()

    # Update Player's Lifetime statistics
    turn.player.player.update(hits)
    turn.player.player.save()

    # Show the turn as committed
    turn.is_committed = True
    turn.save()

    return True
