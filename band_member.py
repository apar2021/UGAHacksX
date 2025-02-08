class BandMember:
    def __init__(self, username, password, name, instruments, collaboration_type, social_links, teams, _id=None):
        if _id:
            self._id = _id
        self.username = username
        self.password = password
        self.name = name
        self.instruments = instruments
        self.collaboration_type = collaboration_type
        self.social_links = social_links
        self.teams = teams