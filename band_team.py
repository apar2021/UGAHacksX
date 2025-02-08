class BandTeam:
    def __init__(self, name, goals, looking_for, members, member_count, _id=None):
        if _id:
            self._id = _id
        self.name = name
        self.goals = goals
        self.looking_for = looking_for
        self.members = members
        self.member_count = member_count