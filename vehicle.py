class Vehicle:
    def __init__(self, id):
        self.rides_taken = []
        self.id = id
        self.cur_position = [0, 0]
        self.target_position = None

    def end_trip_if_done(self):
        if not self.target_position: return False
        if self.target_position[0] == self.cur_position[0] and self.target_position[1] == self.cur_position[1]:
            self.target_position = None
            return True
        else:
            return False