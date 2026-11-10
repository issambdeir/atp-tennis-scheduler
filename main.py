import random
from datetime import timedelta

from players import create_players
from seasons import create_seasons


def get_user_choice(seasons):
    print("Choose a season to test the scheduler:")
    for i, season in enumerate(seasons):
        print(f"{i + 1}. {season.name} (Type: {season.copmetion_type})")

    choice = int(input("Enter the number corresponding to your choice: ")) - 1
    return seasons[choice]


def fetch_random_players(players, num_players):
    return random.sample(players, num_players)


def divide_players(players, competition_type):
    if competition_type == "grand slam":
        seeded_count = 32
        total_players = 128
    elif competition_type == "atp_1000":
        seeded_count = 16
        total_players = 64
    elif competition_type == "atp_500":
        seeded_count = 8
        total_players = 32
    elif competition_type == "atp_250":
        seeded_count = 4
        total_players = 16
    else:
        seeded_count = 0
        total_players = len(players)

    # Sort players by rank and separate seeded and unseeded
    players_sorted = sorted(players, key=lambda x: x.rank, reverse=True)
    seeded_players = players_sorted[:seeded_count]
    unseeded_players = players_sorted[seeded_count:]

    return seeded_players, unseeded_players, total_players


def place_seeded_players(seeded_players, total_players, competition_type):
    draw = [None] * total_players

    # Place top 2 seeds
    draw[0] = seeded_players[0]  # Seed 1 goes to the first position
    draw[-1] = seeded_players[1]  # Seed 2 goes to the last position

    if competition_type == "grand slam":
        half_1_positions = list(set(range(33, 64)))
        half_2_positions = list(set(range(65, 96)))

        pos_3 = random.choice(half_1_positions)
        draw[pos_3] = seeded_players[2]  # Seed 3

        pos_4 = random.choice(half_2_positions)
        draw[pos_4] = seeded_players[3]  # Seed 4

        # Place seeds 5-8 in their respective quarters
        # Define ranges separately
        ranges = [
            range(9, 16),  # Range 9-15
            range(17, 24),  # Range 17-23
            range(25, 32),  # Range 25-31
            range(97, 104),  # Range 97-103
        ]
        for i in range(4, 8):
            empty = False
            quarter_positions = list(set().union(*ranges))

            while not empty:
                pos = random.choice(quarter_positions)
                if draw[pos] is None:
                    draw[pos] = seeded_players[i]  # Seeds 5-8
                    empty = True

                    # Determine which range the selected position belongs to and remove that entire range
                    for r in ranges:
                        if pos in r:
                            ranges.remove(r)  # Remove the entire range
                            break  # Exit the loop after removing the range

        ranges = [
            range(41, 48),
            range(49, 56),
            range(57, 64),
            range(65, 72),
            range(73, 80),
            range(81, 88),
            range(89, 96),
            range(97, 104),
        ]
        # Place seeds 9-16 in respective 1/8th sections
        for i in range(8, 16):
            empty = False
            section_positions = list(set().union(*ranges))

            while not empty:
                pos = random.choice(section_positions)
                if draw[pos] is None:
                    draw[pos] = seeded_players[i]  # Seeds 5-8
                    empty = True

                    # Determine which range the selected position belongs to and remove that entire range
                    for r in ranges:
                        if pos in r:
                            ranges.remove(r)  # Remove the entire range
                            break  # Exit the loop after removing the range

        # Place seeds 17-32 in respective 1/16th sections
        ranges = [
            range(2, 8),
            range(9, 16),
            range(17, 24),
            range(25, 32),
            range(33, 40),
            range(41, 48),
            range(49, 56),
            range(57, 64),
            range(65, 72),
            range(49, 56),
            range(73, 80),
            range(81, 88),
            range(89, 96),
            range(97, 104),
            range(105, 112),
            range(113, 120),
            range(121, 126),
        ]
        for i in range(16, 32):
            empty = False
            sixteenth_positions = list(set().union(*ranges))

            while not empty:
                pos = random.choice(sixteenth_positions)
                if draw[pos] is None:
                    draw[pos] = seeded_players[i]  # Seeds 5-8
                    empty = True

                    # Determine which range the selected position belongs to and remove that entire range
                    for r in ranges:
                        if pos in r:
                            ranges.remove(r)  # Remove the entire range
                            break  # Exit the loop after removing the range

    elif competition_type == "atp_1000":
        half_1_positions = list(set(range(17, 32)))
        half_2_positions = list(set(range(33, 48)))

        pos_3 = random.choice(half_1_positions)
        draw[pos_3] = seeded_players[2]  # Seed 3

        pos_4 = random.choice(half_2_positions)
        draw[pos_4] = seeded_players[3]  # Seed 4

        # Place seeds 5-8 in respective quarters
        ranges = [
            range(9, 16),  # Range 9-15
            range(25, 32),  # Range 17-23
            range(33, 40),  # Range 25-31
            range(41, 48),  # Range 97-103
        ]
        for i in range(4, 8):
            empty = False
            quarter_positions = list(set().union(*ranges))

            while not empty:
                pos = random.choice(quarter_positions)
                if draw[pos] is None:
                    draw[pos] = seeded_players[i]  # Seeds 5-8
                    empty = True

                    # Determine which range the selected position belongs to and remove that entire range
                    for r in ranges:
                        if pos in r:
                            ranges.remove(r)  # Remove the entire range
                            break  # Exit the loop after removing the range

        # Place seeds 9-16 in respective 1/8th sections
        ranges = [
            range(2, 8),
            range(9, 16),
            range(17, 24),
            range(25, 32),
            range(33, 40),
            range(41, 48),
            range(49, 56),
            range(57, 62),
        ]
        for i in range(8, 16):
            empty = False
            section_positions = list(set().union(*ranges))

            while not empty:
                pos = random.choice(section_positions)
                if draw[pos] is None:
                    draw[pos] = seeded_players[i]  # Seeds 5-8
                    empty = True

                    # Determine which range the selected position belongs to and remove that entire range
                    for r in ranges:
                        if pos in r:
                            ranges.remove(r)  # Remove the entire range
                            break  # Exit the loop after removing the range

    elif competition_type == "atp_500":
        half_1_positions = list(set(range(9, 16)))
        half_2_positions = list(set(range(17, 24)))

        pos_3 = random.choice(half_1_positions)
        draw[pos_3] = seeded_players[2]  # Seed 3

        pos_4 = random.choice(half_2_positions)
        draw[pos_4] = seeded_players[3]  # Seed 4

        # Place seeds 5-8 in their quarters
        # Define ranges separately
        ranges = [
            range(2, 8),  # Range 9-15
            range(9, 16),  # Range 17-23
            range(17, 24),  # Range 25-31
            range(25, 31),  # Range 97-103
        ]
        for i in range(4, 8):
            empty = False
            quarter_positions = list(set().union(*ranges))

            while not empty:
                pos = random.choice(quarter_positions)
                if draw[pos] is None:
                    draw[pos] = seeded_players[i]  # Seeds 5-8
                    empty = True

                    # Determine which range the selected position belongs to and remove that entire range
                    for r in ranges:
                        if pos in r:
                            ranges.remove(r)  # Remove the entire range
                            break  # Exit the loop after removing the range

    elif competition_type == "atp_250":
        half_1_positions = list(set(range(5, 8)))
        half_2_positions = list(set(range(9, 12)))

        pos_3 = random.choice(half_1_positions)
        draw[pos_3] = seeded_players[2]  # Seed 3

        pos_4 = random.choice(half_2_positions)
        draw[pos_4] = seeded_players[3]  # Seed 4

    return draw


def fill_unseeded_players(draw, unseeded_players):
    # Fill remaining slots with unseeded players

    # Shuffle the list of unseeded players to randomize their order
    random.shuffle(unseeded_players)

    for player in unseeded_players:
        for i in range(len(draw)):
            if draw[i] is None:
                draw[i] = player
                break  # Move on to the next unseeded player after placing the current one

    return draw


def schedule_matches(seeded_players, unseeded_players, total_players, competition_type):
    # Create the draw by placing seeded players first
    draw = place_seeded_players(seeded_players, total_players, competition_type)

    # Fill remaining slots with unseeded players
    draw = fill_unseeded_players(draw, unseeded_players)

    # Pair adjacent players for matches
    matches = [(draw[i], draw[i + 1]) for i in range(0, total_players, 2)]

    return matches


def schedule_match_with_details(matches, season, num_courts):
    scheduled_matches = []
    current_date = season.start_date  # Get the start date from the season object
    court_availabilities = [i + 1 for i in range(num_courts)]  # List of court numbers

    # Assuming matches are scheduled across 4 time slots per day
    time_slots = ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM"]

    # Calculate the number of matches in round 1
    total_matches = len(
        matches
    )  # Total number of matches (e.g., 64 in a grand slam round 1)

    # Calculate the number of matches per day based on available courts
    matches_per_day = num_courts * len(
        time_slots
    )  # For 16 courts, 4 slots = 64 matches per day
    days_needed = total_matches // matches_per_day + (
        1 if total_matches % matches_per_day != 0 else 0
    )

    match_counter = 0  # to track the match number as we go through the days

    for day in range(days_needed):
        # assign matches for the day
        remaining_matches_today = min(matches_per_day, total_matches - match_counter)

        # Assign the matches
        for match in matches[match_counter : match_counter + remaining_matches_today]:
            court = random.choice(court_availabilities)
            time = random.choice(time_slots)

            scheduled_matches.append(
                {
                    "players": (match[0], match[1]),
                    "court": court,
                    "time": time,
                    "date": current_date.strftime("%Y-%m-%d"),
                }
            )

            # Remove time slot once it's assigned
            time_slots.remove(time)

            # If no time slots left, move to the next day
            if len(time_slots) == 0:
                time_slots = [
                    "10:00 AM",
                    "1:00 PM",
                    "4:00 PM",
                    "7:00 PM",
                ]  # Reset time slots
                current_date += timedelta(days=1)  # Proceed to the next day

        # Move to the next day
        current_date += timedelta(days=1)
        match_counter += remaining_matches_today

    return scheduled_matches


def adjust_matches_for_seeded_preferences(
    scheduled_matches, seeded_players, competition_type
):
    # seeded_players_copy=seeded_players
    # compare seeds 1 and 2
    scheduled_matches, switched = switch_players(
        scheduled_matches, seeded_players, 0, 1
    )

    # compare seeds 3 and 4
    scheduled_matches, switched = switch_players(
        scheduled_matches, seeded_players, 2, 3
    )

    if competition_type == "grand slam":
        # compare seeds 5 to 8
        for i in range(4, 7):
            for y in range(i + 1, 8):
                scheduled_matches, switched = switch_players(
                    scheduled_matches, seeded_players, i, y
                )
                if switched:
                    break

        # compare seeds 9 to 16
        for i in range(8, 15):
            for y in range(i + 1, 16):
                scheduled_matches, switched = switch_players(
                    scheduled_matches, seeded_players, i, y
                )
                if switched:
                    break

        # compare seeds 17 to 32
        for i in range(16, 31):
            for y in range(i + 1, 32):
                scheduled_matches, switched = switch_players(
                    scheduled_matches, seeded_players, i, y
                )
                if switched:
                    break

    elif competition_type == "atp_1000":
        # compare seeds 5 to 8
        for i in range(4, 7):
            for y in range(i + 1, 8):
                scheduled_matches, switched = switch_players(
                    scheduled_matches, seeded_players, i, y
                )
                if switched:
                    break

        # compare seeds 9 to 16
        for i in range(8, 15):
            for y in range(i + 1, 16):
                scheduled_matches, switched = switch_players(
                    scheduled_matches, seeded_players, i, y
                )
                if switched:
                    break

    elif competition_type == "atp_500":
        # compare seeds 5 to 8
        for i in range(4, 7):
            for y in range(i + 1, 8):
                scheduled_matches, switched = switch_players(
                    scheduled_matches, seeded_players, i, y
                )
                if switched:
                    break

    return scheduled_matches


def adjust_matches_for_unseeded_preferences(
    scheduled_matches, unseeded_players, competition_type
):
    # compare seeds 5 to 8
    for i in range(0, len(unseeded_players) - 1):
        for y in range(i + 1, len(unseeded_players)):
            scheduled_matches, switched = switch_players(
                scheduled_matches, unseeded_players, i, y
            )
            if switched:
                break

    return scheduled_matches


def switch_players(scheduled_matches, seeded_players, x, y):
    switched = False
    for i, match in enumerate(scheduled_matches):
        # Check if the top seed (seededPlayers[0]) is in the current match
        if seeded_players[x] in match["players"]:
            # If the player's preferred weather matches the match weather
            if (
                seeded_players[x].preferred_weather != match["weather"]
                and seeded_players[x].preferred_time != match["time_of_day"]
            ):
                # Now search for seededPlayers[1] in another match to swap them
                for j, other_match in enumerate(scheduled_matches):
                    if seeded_players[y] in other_match["players"]:
                        # Check if seededPlayers[1]'s preferred weather is not already in the match
                        if (
                            seeded_players[y].preferred_weather
                            != other_match["weather"]
                            and seeded_players[y].preferred_time
                            != other_match["time_of_day"]
                        ):
                            # Perform the switch
                            # Get the index of each player in their respective match
                            if (
                                seeded_players[x] in match["players"]
                                and seeded_players[y] in other_match["players"]
                            ):
                                player_1_index = match["players"].index(
                                    seeded_players[x]
                                )
                                player_2_index = other_match["players"].index(
                                    seeded_players[y]
                                )

                                # Convert the 'players' tuple to a list for both matches
                                players_i = list(scheduled_matches[i]["players"])
                                players_j = list(scheduled_matches[j]["players"])

                                # Swap the players between the two matches
                                players_i[player_1_index], players_j[player_2_index] = (
                                    players_j[player_2_index],
                                    players_i[player_1_index],
                                )

                                # convert the lists back to tuples and assign them back to the matches
                                scheduled_matches[i]["players"] = tuple(players_i)
                                scheduled_matches[j]["players"] = tuple(players_j)

                                switched = True
                            else:
                                break
                        else:
                            break
            else:
                break

    return scheduled_matches, switched


def fetch_weather_data(scheduledMatches):
    for match in scheduledMatches:
        match["weather"] = random.choice(["Sunny", "Cloudy", "Rainy", "Windy"])

    return scheduledMatches


def assign_time_of_day(scheduled_matches):
    for match in scheduled_matches:
        time = match["time"]

        if "10:00 AM" in time:
            match["time_of_day"] = "Morning"
        elif "1:00 PM" in time:
            match["time_of_day"] = "Afternoon"
        elif "4:00 PM" in time:
            match["time_of_day"] = "Evening"
        elif "7:00 PM" in time:
            match["time_of_day"] = "Night"

    return scheduled_matches


def main():
    # get the seasons
    seasons = create_seasons()
    # get the players
    players = create_players()
    # let the user choose the season
    chosen_season = get_user_choice(seasons)

    # Fetch the required number of players
    selected_players = fetch_random_players(players, chosen_season.num_players)

    # Divide players into seeded and unseeded
    seeded_players, unseeded_players, total_players = divide_players(
        selected_players, chosen_season.copmetion_type
    )

    # Schedule matches
    matches = schedule_matches(
        seeded_players, unseeded_players, total_players, chosen_season.copmetion_type
    )

    # Determine number of courts based on the competition type
    if chosen_season.copmetion_type == "grand slam":
        num_courts = 16
    elif chosen_season.copmetion_type == "atp_1000":
        num_courts = 12
    elif chosen_season.copmetion_type == "atp_500":
        num_courts = 8
    elif chosen_season.copmetion_type == "atp_250":
        num_courts = 4
    else:
        num_courts = 4  # Default value, in case of unrecognized competition type

    # send matches to the scheduling function to assign date, time, and court
    scheduled_matches = schedule_match_with_details(matches, chosen_season, num_courts)

    # send matches to the scheduling function to check the weather for each match
    scheduled_matches = fetch_weather_data(scheduled_matches)

    # send matches to the scheduling function to assign time of matches
    scheduled_matches = assign_time_of_day(scheduled_matches)

    # send matches to the scheduling function to reorder the matches depending on the factors for seede players
    scheduled_matches = adjust_matches_for_seeded_preferences(
        scheduled_matches, seeded_players, chosen_season.copmetion_type
    )

    # send matches to the scheduling function to reorder the matches depending on the factors for unseeded players
    scheduled_matches = adjust_matches_for_unseeded_preferences(
        scheduled_matches, seeded_players, chosen_season.copmetion_type
    )

    # veiw matches
    for match in scheduled_matches:
        print(f"Match: {match['players'][0].name} vs {match['players'][1].name}")
        print(
            f"Date: {match['date']} | Time: {match['time']} | Court: {match['court']} | Weather: {match['weather']}"
        )
        print("-" * 40)


if __name__ == "__main__":
    main()
