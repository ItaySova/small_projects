def command_parser(obj, command, args):
    try:
        func = getattr(obj, command)
    except AttributeError:
        print('function not found')
        return
    res = func(*args)
    return res


def main():
    pass


if __name__ == "__main__":
    main()
