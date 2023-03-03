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
        pos = tuple()
        frees = tuple()
        for key,value in self.__map.items():
            positions.append(key)
            if value in ('g','W',' ','A'):
                pos += (('at',value,key[0],key[1]),)
                frees += (('at','free',key[0],key[1]),)
        #
        # print(self.__map)

        smallers = tuple()

        xs = tuple()
        ys = tuple()
        for coordinate in range(max(self.__maxX + 1,self.__maxY)):
            if coordinate <= self.__maxX:
                xs += (coordinate,)
            if coordinate <= self.__maxY:
                ys += (coordinate,)
            if coordinate > 0:
                smallers += (('smaller',coordinate-1,coordinate),)

        # xs =  tuple([i for i in range(self.__maxX + 1)])
        # ys = tuple([i for i in range(self.__maxY+1)])

        init = (
                   ('=', ('bows',), 0),
                   ('at', 'hunter', self.__startX, self.__startY),
                   ('=', ('gold',), 0),
               ) + pos + frees + smallers
        print('init = ',init)
        # tuto sa vytvara domena - tj. zmeny v pohybe
        # frees = list(frees)
        # frees.remove(('at','free',self.__startX+1,self.__startY))
        # frees.append(pyddl.neg(('at','free',self.__startX+1,self.__startY)))
        # frees = tuple(frees)

        #tests,which should pass
        goal1 = (('at','hunter',self.__startX+1,self.__startY),)
        # goal1 = (('at', 'hunter', self.__startX + 1, self.__startY+1),)
        #tests, which shouldnt pass
        #goal1 = (('at', 'hunter', self.__startX - 1, self.__startY),)
        #goal1 = (('at', 'hunter', self.__startX , self.__startY-1),)



        # goal = (
        #         ('=',('bows',), 0),
        #         ('at','hunter',self.__startX+1,self.__startY),
        #         ('=',('gold',), 0),
        #     ) + obstacles + frees + golds + not_walls
        print()
        print()
        print('goal', goal)
        domain = pyddl.Domain()

        problem = pyddl.Problem(
            domain,
            {
                # 'start': tuple(''),
                # 'monster': tuple('W'),
                # 'obstacle': tuple('#'),
                # 'spaces': (' ','W','#'),

                # 'free_spots': (' ','W','g','A'),
                'positionX': xs,
                'positionY': ys,
            },
            init,
            goal1
            ,
        )
        print('xs', xs)
        print('ys', ys)
        print(smallers)
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
