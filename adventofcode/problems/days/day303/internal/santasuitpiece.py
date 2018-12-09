class SantaSuitPiece:
    def __init__(self, patch_id, position_x, position_y, size_x, size_y) -> None:
        super().__init__()
        self.id = int(patch_id)
        self.position_x = int(position_x)
        self.position_y = int(position_y)
        self.size_x = int(size_x)
        self.size_y = int(size_y)
