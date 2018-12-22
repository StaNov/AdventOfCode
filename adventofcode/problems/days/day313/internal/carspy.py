class CarSpy:
    POSITION_NOT_SPECIFIED = (-1, -1)

    def __init__(self, position=POSITION_NOT_SPECIFIED):
        super().__init__()
        self.position = position
        self.moved = False
        self.those_must_move_after_this = []
        self.those_must_move_before_this = []

    def move(self):
        self.moved = True

        self.position = (
            self.position[0] + 1,
            self.position[1] + 1
        )

        for before in self.those_must_move_before_this:
            assert before.moved, "Not all cars were moved that should move before this one."

        for after in self.those_must_move_after_this:
            assert not after.moved, "Some car was incorrectly moved before this one."

    def can_move_only_before(self, before):
        self.those_must_move_after_this = before

    def can_move_only_after(self, after):
        self.those_must_move_before_this = after
