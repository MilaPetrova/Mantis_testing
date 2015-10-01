from sys import maxsize

class MyProject:
    def __init__(self, name=None, status=None, view_status=None, id=None, description=None):
        self.name = name
        self.status = status
        self.view_status = view_status
        self.id = id
        self.description = description

    def __repr__(self):
        return "%s" % (self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)and self.name == other.name



    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

