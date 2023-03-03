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
        init = tuple()
        goal = tuple()
        positions_x = tuple()
        positions_y = tuple()
        for coord in range(max(self.__maxX + 1,self.__maxY + 1)):
            if coord - 1 >= 0:
                init += (('smaller', coord - 1,coord),)
            if coord <= self.__maxX:
                positions_x += ((coord),)
            if coord <= self.__maxY:
                positions_y += ((coord),)

        for position, value in self.__map.items():
            if value != '#':
                init += (('at',value, position[0], position[1]),)
                if value != 'W':
                    init += (('at', 'free', position[0], position[1]),)

        init += (('=', ('gold',), 0),)
        init += (('=', ('arrows',), 0),)

        goal += (('at', '@', self.__startX, self.__startY),)
        goal += (('=', ('gold',), self.__totalGold),)
        domain = pyddl.Domain(
            (pyddl.Action('move-left',
                   parameters=(
                       ('positionX', 'px'),
                       ('positionY', 'py'),
                       ('positionX', 'bx'),
                   ),
                   preconditions=(
                       ('at', '@', 'px', 'py'),
                       ('at', 'free', 'bx', 'py'),
                       ('smaller', 'bx', 'px'),
                   ),
                   effects=(
                       pyddl.neg(('at', '@', 'px', 'py')),
                       ('at', '@', 'bx', 'py'),
                   )),
            pyddl.Action('move-right',
                   parameters=(
                       ('positionX', 'px'),
                       ('positionY', 'py'),
                       ('positionX', 'bx'),
                   ),
                   preconditions=(
                       ('at', '@', 'px', 'py'),
                       ('at', 'free', 'bx', 'py'),
                       ('smaller', 'px', 'bx'),
                   ),
                   effects=(
                       pyddl.neg(('at', '@', 'px', 'py')),
                       ('at', '@', 'bx', 'py'),
                   )),

            pyddl.Action('move-up',
                   parameters=(
                       ('positionX', 'px'),
                       ('positionY', 'py'),
                       ('positionY', 'by'),
                   ),
                   preconditions=(
                       ('at', '@', 'px', 'py'),
                       ('at', 'free', 'px', 'by'),
                       ('smaller', 'by', 'py'),
                   ),
                   effects=(
                       pyddl.neg(('at', '@', 'px', 'py')),
                       ('at', '@', 'px', 'by'),
                   )),
            pyddl.Action('move-down',
                   parameters=(
                       ('positionX', 'px'),
                       ('positionY', 'py'),
                       ('positionY', 'by'),
                   ),
                   preconditions=(
                       ('at', '@', 'px', 'py'),
                       ('at', 'free', 'px', 'by'),
                       ('smaller','py', 'by'),
                   ),
                   effects=(
                       pyddl.neg(('at', '@', 'px', 'py')),
                       ('at', '@', 'px', 'by'),
                   )),
            pyddl.Action('take-gold',
                   parameters=(
                       ('positionX', 'px'),
                       ('positionY', 'py'),
                   ),
                   preconditions=(
                       ('at', '@', 'px', 'py'),
                       ('at', 'g', 'px', 'py'),
                   ),
                   effects=(
                       pyddl.neg(('at', 'g', 'px', 'py')),
                       ('+=', ('gold',), 1),
                   )),
            pyddl.Action('take-arrow',
                   parameters=(
                       ('positionX', 'px'),
                       ('positionY', 'py'),
                   ),
                   preconditions=(
                       ('at', '@', 'px', 'py'),
                       ('at', 'A', 'px', 'py'),

                   ),
                   effects=(
                       pyddl.neg(('at', 'A', 'px', 'py')),
                       ('+=', ('arrows',), 1),
                   )),

            pyddl.Action('shoot-wumpus-right',
                   parameters=(
                       ('positionX', 'px'),
                       ('positionY', 'py'),
                       ('positionX', 'bx'),
                   ),
                   preconditions=(
                       ('at', '@', 'px', 'py'),
                       ('at', 'W', 'bx', 'py'),
                       ('smaller', 'px', 'bx'),
                       ('>', ('arrows',), 0),
                   ),
                   effects=(
                       pyddl.neg(('at', 'W', 'bx', 'py')),
                       ('at','free','bx','py'),
                       ('-=', ('arrows',), 1),
                   )),
            pyddl.Action('shoot-wumpus-left',
                   parameters=(
                       ('positionX', 'px'),
                       ('positionY', 'py'),
                       ('positionX', 'bx'),
                   ),
                   preconditions=(
                       ('at', '@', 'px', 'py'),
                       ('at', 'W', 'bx', 'py'),
                       ('smaller', 'bx', 'px'),
                       ('>', ('arrows',), 0),
                   ),
                   effects=(
                       pyddl.neg(('at', 'W', 'bx', 'py')),
                       ('at', 'free', 'bx', 'py'),
                       ('-=', ('arrows',), 1),
                   )),
            pyddl.Action('shoot-wumpus-up',
                   parameters=(
                       ('positionX', 'px'),
                       ('positionY', 'py'),
                       ('positionY', 'by'),
                   ),
                   preconditions=(
                       ('at', '@', 'px', 'py'),
                       ('at', 'W', 'px', 'by'),
                       ('>', ('arrows',), 0),
                       ('smaller', 'by', 'py'),
                   ),
                   effects=(

                       pyddl.neg(('at', 'W', 'px', 'by')),
                       ('at', 'free', 'px', 'by'),
                       ('-=', ('arrows',), 1),
                   )),
            pyddl.Action('shoot-wumpus-down',
                   parameters=(
                       ('positionX', 'px'),
                       ('positionY', 'py'),
                       ('positionY', 'by'),

                   ),
                   preconditions=(
                       ('at', '@', 'px', 'py'),
                       ('at', 'W', 'px', 'by'),
                       ('smaller', 'py', 'by'),
                       ('>', ('arrows',), 0),
                   ),
                   effects=(
                       pyddl.neg(('at', 'W', 'px', 'by')),
                       ('at', 'free', 'px', 'by'),
                       ('-=', ('arrows',), 1),
                   )),)

            )
        problem = pyddl.Problem(
            domain,
            {
                'positionX': positions_x,
                'positionY': positions_y,
            },
            init,
            goal,
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
