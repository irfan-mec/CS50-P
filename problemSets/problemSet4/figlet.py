import sys
import random
import pyfiglet

def main():
    
    if len(sys.argv) not in [1, 3]:
        sys.exit("Usage: figlet.py [-f FONT | --font FONT]")


    if len(sys.argv) == 3:
        if sys.argv[1] not in ['-f', '--font']:
            sys.exit("Usage: figlet.py [-f FONT | --font FONT]")
        font = sys.argv[2]
        try:

            pyfiglet.FigletFont.getFonts().index(font)
        except ValueError:
            sys.exit("Invalid font name. Please provide a valid font.")
    else:

        font = random.choice(pyfiglet.FigletFont.getFonts())


    text = input("Input: ")


    figlet = pyfiglet.Figlet(font=font)


    print(figlet.renderText(text))

if __name__ == "__main__":
    main()