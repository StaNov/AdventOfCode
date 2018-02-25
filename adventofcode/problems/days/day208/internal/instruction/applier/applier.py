class Applier:
    def __init__(self, register_name, value_to_apply) -> None:
        self._register_name = register_name
        self._value_to_apply = value_to_apply

    def apply_on_registers(self, registers):
        registers.add(self._register_name, self._value_to_apply)
