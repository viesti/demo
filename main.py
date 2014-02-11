import sys

def make_greeting(name):
    return "Hello %s!" % name

if __name__ == "__main__":
    # need one argument
    print make_greeting(sys.argv[1])
