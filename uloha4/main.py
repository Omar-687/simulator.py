# This is a sample Python script.
import math
import random

def is_inside(x1,x2,y1,y2,r,z1=0,z2=0):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1 - z2)**2) < r

# def real_volume():
#
#
# def volume_of_obal():
#     return 150*80*80
def volume_of_hull():
    return 7.2885 * 10**5
    # we rotate 2 dimensional object with length 145 and height 40, that is our hull cover
    # calculation : integral od 0 do 145 math.pi * (40)**2
def simulate_ex():
    total_width = 5 + 35 + 10 + 20 + 20 + 10 + 10 + 35
    total_height = 80
    N = 100
    samples = 10000
    ps = []

    for i in range(N):
        out = 0
        inside_object = 0
        inside_all = 0
        for j in range(samples):
            x = random.uniform(0,145)
            y = random.uniform(-total_height/2,total_height/2)
            z = random.uniform(-total_height/2,total_height/2)
            inside_all += 1

            if x >= 0 and x <= 5:
                r = 15 + x
                if  math.sqrt(y**2 + z**2) < r:
                    inside_object += 1
                else:
                    out += 1

            # if x >= 5 and x <= 40:
            #     r = 20
            #     if  math.sqrt(y**2 + z**2) < r:
            #         inside_object += 1
            #     else:
            #         out += 1
            if x >= 40 and x <= 50:
                r = 30
                if  math.sqrt(y**2 + z**2) < r:
                    inside_object += 1
                else:
                    out += 1
            if (x >= 50 and x <= 70) or (x >= 90 and x <= 100) or (x >= 5 and x <= 40):
                r = 20
                if  math.sqrt(y**2 + z**2) < r:
                    inside_object += 1
                else:
                    out += 1
            if x >= 70 and x <= 90:
                r = 10 * (0.5 - 0.005*(x-80)**2) + 20
                if  math.sqrt(y**2 + z**2) < r:
                    inside_object += 1
                else:
                    out += 1

            # if x >= 90 and x <= 100:
            #     r = 20
            #     if  math.sqrt(y**2 + z**2) < r:
            #         inside_object += 1
            #     else:
            #         out += 1
            if x >= 100 and x <= 110:
                r = 40
                if  math.sqrt(y**2 + z**2) < r:
                    inside_object += 1
                else:
                    out += 1
            if x >= 110 and x <= 140:
                r = 25
                if  math.sqrt(y**2 + z**2) < r:
                    inside_object += 1
                else:
                    out += 1
            if x >= 140 and x <= 145:
                r = 25 - (x - 140)

                if  math.sqrt(y**2 + z**2) < r:
                    inside_object += 1
                else:
                    out += 1
        print('inside = ',inside_object)
        print('outside = ',inside_all)
        ps.append(inside_object/inside_all)


    priemer = sum(ps)/len(ps)
    print('ps = ', ps)
    print('priemer ps = ', priemer)

    return priemer * volume_of_hull()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Resulting volume of waste materials in cubic milimeters = ',simulate_ex())
    print('volume of hull * 0.42',volume_of_hull()*0.36)
    # simulation()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
