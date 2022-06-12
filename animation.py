# Example output: 
# .-'¯    _,.-'¯    _,.-'¯    _,.-'¯    _,.-'¯    | your message here |.,_    ¯'-.,_    ¯'-.,_    ¯'-.,_    ¯'-.,_    ¯
# The things next to the message are animated and moving. 

import time
import sys
import os


def wait():
    _, cols = os.popen('stty size', 'r').read().split()
    cols = int(cols)

    # You can choose or create a different animation pattern: 
    # chars = "_.~\"|"
    # chars = "\"`-._,-'"
    # chars = """|/-.-\\|/-'-\\"""
    # chars = """|/-\\|/-\\"""
    chars = "_,.-'¯    "

    message = "| your message here |"
    cols -= len(message)
    half_cols = int(cols/2)

    for i in range(100000):
        time.sleep(0.07)
        sys.stdout.write("\r" +
            "".join([chars[(i + j) % len(chars)] for j in range(half_cols)]) +
            message +
            "".join([chars[(i - j) % len(chars)] for j in range(half_cols)])
        )
        sys.stdout.flush()
    # print("")  # uncomment this line to print many lines, filling up the whole screen.


wait()