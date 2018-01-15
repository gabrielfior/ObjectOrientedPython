import random
some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("Raising {}".format(choice))
    if choice:
        raise choice("An error")
# catching raised exceptions
except ValueError:
    print("caught value error")
except TypeError:
    print("caught type error")
except Exception as e:
    print("caught some other error: %s " %(e.__class__.__name__))

else:
    print("Code is called if there is no exception")
finally:
    print("This cleanup code is always called")

