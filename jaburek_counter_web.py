import requests
import argparse
import sys

def main():
    muj_parser = argparse.ArgumentParser(description='Program Vojtěcha Jabůrka, který počítá slova, znaky a řádky z vložené webové stránky')
    muj_parser.add_argument("web", help='Webová stránka ke zpracování:')
    muj_parser.add_argument("--slova", help="Vypise slova", action="store_true" )
    muj_parser.add_argument("--znaky", help="Vypise znaky", action="store_true")
    muj_parser.add_argument("--radky", help="Vypise radky", action="store_true")

    argumenty = muj_parser.parse_args()

    try:
        if argumenty.slova and argumenty.znaky and argumenty.radky:
            web_stranka = requests.get(argumenty.web)
            prevedeni = web_stranka.text
            pocet_znaku = len(prevedeni)
            pocet_radku = prevedeni.count("/n") + 1
            pocet_slov = prevedeni.count(" ") + pocet_radku
            print(f"Text z webové stránky má {pocet_slov} slov, {pocet_znaku} znaků a {pocet_radku} řádků.")

        elif argumenty.slova and argumenty.znaky:
            web_stranka = requests.get(argumenty.web)
            prevedeni = web_stranka.text
            pocet_znaku = len(prevedeni)
            pocet_radku = prevedeni.count("/n") + 1
            pocet_slov = prevedeni.count(" ") + pocet_radku
            print(f"Text z webové stránky má {pocet_slov} slov a {pocet_znaku} znaků.")

        elif argumenty.znaky and argumenty.radky:
            web_stranka = requests.get(argumenty.web)
            prevedeni = web_stranka.text
            pocet_znaku = len(prevedeni)
            pocet_radku = prevedeni.count("/n") + 1
            pocet_slov = prevedeni.count(" ") + pocet_radku
            print(f"Text z webové stránky má {pocet_znaku} znaků a {pocet_radku} řádků.")

        elif argumenty.radky and argumenty.slova:
            web_stranka = requests.get(argumenty.web)
            prevedeni = web_stranka.text
            pocet_znaku = len(prevedeni)
            pocet_radku = prevedeni.count("/n") + 1
            pocet_slov = prevedeni.count(" ") + pocet_radku
            print(f"Text z webové stránky má {pocet_radku} řádků a {pocet_slov} slov.")

        elif argumenty.slova:
            web_stranka = requests.get(argumenty.web)
            prevedeni = web_stranka.text
            pocet_znaku = len(prevedeni)
            pocet_radku = prevedeni.count("\n") + 1
            pocet_slov = prevedeni.count(" ") + pocet_radku
            print(f"Text z webové stránky má {pocet_slov} slov.")

        elif argumenty.znaky:
            web_stranka = requests.get(argumenty.web)
            prevedeni = web_stranka.text
            pocet_znaku = len(prevedeni)
            pocet_radku = prevedeni.count("/n") + 1
            pocet_slov = prevedeni.count(" ") + pocet_radku
            print(f"Text z webové stránky má {pocet_znaku} znaků.")

        elif argumenty.radky:
            web_stranka = requests.get(argumenty.web)
            prevedeni = web_stranka.text
            pocet_znaku = len(prevedeni)
            pocet_radku = prevedeni.count("/n") + 1
            pocet_slov = prevedeni.count(" ") + pocet_radku
            print(f"Text z webové stránky má {pocet_radku} řádků.")

        else:
            web_stranka = requests.get(argumenty.web)
            prevedeni = web_stranka.text
            pocet_znaku = len(prevedeni)
            pocet_radku = prevedeni.count("/n") + 1
            pocet_slov = prevedeni.count(" ") + pocet_radku
            print(f"Text z webové stránky má {pocet_slov} slov, {pocet_znaku} znaků a {pocet_radku} řádků.")

    except:
        print("Chyba při čtení souboru")
        sys.exit()
        
if __name__ == '__main__':
    main()


