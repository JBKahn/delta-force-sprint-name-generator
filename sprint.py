import os
import random

if __name__ == "__main__":
    print "Operation {} {}".format(
        random.choice(open(os.path.dirname(os.path.abspath(__file__)) + "/adjectives.txt", "r").readlines()).strip().capitalize(),
        random.choice(open(os.path.dirname(os.path.abspath(__file__)) + "/nouns.txt", "r").readlines()).strip().capitalize(),
    )
