# Tutoriál: Vývoj hry Snake v Pythonu (krok za krokem)

Vítej u praktického průvodce Pythonem! Hra **Snake (Had)** je jeden z nejlepších projektů pro začátečníky, protože si na ní postupně a přirozeně osaháš všechny základní stavební kameny programování:

| Fáze | Co ve hře vytvoříme | Co se naučíš z Pythonu |
| :--- | :--- | :--- |
| **Fáze 0** | Příprava prostředí | Spouštění skriptů, balíčky (`pip`, `venv`), `import` |
| **Fáze 1** | Herní okno a hlavní smyčka | Proměnné, datové typy (`int`, `bool`, `tuple`), cyklus `while` |
| **Fáze 2** | Hlava hada a ovládání | Podmínky (`if` / `elif`), souřadnicový systém, události klávesnice |
| **Fáze 3** | Jídlo pro hada | Modul `random`, porovnávání hodnot (`==`), počítání skóre (`+=`) |
| **Fáze 4** | Tělo hada a růst | Seznamy (`list`), přidávání a odebírání prvků (`insert`, `pop`), cyklus `for` |
| **Fáze 5** | Kolize a Game Over | Logické operátory (`or`, `and`, `in`), vykreslování textu, f-stringy |
| **Fáze 6** | Čistý kód a restart hry | Vlastní funkce (`def`), organizace kódu |

---

## Jak doporučuji postupovat

1. **Přečti si vždy jen jednu fázi** – podívej se, jaký koncept z Pythonu řeší.
2. **Napiš (nebo uprav) kód v souboru `snake.py`** – doporučuji kód opisovat ručně místo kopírování, lépe si ho zapamatuješ.
3. **Spusť hru a otestuj ji** – na konci každé fáze je hra spustitelná a uvidíš okamžitý výsledek.
4. **Splň malý „Mini-úkol“** na konci fáze – ověříš si, že kódu opravdu rozumíš.

---

## Fáze 0: Příprava prostředí a knihovna Pygame

Pro grafiku a ovládání použijeme populární knihovnu **`pygame`**. Samotný kód hry v Pythonu je 100% stejný na Windows i Linuxu, liší se jen příkazy v terminálu při přípravě prostředí.

---

### Varianta A: Windows 11

#### 1. Kontrola (nebo instalace) Pythonu
Otevři **Terminál (PowerShell)** nebo terminál přímo v editoru (zkratka `` Ctrl+` ``) a zkus napsat:
```powershell
python --version
```
* Pokud ještě Python nemáš nainstalovaný, stáhni ho z [python.org/downloads](https://www.python.org/downloads/) (**Důležité:** v prvním okně instalátoru dole určitě zaškrtni **„Add python.exe to PATH“**!) nebo ho nainstaluj jedním příkazem přes vestavěný správce balíčků ve Windows 11:
  ```powershell
  winget install Python.Python.3.12
  ```
  *(Po instalaci terminál zavři a znovu otevři.)*

#### 2. Vytvoření prostředí a instalace `pygame` (ve složce projektu)
Pokud používáš **PowerShell** (výchozí terminál ve Windows 11):
```powershell
# 1. Vytvoření virtuálního prostředí (izolované místo pro knihovny)
python -m venv .venv

# 2. Aktivace virtuálního prostředí v PowerShellu
.venv\Scripts\Activate.ps1

# 3. Instalace knihovny pygame
pip install pygame
```

> **Tip pro Windows 11 (chyba se skripty v PowerShellu):**
> Pokud ti PowerShell při příkazu `.venv\Scripts\Activate.ps1` vypíše červenou chybu, že *„spouštění skriptů je v tomto systému zakázáno“* (`PSSecurityException`), povol lokální skripty pro svého uživatele tímto příkazem a pak aktivaci zopakuj:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> *(Pokud místo PowerShellu používáš klasický **Příkazový řádek – CMD**, aktivuješ prostředí příkazem `.venv\Scripts\activate.bat`.)*

#### 3. Spuštění hry na Windows 11
```powershell
python snake.py
```
*(Případně `py snake.py`)*

---

### Varianta B: Linux / macOS

```bash
# 1. Vytvoření virtuálního prostředí (izolované místo pro knihovny)
python3 -m venv .venv

# 2. Aktivace virtuálního prostředí
source .venv/bin/activate

# 3. Instalace knihovny pygame
pip install pygame
```

Spuštění hry na Linuxu / macOS:
```bash
python3 snake.py
```

---

## Fáze 1: Herní okno a hlavní smyčka (Game Loop)

### Cíl fáze
Otevřít černé okno hry, které zůstane otevřené, dokud ho nezavřeš křížkem.

### Co se naučíš z Pythonu
* **`import`** – zpřístupní v tvém programu cizí knihovnu (`pygame`).
* **Proměnné** – pojmenované krabičky na hodnoty (např. `SIRKA = 600`). Velkými písmeny se v Pythonu označují konstanty (hodnoty, které se během hry nemění).
* **N-tice (`tuple`)** – např. `(0, 0, 0)` pro barvu v režimu RGB (červená, zelená, modrá od 0 do 255).
* **Cyklus `while`** – opakuje blok kódu stále dokola, dokud platí podmínka. Každá hra je v jádru jeden velký `while` cyklus, který běží třeba 10× za sekundu:
  1. Zkontroluje stisknuté klávesy.
  2. Posune objekty ve hře.
  3. Překreslí obrazovku.

### Kód pro `snake.py` (Fáze 1)
```python
import pygame

# Inicializace knihovny pygame
pygame.init()

# Nastavení rozměrů okna (konstanty píšeme velkými písmeny)
SIRKA = 600
VYSKA = 400

# Barvy ve formátu RGB (Červená, Zelená, Modrá: 0 až 255)
CERNA = (0, 0, 0)

# Vytvoření okna a nastavení titulku
okno = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Moje první hra: Snake")

# Hodiny pro řízení rychlosti hry
hodiny = pygame.time.Clock()

# Proměnná typu bool (True/False), která řídí, zda hra běží
hra_bezi = True

# HLAVNÍ HERNÍ SMYČKA
while hra_bezi:
    # 1. Zpracování událostí (klávesy, myš, zavření okna)
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            hra_bezi = False

    # 2. Vykreslování
    okno.fill(CERNA)             # Vybarví celé okno černou barvou
    pygame.display.update()      # Zobrazí změny na monitoru

    # 3. Omezení rychlosti na 10 snímků za sekundu (FPS)
    hodiny.tick(10)

# Ukončení pygame po vyskočení ze smyčky
pygame.quit()
```

> **Mini-úkol pro Fázi 1:** Zkus změnit barvu pozadí z černé `(0, 0, 0)` na tmavě modrou `(0, 0, 50)` a změň titulek okna.

---

## Fáze 2: Hlava hada a pohyb pomocí šipek

### Cíl fáze
Vykreslit zelený čtvereček (hlavu hada) a rozpohybovat ho po mřížce pomocí šipek na klávesnici.

### Co se naučíš z Pythonu
* **Souřadnice v okně** – bod `(0, 0)` je v **levém horním rohu**. Doprava roste `x`, dolů roste `y`.
* **Podmínky `if` / `elif`** – rozhodování v programu: *„Pokud hráč stiskl šipku doprava, nastav směr pohybu doprava, jinak pokud stiskl doleva…“*
* **Přičítání do proměnné (`+=`)** – zápis `had_x += zmena_x` je zkratka pro `had_x = had_x + zmena_x`.

### Co přidáme / upravíme v kódu (Fáze 2)
```python
import pygame

pygame.init()

SIRKA = 600
VYSKA = 400
VELIKOST_BLOKU = 20  # Velikost jednoho čtverečku mřížky v pixelech

CERNA = (0, 0, 0)
ZELENA = (0, 200, 0)

okno = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Moje první hra: Snake")
hodiny = pygame.time.Clock()

# Výchozí pozice hlavy hada (uprostřed okna)
had_x = SIRKA // 2
had_y = VYSKA // 2

# O kolik se had posune v každém kroku (na začátku stojí na místě)
zmena_x = 0
zmena_y = 0

hra_bezi = True

while hra_bezi:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            hra_bezi = False
        # Reakce na stisknutí klávesy
        elif udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_LEFT:
                zmena_x = -VELIKOST_BLOKU
                zmena_y = 0
            elif udalost.key == pygame.K_RIGHT:
                zmena_x = VELIKOST_BLOKU
                zmena_y = 0
            elif udalost.key == pygame.K_UP:
                zmena_x = 0
                zmena_y = -VELIKOST_BLOKU
            elif udalost.key == pygame.K_DOWN:
                zmena_x = 0
                zmena_y = VELIKOST_BLOKU

    # Posun hlavy hada o aktuální směr
    had_x += zmena_x
    had_y += zmena_y

    # Vykreslování
    okno.fill(CERNA)
    # Vykreslení obdélníku: (kde, barva, [x, y, šířka, výška])
    pygame.draw.rect(okno, ZELENA, [had_x, had_y, VELIKOST_BLOKU, VELIKOST_BLOKU])
    pygame.display.update()

    hodiny.tick(10)

pygame.quit()
```

> **Mini-úkol pro Fázi 2:** Co se teď stane, když jedeš doprava a zmáčkneš rovnou šipku doleva? Had se otočí o 180° do protisměru. Zkus do podmínek přidat kontrolu (např. `if udalost.key == pygame.K_LEFT and zmena_x == 0:`), aby se had nemohl otočit přímo do protisměru.

---

## Fáze 3: Jídlo, náhoda a sbírání bodů

### Cíl fáze
Vygenerovat červené jablíčko na náhodném místě mřížky. Když na něj had najede, přičte se bod a jablíčko se objeví jinde.

### Co se naučíš z Pythonu
* **Modul `random`** – funkce `random.randrange(start, stop, krok)` vybere náhodné číslo. Díky parametru `krok = VELIKOST_BLOKU` (20) zajistíme, že jídlo vždy přesně sedne do mřížky (např. na souřadnice 0, 20, 40, 60…).
* **Porovnávání (`==` a `and`)** – jedním `=` hodnotu ukládáme, dvěma `==` se ptáme, zda se dvě hodnoty rovnají.

### Co přidáme do kódu (Fáze 3)
Na začátek souboru přidáme `import random`, barvu `CERVENA = (220, 40, 40)` a před smyčku `while` vygenerujeme první pozici jídla:

```python
# Náhodná pozice jídla zarovnaná na mřížku
jidlo_x = random.randrange(0, SIRKA, VELIKOST_BLOKU)
jidlo_y = random.randrange(0, VYSKA, VELIKOST_BLOKU)
skore = 0
```

Uvnitř `while` smyčky (po posunu hada) zkontrolujeme, zda hlava hada není na stejné pozici jako jídlo:

```python
    # Kontrola, zda had snědl jídlo
    if had_x == jidlo_x and had_y == jidlo_y:
        skore += 1
        print("Mňam! Aktuální skóre:", skore)
        jidlo_x = random.randrange(0, SIRKA, VELIKOST_BLOKU)
        jidlo_y = random.randrange(0, VYSKA, VELIKOST_BLOKU)
```

A při vykreslování nakreslíme i jídlo:
```python
    pygame.draw.rect(okno, CERVENA, [jidlo_x, jidlo_y, VELIKOST_BLOKU, VELIKOST_BLOKU])
```

> **Mini-úkol pro Fázi 3:** Sleduj v terminálu výpis `print(...)` pokaždé, když sebereš jablíčko.

---

## Fáze 4: Tělo hada a jeho růst (Seznamy)

### Cíl fáze
Toto je nejzajímavější část logiky! Chceme, aby se za hlavou hada táhlo tělo, které se s každým snědeným jídlem prodlouží o jeden článek.

### Co se naučíš z Pythonu
* **Seznamy (`list`)** – uspořádaná kolekce prvků zapisovaná do hranatých závorek `[...]`.
* **Jak funguje pohyb celého hada?**
  Představ si hada jako seznam souřadnic jeho článků: `telo_hada = [[300, 200], [280, 200], [260, 200]]`.
  V každém kroku hry nemusíme posouvat každý článek zvlášť! Stačí udělat chytrý trik:
  1. Na konec seznamu **přidáme novou pozici hlavy** (`telo_hada.append([had_x, had_y])`).
  2. Pokud je seznam delší než aktuální `delka_hada`, **smažeme nejstarší článek na začátku seznamu** (`del telo_hada[0]`), což je konec ocasu.
  3. Když had sní jídlo, zvýšíme `delka_hada += 1` – ocas se v tom kroku nesmaže a had vyroste!
* **Cyklus `for`** – projde všechny články v seznamu `telo_hada` a každý vykreslí na obrazovku.

### Klíčová část kódu pro Fázi 4
Před smyčkou `while`:
```python
telo_hada = []
delka_hada = 1
```

Uvnitř smyčky `while` (po posunu `had_x` a `had_y`):
```python
    # Přidáme novou pozici hlavy do těla hada
    hlava = [had_x, had_y]
    telo_hada.append(hlava)

    # Udržujeme správnou délku hada (odstraníme konec ocasu)
    if len(telo_hada) > delka_hada:
        del telo_hada[0]

    # Pokud had snědl jídlo, prodloužíme ho
    if had_x == jidlo_x and had_y == jidlo_y:
        delka_hada += 1
        skore += 1
        jidlo_x = random.randrange(0, SIRKA, VELIKOST_BLOKU)
        jidlo_y = random.randrange(0, VYSKA, VELIKOST_BLOKU)
```

A vykreslení celého hada pomocí cyklu `for`:
```python
    for clanek in telo_hada:
        pygame.draw.rect(okno, ZELENA, [clanek[0], clanek[1], VELIKOST_BLOKU, VELIKOST_BLOKU])
```

> **Mini-úkol pro Fázi 4:** Zkus nastavit výchozí `delka_hada = 5`, ať vidíš, jak se had hned po rozjezdu rozvine do délky 5 článků.

---

## Fáze 5: Pravidla hry – Kolize a Game Over

### Cíl fáze
Hra musí skončit, když had narazí do okraje okna nebo sám do sebe. Také vykreslíme skóre přímo do herního okna.

### Co se naučíš z Pythonu
* **Logický operátor `or` (nebo)** – stačí, aby platila alespoň jedna podmínka pro náraz do zdi:
  `had_x < 0 or had_x >= SIRKA or had_y < 0 or had_y >= VYSKA`
* **Řezy seznamů (slicing) a operátor `in`** – `telo_hada[:-1]` znamená „všechny články těla kromě posledního (hlavy)“. Zápisem `if hlava in telo_hada[:-1]:` se jedním řádkem zeptáme: *„Nachází se souřadnice hlavy někde ve zbytku těla?“*
* **F-stringy (`f"Skóre: {skore}"`)** – moderní způsob, jak v Pythonu vložit hodnotu proměnné přímo do textu.

### Kontrola kolizí (Fáze 5)
```python
    # 1. Náraz do zdi
    if had_x < 0 or had_x >= SIRKA or had_y < 0 or had_y >= VYSKA:
        hra_bezi = False

    # 2. Náraz do vlastního těla (kontrolujeme všechny články kromě právě přidané hlavy)
    if hlava in telo_hada[:-1]:
        hra_bezi = False
```

### Vykreslení skóre na obrazovku
```python
pismo = pygame.font.SysFont("sans", 24)
# ... uvnitř vykreslování:
text_skore = pismo.render(f"Skóre: {skore}", True, (255, 255, 255))
okno.blit(text_skore, (10, 10))
```

---

## Fáze 6: Kompletní hra s funkcemi a možností restartu

### Cíl fáze
Zabalit logiku do přehledných funkcí (`def`), přidat obrazovku „Konec hry!“ a umožnit hráči stisknout klávesu `R` pro novou hru nebo `Q` pro ukončení.

### Kompletní cílový kód (k němuž společně dojdeme)
```python
import random
import pygame

pygame.init()

# Konstanty nastavení hry
SIRKA = 600
VYSKA = 400
VELIKOST_BLOKU = 20
RYCHLOST_HRY = 10

# Barvy (RGB)
CERNA = (20, 20, 20)
BILA = (255, 255, 255)
ZELENA = (40, 200, 40)
CERVENA = (220, 50, 50)

okno = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Snake v Pythonu")
hodiny = pygame.time.Clock()
pismo = pygame.font.SysFont("sans", 24)


def vykresli_text(text, barva, x, y):
    """Pomocná funkce pro vykreslení textu na souřadnice (x, y)."""
    obraz_textu = pismo.render(text, True, barva)
    okno.blit(obraz_textu, (x, y))


def spustit_hru():
    """Hlavní funkce jedné hry."""
    had_x = SIRKA // 2
    had_y = VYSKA // 2
    zmena_x = 0
    zmena_y = 0

    telo_hada = []
    delka_hada = 1
    skore = 0

    jidlo_x = random.randrange(0, SIRKA, VELIKOST_BLOKU)
    jidlo_y = random.randrange(0, VYSKA, VELIKOST_BLOKU)

    hra_bezi = True
    konec_hry = False

    while hra_bezi:
        # Obrazovka po prohře (čeká na R nebo Q)
        while konec_hry:
            okno.fill(CERNA)
            vykresli_text(f"Konec hry! Skóre: {skore}", CERVENA, 200, 150)
            vykresli_text("Stiskni R pro novou hru nebo Q pro konec", BILA, 110, 200)
            pygame.display.update()

            for udalost in pygame.event.get():
                if udalost.type == pygame.QUIT:
                    hra_bezi = False
                    konec_hry = False
                elif udalost.type == pygame.KEYDOWN:
                    if udalost.key == pygame.K_q:
                        hra_bezi = False
                        konec_hry = False
                    elif udalost.key == pygame.K_r:
                        spustit_hru()
                        return

        # 1. Ovládání
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                hra_bezi = False
            elif udalost.type == pygame.KEYDOWN:
                if udalost.key == pygame.K_LEFT and zmena_x == 0:
                    zmena_x = -VELIKOST_BLOKU
                    zmena_y = 0
                elif udalost.key == pygame.K_RIGHT and zmena_x == 0:
                    zmena_x = VELIKOST_BLOKU
                    zmena_y = 0
                elif udalost.key == pygame.K_UP and zmena_y == 0:
                    zmena_x = 0
                    zmena_y = -VELIKOST_BLOKU
                elif udalost.key == pygame.K_DOWN and zmena_y == 0:
                    zmena_x = 0
                    zmena_y = VELIKOST_BLOKU

        # 2. Pohyb hada
        had_x += zmena_x
        had_y += zmena_y

        # 3. Kontrola nárazu do zdi
        if had_x < 0 or had_x >= SIRKA or had_y < 0 or had_y >= VYSKA:
            konec_hry = True

        # 4. Aktualizace těla hada
        hlava = [had_x, had_y]
        telo_hada.append(hlava)
        if len(telo_hada) > delka_hada:
            del telo_hada[0]

        # Kontrola nárazu do vlastního těla
        if hlava in telo_hada[:-1]:
            konec_hry = True

        # 5. Kontrola snědení jídla
        if had_x == jidlo_x and had_y == jidlo_y:
            delka_hada += 1
            skore += 1
            jidlo_x = random.randrange(0, SIRKA, VELIKOST_BLOKU)
            jidlo_y = random.randrange(0, VYSKA, VELIKOST_BLOKU)

        # 6. Vykreslování
        okno.fill(CERNA)
        pygame.draw.rect(okno, CERVENA, [jidlo_x, jidlo_y, VELIKOST_BLOKU, VELIKOST_BLOKU])

        for clanek in telo_hada:
            pygame.draw.rect(okno, ZELENA, [clanek[0], clanek[1], VELIKOST_BLOKU, VELIKOST_BLOKU])

        vykresli_text(f"Skóre: {skore}", BILA, 10, 10)
        pygame.display.update()

        hodiny.tick(RYCHLOST_HRY)

    pygame.quit()


if __name__ == "__main__":
    spustit_hru()
```
