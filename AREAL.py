from cgi import print_arguments
from inspect import Parameter
import os

# Funksjon for å tømme terminalen
def clear():
    os.system('cls')

# Funskjon for å skrive hovedmenyen til skjerm
def skriv_meny():
    print("\nHovedmeny for beregning av areal\n")
    print("1. Beregn areal for kvadrat")
    print("2. Beregn areal for rektangel")
    print("3. Beregn areal for trekant")
    print("4. Beregn areal for parallellogram")
    print("5. Beregn areal for rombe")
    print("6. Beregn areal for trapes")
    print("7. Beregn areal for sirkel")
    print("8. Avslutt")


# Funksjon for å beregne arealet av et kvadrat skrives her. Funsjonen skal ta imot et parameter (s)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen
def kvadrat(s):
    return s*s

# Funksjon for å beregne arealet av et rektangel skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen

def rektangel(g,h):
    return g*h

# Funksjon for å beregne arealet av en trekant skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen

def trekant(g,h):
    return g*h/2

# Funksjon for å beregne arealet av et parallellogram skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen

def parallellogram(g,h):
    return g*h

# Funksjon for å beregne arealet av en rombe skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 2 har ansvaret for å lage denne funksjonen


# Funksjon for å beregne arealet av en trapes skrives her. Funsjonen skal ta imot tre parameter (a, b og h)
# Funksjonen skal returnere arealet
# Utvikler 2 har ansvaret for å lage denne funksjonen


# Funksjon for å beregne arealet av en sirkel skrives her. Funsjonen skal ta imot et parameter (r)
# Funksjonen skal returnere arealet
# Utvikler 2 har ansvaret for å lage denne funksjonen

   

# Programmet starter her
ans="Start"
while ans != "8":
    clear()
    skriv_meny()
    
    ans=input("Hva ønsker du å gjøre. Velg tall? ") 
    if ans=="1":
        clear()
        print("\nHer bergnes arealet av et kvadrat")
        print(f"Areal: {kvadrat(int(input('Oppgi side lengde: ')))}")
        venter=input("Trykk ENTER for å fortsette!")    
    elif ans=="2":
        clear()
        print("\nHer bergnes arealet av et rektangel")
        print(f"Areal: {rektangel(int(input('Oppgi g: ')), int(input('Oppgi h: ')))}")
        venter=input("Trykk ENTER for å fortsette!") 
    elif ans=="3":
        clear()
        print("\nHer bergnes arealet av en trekant")
        print(f"Areal: {rektangel(int(input('Oppgi g: ')), int(input('Oppgi h: ')))}") 
        venter=input("Trykk ENTER for å fortsette!") 
    elif ans=="4":
        clear()
        print("\nHer bergnes arealet av et parallellogram")
        print(f"Areal: {rektangel(int(input('Oppgi g: ')), int(input('Oppgi h: ')))}")
        venter=input("Trykk ENTER for å fortsette!") 
    elif ans=="5":
        clear()
        print("\nHer bergnes arealet av en rombe")
        venter=input("Trykk ENTER for å fortsette!") 
    elif ans=="6":
        clear()
        print("\nHer bergnes arealet av en trapes")
        venter=input("Trykk ENTER for å fortsette!")         
    elif ans=="7":
        clear()
        print("\nHer bergnes arealet av en sirkel")
        venter=input("Trykk ENTER for å fortsette!") 
    
print("\nTakk for at du brukte areal-programmet! Velkommen igjen!\n")          
    
        