import pygame


# Inicializace knihovny pygame
pygame.init()

# Rozměry okna
SIRKA = 600
VYSKA = 400

# Barva v RGB formátu
CERNA = (255, 0, 255)

# Vytvoření okna a nastavení titulku
okno = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Moje první hra: Snake")

# Hodiny řídí rychlost hry
hodiny = pygame.time.Clock()

# Určuje, zda hra pokračuje
hra_bezi = True

while hra_bezi:
    # Zpracování událostí, například zavření okna
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            hra_bezi = False

    # Vykreslení černého pozadí
    okno.fill(CERNA)
    pygame.display.update()

    # Omezení rychlosti na 10 snímků za sekundu
    hodiny.tick(10)

pygame.quit()