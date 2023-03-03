import pyddl
import sys
import simulator

class world:
    __map = {}
    __totalGold = 0
    __maxX = 0
    __maxY = 0
    __startX = 0
    __startY = 0

    def load(self, file):
        f = open(file, 'r')
        data = f.read().split('\n')
        f.close()
        self.__parse(data)

    def __parse(self, data):
        y = 0
        for line in data:
            self.__maxY = y
            x = 0
            for char in line:
                self.__maxX = max(self.__maxX, x)
                self.__map[(x,y)] = char
                if char == 'g':
                    self.__totalGold+=1
                if char == '@':
                    self.__startX = x
                    self.__startY = y
                x+=1
            y+=1

    def getProblem(self):

        goal = list()

        positions = list()
        golds = tuple()
        monsters = tuple()
        frees = tuple()
        obstacles = tuple()
        for key,value in self.__map.items():
            positions.append(key)
            if value == 'g':
                golds += (('at',value,key[0],key[1]),)
            elif value == 'W':
                monsters += (('at',value,key[0],key[1]),)
            elif value == ' ':
                frees += (('at',value,key[0],key[1]),)
            elif value == '#':
                obstacles += (('at',value,key[0],key[1]),)

        init = (
                ('=',('bows',), 0),
                ('at','hunter',self.__startX,self.__startY),
                ('=',('gold',),0),
            ) + obstacles + frees + golds
        print(self.__map)
        print(positions)
        print('init = ',init)
        # tuto sa vytvara domena - tj. zmeny v pohybe
        domain = pyddl.Domain()

        problem = pyddl.Problem(
            domain,
            {
                # 'start': tuple(''),
                # 'monster': tuple('W'),
                # 'obstacle': tuple('#'),
                'spaces': (' ','W','#'),
                'positionX': tuple([i for i in range(self.__maxX+1)]),
                'positionY': tuple([i for i in range(self.__maxY+1)])
            },
            init,

            goal= (
                # ('=',('gold',),self.__totalGold),
                 ('=', ('gold',), 0),
                #('=', ('gold',), 1),
               # ('at','hunter',(self.__startX,self.__startY))
            ),
        )
        return problem

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Map file need to be specified!")
        print("Example: python3 " + sys.argv[0] + " world1.txt")
        sys.exit(1)
    w = world()
    w.load(sys.argv[1])
    problem = w.getProblem()
    plan = pyddl.planner(problem, verbose=True)
    if plan is None:
        print('Hunter is not able to solve this world!')
    else:
        actions = [action.name for action in plan]
        print(", ".join(actions))
        f = open(sys.argv[1] + ".solution", "w")
        f.write("\n".join(actions))
        f.close()
        input()

        simulator.simulate(sys.argv[1], sys.argv[1] + ".solution")
