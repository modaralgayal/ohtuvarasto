"""Importing varasto."""

from varasto import Varasto

def main():

    """ Main function to demontrate proportions """

    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(mehua)
    print(olutta)


if __name__ == "__main__":
    main()
