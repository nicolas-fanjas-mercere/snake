import pygame
import random

pygame.init()

largeur = 400
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))

blanc = (0, 0, 0)
noir = (255, 255, 255)
rouge = (255, 0, 0)
vert = (0, 255, 0)

police = pygame.font.Font(None, 36)

taille_case = 10
nb_cases_largeur = largeur // taille_case
nb_cases_hauteur = hauteur // taille_case

tete = [nb_cases_largeur // 2, nb_cases_hauteur // 2]
corps = [tete[:]] * 3

direction = "gauche"

pomme = [random.randint(0, nb_cases_largeur - 1), random.randint(0, nb_cases_hauteur - 1)]

score = 0

def afficher_score():
    texte = police.render("Score : {}".format(score), True, noir)
    fenetre.blit(texte, (10, 10))

def afficher_serpent():
    for partie in corps:
        x, y = partie
        pygame.draw.rect(fenetre, vert, (x * taille_case, y * taille_case, taille_case, taille_case))

def afficher_pomme():
    x, y = pomme
    pygame.draw.rect(fenetre, rouge, (x * taille_case, y * taille_case, taille_case, taille_case))

def deplacer_serpent():
    global tete, corps, direction, pomme, score
    if direction == "gauche":
        tete[0] -= 1
    elif direction == "droite":
        tete[0] += 1
    elif direction == "haut":
        tete[1] -= 1
    elif direction == "bas":
        tete[1] += 1
    corps.insert(0, tete[:])
    if tete == pomme:
        pomme = [random.randint(0, nb_cases_largeur - 1), random.randint(0, nb_cases_hauteur - 1)]
        score += 1
    else: corps.pop()
def verifier_collision_bords():
    if tete[0] < 0 or tete[0] >= nb_cases_largeur or tete[1] < 0 or tete[1] >= nb_cases_hauteur:
        return True
    return False

def verifier_collision_corps():
    if tete in corps[1:]:
        return True
    return False

def reinitialiser_jeu():
    global tete, corps, direction, pomme, score
    tete = [nb_cases_largeur // 2, nb_cases_hauteur // 2]
    corps = [tete[:]] * 3
    direction = "gauche"
    pomme = [random.randint(0, nb_cases_largeur - 1), random.randint(0, nb_cases_hauteur - 1)]
    score = 0

def jouer():
    global direction
    while True:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_LEFT:
                    direction = "gauche"
                elif evenement.key == pygame.K_RIGHT:
                    direction = "droite"
                elif evenement.key == pygame.K_UP:
                    direction = "haut"
                elif evenement.key == pygame.K_DOWN:
                    direction = "bas"
                elif evenement.key == pygame.K_SPACE:
                    reinitialiser_jeu()

        fenetre.fill(blanc)

        deplacer_serpent()

        if verifier_collision_bords() or verifier_collision_corps():
            reinitialiser_jeu()

        afficher_serpent()
        afficher_pomme()
        afficher_score()

        pygame.display.flip()

        pygame.time.wait(100)


jouer()


pygame.quit()