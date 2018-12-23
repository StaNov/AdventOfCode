class CarSpy:
    def __init__(self, position=(-1, -1), move_by=(0, 0)):
        super().__init__()
        self.position = position
        self.move_by = move_by
        self.moved = False
        self.turned = False
        self.those_must_move_after_this = []
        self.those_must_move_before_this = []

    def move(self):
        self.moved = True

        self.position = tuple(map(sum, zip(self.position, self.move_by)))

        for before in self.those_must_move_before_this:
            assert before.moved, "Not all cars were moved that should move before this one."

        for after in self.those_must_move_after_this:
            assert not after.moved, "Some car was incorrectly moved before this one."

    def turn(self, road_type):
        self.turned = True

    def can_move_only_before(self, before):
        self.those_must_move_after_this = before

    def can_move_only_after(self, after):
        self.those_must_move_before_this = after
