class Registers:
    def __init__(self) -> None:
        self._registers = {}

    def get(self, name):
        self._initialize_register_if_untouched(name)
        return self._registers[name]

    def add(self, name, value):
        self._initialize_register_if_untouched(name)
        self._registers[name] += value

    def _initialize_register_if_untouched(self, name):
        if name not in self._registers:
            self._registers[name] = 0

    @property
    def registers(self):
        return set(self._registers.items())
