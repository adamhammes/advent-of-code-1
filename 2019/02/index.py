#!/usr/bin/env python3

part_1_input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0"

from functions import getOpcodeResult, changeNounAndVerb

def part_one():
    print(
        "Part one's result is:",
        getOpcodeResult(
            changeNounAndVerb(part_1_input, 12, 2)
        ).split(",")[0]
    )

def part_two():
    expected_output = 19690720
    # TODO: make a real reverse noun and verb calculator based on the expected output
    # these values were found by hand...
    noun = 65
    verb = 77
    output = getOpcodeResult(
        changeNounAndVerb(part_1_input, noun, verb)
    )

    print(
        "expected output:", expected_output, 
        "noun:", noun,
        "verb:", verb,
        "output:", output.split(",")[0]
    )

if __name__ == "__main__":
    part_one()
    part_two()
