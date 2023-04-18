class MessageCounter:
    def __init__(self):
        self.total_count = 0

    def increment(self):
        self.total_count += 1

    def get_count(self):
        return self.total_count
