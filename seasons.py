from datetime import datetime


class Season:
    def __init__(self, name,copmetion_type, start_date, end_date, venue, num_players):
        self.name = name
        self.copmetion_type=copmetion_type
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.venue = venue
        self.num_players = num_players

    def __repr__(self):
         return f'Season("{self.name}", "{self.start_date}", "{self.end_date}", "{self.venue}", {self.num_players})'

def create_seasons():
    seasons = [    
        Season("Wimbledon Men Singles 2023","grand slam", "2023-06-26", "2023-07-16", "AELTC Wimbledon", 128),
        Season("ATP Paris, France Men Singles 2023","atp_1000", "2023-10-28", "2023-11-05", "Accor Arena", 64),
        Season("ATP Doha, Qatar Men Singles 2024","atp_500", "2024-02-17", "2024-02-24", "Khalifa International", 32),
        Season("ATP Brisbane, Australia Men Singles 2024","atp_250", "2023-12-30", "2024-01-07", "Queensland Tennis Centre", 16),
    ]
    return seasons
