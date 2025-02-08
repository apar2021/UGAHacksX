class RockMember:
    def __init__(self, username, password, name, genre, instruments, collaboration_type, teams, _id=None):
        if _id:
            self._id = _id
        self.username = username
        self.password = password
        self.name = name
        self.genre=genre
        self.instruments = instruments
        self.collaboration_type = collaboration_type
        # self.social_links = social_links
        self.teams = teams

class RockTeam:
    def __init__(self, name, goals, looking_for, members, member_count, _id=None):
        if _id:
            self._id = _id
        self.name = name
        self.goals = goals
        self.looking_for = looking_for
        self.members = members
        self.member_count = member_count