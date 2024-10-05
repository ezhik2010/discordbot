import random, requests

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
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']    
