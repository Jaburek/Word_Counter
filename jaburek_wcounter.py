import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Counter')
    parser.add_argument('soubor_')
    parser.add_argument("--znaky", help="Vypis znaky", action="store_true")
    parser.add_argument("--slova", help="Vypis slova", action="store_true")
    parser.add_argument("--radky", help="Vypis řádky", action="store_true")
    args = parser.parse_args()

    try:
        f = open(args.soubor_, "r")
        soubor_ = f.read()
        lamp = False
        if args.slova:
            pocet_slov = slova_counter(soubor_)
            print(f"Pocet slov: {pocet_slov}")
            lamp = True
        if args.radky:
            pocet_radku = radky_counter(soubor_)
            print(f"Pocet radku: {pocet_radku}")
            lamp = True
        if args.znaky:
            pocet_znaku = znaky_counter(soubor_)
            print(f"Pocet znaku: {pocet_znaku}")
            lamp = True
        if not lamp:
            pocet_slov = slova_counter(soubor_)
            pocet_znaku = znaky_counter(soubor_)
            pocet_radku = radky_counter(soubor_)
            print(f"Pocet slov: {pocet_slov}\nPocet znaku: {pocet_znaku}\nPocet radku: {pocet_radku}")
    except:
        print("Nastala chyba")
        sys.exit(1)

def slova_counter(f):
    pocet_slov = f.count(' ') + len(f.split('\n'))
    return pocet_slov
    pass
def znaky_counter(f):
    pocet_znaku = len(f)
    return pocet_znaku
def radky_counter(f):
    pocet_radku = len(f.split('\n'))
    return pocet_radku

main ()