import sys

def make_greeting(name):
    return "Hello %s!!" % name

def make_another_greeting(name):
    return "What's the clock %s!" % name

if __name__ == "__main__":
    for name in sys.argv[1:]:
        print make_greeting(name)
        print make_another_greeting(name)
