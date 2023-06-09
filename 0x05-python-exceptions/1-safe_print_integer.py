#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return False
    else:
        return True


if __name__ == "__main__":
    safe_print_integer()
