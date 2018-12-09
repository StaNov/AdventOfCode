class SantaSuit:
    def __init__(self):
        self.suit = {}

    def saw_patch(self, patch):
        for i in range(patch.position_x, patch.position_x + patch.size_x):
            for j in range(patch.position_y, patch.position_y + patch.size_y):
                current = self.suit.get((i, j), 0)
                self.suit[(i, j)] = current + 1

    def get_overlapping_count(self):
        return len(list(filter(lambda x: x > 1, self.suit.values())))

    def get_intact_patch_id(self):
        return 1
