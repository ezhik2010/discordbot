import random

def coin():
    flip = random.randint(0,2)
    if flip == 0:
        return "Выпал орел"
    else:
        return "Выпала решка"
    
def howyou():
    variants = ['хорошо', 'нормально', 'просто супер']
    dela = random.choice(variants)
    return dela

def howprocent():
    procent = random.randint(0,100)
    return procent 
