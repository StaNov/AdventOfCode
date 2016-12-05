class TriangleChecker:
    @staticmethod
    def check(x, y, z):
        return x + y > z and x + z > y and y + z > x