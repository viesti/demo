# A great demo effect
import sys

def make_greeting(name):
    return "Hello %s!!" % name

if __name__ == "__main__":
    for name in sys.argv[1:]:
        print make_greeting(name)
