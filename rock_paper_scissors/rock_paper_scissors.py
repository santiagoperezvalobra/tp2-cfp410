import random

PIEDRA=1
PAPEL=2
TIJERA=3


def rock_paper_scissors(eleccion):
    pc = random.randint(1, 3)
    userGano = ((pc==PIEDRA and eleccion==PAPEL) or (pc==PAPEL and eleccion == TIJERA) or (pc==TIJERA and eleccion==PIEDRA))

    pc_op = pc
    if pc_op==PIEDRA:
        pc_op="PIEDRA"
    elif pc_op==PAPEL:
        pc_op="PAPEL"
    else:
        pc_op="TIJERA"

    if userGano:
        
        return (f"¡Ganaste!, yo elegí {pc_op}")
    elif pc==eleccion:
        return(f"¡Empatamos! yo también elegí {pc_op}")
    else:
        return(f"¡Perdiste!, yo elegí {pc_op}")
