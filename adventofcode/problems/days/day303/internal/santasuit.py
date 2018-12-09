class SantaSuit:
    def __init__(self):
        self.suit = {}
        self.intact_patches = set()

    def saw_patch(self, patch):
        self.intact_patches.add(patch.id)

        for i in range(patch.position_x, patch.position_x + patch.size_x):
            for j in range(patch.position_y, patch.position_y + patch.size_y):
                current_patch_id, current_count = self.suit.get((i, j), (None, 0))
                self.suit[(i, j)] = patch.id, current_count + 1

                if current_patch_id is not None:
                    self.intact_patches.discard(current_patch_id)
                    self.intact_patches.discard(patch.id)

    def get_overlapping_count(self):
        return len(list(filter(lambda id_and_count: id_and_count[1] > 1, self.suit.values())))

    def get_intact_patch_id(self):
        return list(self.intact_patches)[0]
