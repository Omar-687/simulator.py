# This is a sample Python script.
import math
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f'Point has coordinates (x,y,z) = ({self.x},{self.y},{self.z})'


# class Cuboid:
#     # todo? : nadniest teleso
#     def __init__(self,width,height,start = Point(0,40,0)):
#         self.p1 = start
#         self.p2 = Point(start.x,start.y - height,start.z)
#         self.p3 = Point(start.x + width,start.y,start.z)
#         self.p4 = Point(start.x + width,start.y - height,start.z)
#
#         self.p5 = Point(self.p1.x,self.p1.y,self.p1.z + height)
#         self.p6 = Point(self.p2.x,self.p2.y,self.p2.z + height)
#         self.p7 = Point(self.p3.x,self.p3.y,self.p3.z + height)
#         self.p8 = Point(self.p4.x, self.p4.y, self.p4.z + height)
#
#         self.height = height
#         self.depth = height
#         self.width = width
#     def overall_size(self):
#         return self.height * self.depth * self.width
#     def __str__(self):
#         return f'Cuboid starts at {self.p1} and has (width,height,depth) = ({self.width},{self.height},{self.depth})'
#     def is_inside(self):
#         ...


def create_obal(width,height):
    ...

def is_inside(x1,x2,y1,y2,r,z1=0,z2=0):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2) <= r



def cubic_to_milimeter(cubic_meter):
    return cubic_meter * 1000000


def volume_of_obal():
    return 150*80*80
def calc():
    return 7.2885 * 10**5
    # return math.pi * (40)**2 a z toho integral od 0 do 145
def simulate_ex():
    f = 10
    total_width = 5 + 35 + 10 + 20 + 20 + 10 + 10 + 35
    total_height = 80
    N = 10
    samples = 10000
    ps = []
    priemer = 0
    for i in range(N):
        inside_object = 0
        inside_all = 0
        for j in range(samples):


            x = random.uniform(0,total_width)
            y = random.uniform(-total_height/2,total_height/2)

            if is_inside(x,x,0,y,total_height/2):
                inside_all += 1

            if x >= 0 and x <= 5:
                r = 15 + x
                if is_inside(x,x,0,y,r):
                    inside_object += 1

            if x >= 5 and x <= 40:
                # od sin(90) a cos(90) do sin(-90)

                r = 20
                if is_inside(x,x,0,y,r):
                    inside_object += 1
            if x >= 40 and x <= 50:
                r = 30
                if is_inside(x,x,0,y,r):
                    inside_object += 1
            if x >= 50 and x <= 70:
                r = 20
                if is_inside(x,x,0,y,r):
                    inside_object += 1
            if x >= 70 and x <= 90:
                r = 10 * (0.5 - 0.005*(x-70)**2) + 20
                if is_inside(x,x,y,0,r):
                    inside_object += 1

            if x >= 90 and x <= 100:
                r = 20
                if is_inside(x,x,0,y,r):
                    inside_object += 1
            if x >= 100 and x <= 110:
                r = 40
                if is_inside(x,x,0,y,r):
                    inside_object += 1
            if x >= 110 and x <= 140:
                r = 25
                if is_inside(x,x,0,y,r):
                    inside_object += 1
            if x >= 140 and x <= 145:
                r = 25 - (x - 140)
                if is_inside(x,x,0,y,r):
                    inside_object += 1
        ps.append((inside_object/inside_all))


    for p in ps:
        priemer += p
    priemer /= len(ps)
    print('ps = ', ps)
    print('priemer ps = ', priemer)

    return priemer * calc()

def dist(stred,r,point):
    return math.sqrt((stred[0] - point[0])**2 + (stred[1] - point[1])**2) <= r

def simulation():
    r = 1
    obsah_stvorca = (2*r)**2
    obsah_kruhu = (math.pi*r**2)
    res = obsah_kruhu/obsah_stvorca
    print('res = ',res)
    N = 10
    samples = 10000
    inside = 0
    all = 0
    ps = []
    for i in range(N):
        for j in range(samples):
            x = random.uniform(0,2*r)
            y = random.uniform(0,2*r)
            if dist([r,r],r,[x,y]):
                inside += 1
            all += 1
        ps.append(inside/all)
        all,inside = 0,0
    print('ps = ',ps)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    simulate_ex()
    # simulation()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
