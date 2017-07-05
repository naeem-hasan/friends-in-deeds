class Friend(object):
    def __init__(self, name, reactions, comments):
        self.name = name
        self.reactions = reactions
        self.comments = comments

    def __str__(self):
        return self.name


class FriendsData(object):
    def __init__(self):
        self.friends = []

    def add_friend(self, name, t):
        if name == "Naeem Hasan":
            return
        found = False
        for friend in self.friends:
            if friend.name == name:
                if t == "REACTION":
                    friend.reactions += 1
                elif t == "COMMENT":
                    friend.comments += 1
                else:
                    pass
                found = True
                break

        if not found:
            self.friends.append(Friend(name, 0, 0))
            self.add_friend(name, t)

    def print_(self):
        for friend in self.friends:
            print "{}\t\t\t\t{}\t\t\t\t{}".format(friend.name.encode("utf-8"), friend.comments, friend.reactions)

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write("{}\t\t{}\t\t{}\n".format("Name", "Comments", "Reactions"))
            for friend in self.friends:
                f.write("{}\t\t{}\t\t{}\n".format(friend.name.encode("utf-8"), friend.comments, friend.reactions))
            f.close()

    def save_csv(self, filename):
        with open(filename, 'w') as f:
            f.write("{},{},{},{}\n".format("Name", "Comments", "Reactions", "Total"))
            for friend in self.friends:
                f.write("{},{},{},{}\n".format(friend.name.encode("utf-8"), friend.comments, friend.reactions, friend.comments + friend.reactions))
            f.close()
