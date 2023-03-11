import random
import  math
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
    priemer = sum(ps)/len(ps)
    return (1-priemer)*obsah_stvorca

print(simulation())

def ttt():
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
            x = random.uniform(0,4)
            y = random.uniform(0,2*r)
            if dist([r,r],r,[x,y]):
                inside += 1
            all += 1
        ps.append(inside/all)
        all,inside = 0,0
    print('ps = ',ps)