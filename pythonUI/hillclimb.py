import random

class HillClimb:
    def __init__(self, position, n_gold, golds):
        self.position = position
        self.n_gold = n_gold
        self.g_positions = golds
        self.n_steps = 10
        self.grid = 10
        self.directions = ['U', 'D', 'L', 'R']

    def move(self, position, direction):
        if direction == 'U':
            position[0] += 1
        elif direction == 'D':
            position[0] -= 1
        elif direction == 'L':
            position[1] -= 1
        elif direction == 'R':
            position[1] += 1
        return position
    def move_multiple(self, position, directions):
        pos = position
        for direction in directions:
            pos = self.move(pos,direction)
            pos = self.cycling(pos)
        return pos
    def cycling(self, position):
        if position[0] > self.grid:
            position[0] = 1
        elif position[0] < 1:
            position[0] = self.grid
        elif position[1] > self.grid:
            position[1] = 1
        elif position[1] < 1:
            position[1] = self.grid
        return position
    def eval_gold(self, position):
        for gold in self.g_positions:
            if position == gold:
                return 1
        return 0
    def number_of_golds_gained(self,position, route):
        golds = self.g_positions[:]
        gained_golds = 0
        for direction in route:
            position = self.move(position,direction)
            position = self.cycling(position)
            for gold in golds:
                if position == gold:
                    gained_golds += 1
                    golds.remove(position)
                    break

        return gained_golds

    def repetitions(self,position, route):
        diff_pos = []
        num = 0
        for direction in route:
            position = self.move(position, direction)
            position = self.cycling(position)
            if position not in diff_pos:
                diff_pos.append(position)
            elif position in diff_pos:
               num += 1
        return num

    def eval_fitness(self,position,gold_gained, route):
        # TODO define the fitness function
        # ak sa v policko v cestne opakuje tak ho znizime fitness
        return gold_gained - (1/(1+self.repetitions(position,route)*len(self.g_positions)))


    def neighbours(self, route):
        # TODO return all neighbours
        nb = []

        for i in range(len(route)):
            for direction in self.directions:
                if route[i] == direction:
                    continue
                kopia = route[:]
                kopia[i] = direction
                nb.append(kopia)
        return nb
    def create_random_vector(self):
        v = []
        length = len(self.directions)
        for i in range(self.n_steps):
            v.append(self.directions[random.randint(0,length-1)])
        return v

    def search(self, n_attempts):
        r_vector = self.create_random_vector()
        print(f'random vector = {r_vector}')
        best_fitness = 0
        for att in range(n_attempts):
            maximum = 0
            index = -1
            nb = self.neighbours(r_vector)
            for i in range(len(nb)):
                neighbour = nb[i]
                gold_num = self.number_of_golds_gained(self.position, r_vector)
                curr = self.eval_fitness(self.position,gold_num,neighbour)
                if curr > maximum:
                    index = i
                    maximum = curr
            if index == -1:
                break
            r_vector = nb[index]
            # TODO implement hillclimb to search for the best route


            best_gold_num = self.number_of_golds_gained(self.position, r_vector)
            best_fitness = self.eval_fitness(self.position,best_gold_num,r_vector)
            print(f'Pocet najdenych pokladov = {best_gold_num}, fitness = {best_fitness}, route = {r_vector}')
            return best_fitness, r_vector
if __name__ == "__main__":
    f = open("data.txt", "r")

    data = f.readlines()
    data = [d.strip().split() for d in data]
    data = [[int(n) for n in d] for d in data]

    posit, num_g = data[0], data[1][0]
    g_positions = data[2:]

    HC = HillClimb(posit, num_g, g_positions)
    HC.search(10)
