import argparse

# 命令行模块
def Terminal():
    parser = argparse.ArgumentParser(
        description="e.g：python fofa_api.py --search IP or domain\t python fofa_api.py --search \"domain=xx.com\" or \"city=Beijing\"",
        prog="fofa_api.py")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--version", "-V", help="Show version of Fofa_API", action='version',
                       version="| %(prog)s v1.2 |")
    group.add_argument("--search", "-S", help="Search key word", type=str)
    group.add_argument("--rule", help="Query fofa syntax rules(only Fofa)", action="store_true")
    group.add_argument("--information", help="Query fofa information(only Fofa)", action="store_true")
    parser.add_argument("--size", help="Show the number of results.(default=100)", default=100)
    parser.add_argument("--page", help="Show the page of results.(default=1)", default=1)
    # parser.add_argument('word_search', help="search key word")
    args = parser.parse_args()
    if args.search:
        return args.search, args.size, args.page
    else:
        if args.rule:
            return args.rule, -1, -2
        else:
            if args.information:
                return args.information, -2, -1
            else:
                print("\nusage: main.py -h, --help          show help message and exit")
                return 0, 0, 0