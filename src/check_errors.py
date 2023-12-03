from src.utils import help

def check_args(ac, av):
    if ac == 2 and av[1] == "-h":
        help()
        exit(0)
    if ac != 3:
        raise Exception("ERROR: The number of arguments must be 3.")
    if ((not av[1].isnumeric()) or int(av[1]) < 50) or ((not av[2].isnumeric()) or int(av[2]) < 50):
        raise Exception("ERROR: The args must number and need to be >= 50.")