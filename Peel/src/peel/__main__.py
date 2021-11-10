from sys import argv

def main(args):
    if len(args) > 1:
        print()
    elif len(args) == 1:
        run_file(args[0]
    else:
        run_prompt()
