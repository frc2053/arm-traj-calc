# Copyright (c) 2023 FRC 6328
# http://github.com/Mechanical-Advantage
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file at
# the root directory of this project.

import json

from plotter import plot
from solver import Solver
from math import pi, radians

if __name__ == "__main__":
    config = json.loads(open("arm_config.json", "r").read())
    solver = Solver(config)

    # start to high cone
    request = {
        "initial": [0, -pi/2],
        "final": [radians(130), radians(30)],
        "constraintOverrides": []
    }

    # start to mid cone
    # request = {
    #     "initial": [0, -pi/2],
    #     "final": [radians(100), radians(120)],
    #     "constraintOverrides": []
    # }

    # start to low area
    # request = {
    #     "initial": [0, -pi/2],
    #     "final": [radians(250), radians(-45)],
    #     "constraintOverrides": []
    # }

    # low to mid
    # request = {
    #     "initial": [radians(250), radians(-45)],
    #     "final": [radians(100), radians(120)],
    #     "constraintOverrides": []
    # }

    # low to high
    # request = {
    #     "initial": [radians(250), radians(-45)],
    #     "final": [radians(135), radians(30)],
    #     "constraintOverrides": []
    # }

    # stowed to human station
    # request = {
    #     "initial": [0, -pi/2],
    #     "final": [0, radians(10)],
    #     "constraintOverrides": []
    # }

    result = solver.solve(request)

    if result != None:
        print("DT =", result[0] / (len(result[1]) - 1))
        plot(result, config)