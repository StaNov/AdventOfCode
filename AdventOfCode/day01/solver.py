# -*- coding: utf-8 -*-
from marshaller import Marshaller, MarshallerController


def solve_1(input_string):
    marshaller = Marshaller()
    controller = MarshallerController(marshaller)

    for instruction in input_string.split(", "):
        controller.execute_instruction(instruction)

    return marshaller.steps_from_start()
