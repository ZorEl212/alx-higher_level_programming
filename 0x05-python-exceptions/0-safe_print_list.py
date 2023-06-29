#!/usr/bin/python3
if __name__ == "__main__":
    def safe_print_list(my_list=[], x=0):
        i = 0
        for i in range(0, x):
            try:
                print("{}".format(my_list[i]), end="")
                i= i+1
            except IndexError:
                print()
                return i
        print()
        return i
        
