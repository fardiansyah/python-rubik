import sys
import os
import re
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Move import Move
from Printer import TtyPrinter, OpenGLPrinter
from Solver.Kociemba import KociembaSolver
from Solver.Beginner import BeginnerSolver
from Cubie import Cube
from NaiveCube import NaiveCube
from Move import Move

if __name__ == '__main__':
    c = Cube(3)
    p = OpenGLPrinter(c)
    tp = TtyPrinter(c, True)
    c.shuffle()
    # nc = NaiveCube()
    # nc.set_cube("OYOYYOGRRBRRGBWRGGWBBRRBYWBWYGOGBOWBWGWYOWYRGOBYOWOYGR")
    # c.from_naive_cube(nc)
    p.pprint()
    tp.pprint()

    solver = KociembaSolver(c)

    while True:
        m = raw_input('Input move: ')
        if re.match("[RLBFUDXYZ]'?2?", m, re.I):
            c.move(Move(m))
            tp.pprint()
        elif m.upper() == 'SH':
            print "Shuffling"
            c.shuffle()
        elif m.upper() == 'S':
            print "Solving"
            solution = solver.solution()
            print "Solution:", ' '.join(str(m) for m in solution)
            for m in solution:
                # time.sleep(1)
                c.move(m)
            tp.pprint()
            print "SOLVED!"
        elif m.upper() == 'Q':
            print "Bye"
            p.stop()
            break
        else:
            print "Invalid move, try one of R, L, B, F, U, D, X, Y, Z, SH, S"
