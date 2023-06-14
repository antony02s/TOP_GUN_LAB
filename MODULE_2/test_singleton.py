from module_version import SingletonTest


def main():
    sin_1 = SingletonTest()
    sin_2 = SingletonTest()

    print(sin_1 == sin_2)
    print(sin_1 is sin_2)


if __name__ == '__main__':
    main()
