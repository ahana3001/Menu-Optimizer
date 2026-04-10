import random
import math

POPULATION_SIZE = 50
GENERATIONS = 30
MENU_DAYS = 7
MUTATION_RATE = 0.2
TARGET_CALORIES = 650

DISHES = [
    ("Risotto", 18.5, 4.8, 720, 35),
    ("Salmon", 22.0, 4.9, 580, 20),
    ("Wellington", 35.0, 4.7, 890, 60),
    ("Vegan Bowl", 14.0, 4.5, 480, 15),
    ("Pizza", 12.0, 4.3, 680, 25),
    ("Tikka", 16.0, 4.7, 620, 30),
    ("Sushi", 32.0, 4.9, 510, 40),
    ("BBQ Ribs", 20.0, 4.5, 950, 55),
    ("Salad", 9.0, 4.1, 320, 10),
    ("Pasta", 19.0, 4.6, 690, 25),
]

DAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0

    @staticmethod
    def random():
        return Chromosome(random.sample(range(len(DISHES)), MENU_DAYS))

    def evaluate(self):
        profit = sum(DISHES[g][1] for g in self.genes)
        rating = sum(DISHES[g][2] for g in self.genes) / MENU_DAYS
        calories = sum(DISHES[g][3] for g in self.genes) / MENU_DAYS
        prep = sum(DISHES[g][4] for g in self.genes) / MENU_DAYS

        calorie_score = math.exp(-((calories - TARGET_CALORIES) ** 2) / 10000)

        self.fitness = (
            0.3 * profit +
            0.3 * rating * 20 +
            0.2 * calorie_score * 100 +
            0.2 * (1/(1+prep))
        )

def crossover(p1, p2):
    child = []
    used = set()

    for i in range(MENU_DAYS):
        gene = p1.genes[i] if random.random() < 0.5 else p2.genes[i]
        if gene not in used:
            child.append(gene)
            used.add(gene)

    # fill missing genes
    for g in range(len(DISHES)):
        if len(child) < MENU_DAYS and g not in used:
            child.append(g)

    return Chromosome(child)

def mutate(chrom):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(MENU_DAYS), 2)
        chrom.genes[i], chrom.genes[j] = chrom.genes[j], chrom.genes[i]
    return chrom

def run_ga():
    population = [Chromosome.random() for _ in range(POPULATION_SIZE)]
    history = []

    for gen in range(GENERATIONS):
        for c in population:
            c.evaluate()

        population.sort(key=lambda x: x.fitness, reverse=True)

        best = population[0]
        avg = sum(c.fitness for c in population)/len(population)

        history.append({
            "generation": gen,
            "best": round(best.fitness,2),
            "avg": round(avg,2)
        })

        new_pop = population[:5]

        while len(new_pop) < POPULATION_SIZE:
            p1 = random.choice(population[:15])
            p2 = random.choice(population[:15])

            child = crossover(p1, p2)
            child = mutate(child)

            new_pop.append(child)

        population = new_pop

    best = population[0]

    menu = []
    for i, g in enumerate(best.genes):
        menu.append({
            "day": DAYS[i],
            "dish": DISHES[g][0],
            "profit": DISHES[g][1],
            "rating": DISHES[g][2],
            "calories": DISHES[g][3],
            "prep": DISHES[g][4]
        })

    summary = {
        "profit": sum(DISHES[g][1] for g in best.genes),
        "rating": round(sum(DISHES[g][2] for g in best.genes)/7,2),
        "calories": round(sum(DISHES[g][3] for g in best.genes)/7,0)
    }

    return {"menu": menu, "summary": summary, "history": history}