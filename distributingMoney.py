def distributingMoney(x,y,z,k) :
    total = x + y + z + k
    if total % 3 != 0:
        return 0
    T = total // 3
    if T >= max(x, y, z):
        return 1
    return 0
x,y,z,k= map(int,input().split());
print (int(distributingMoney(x,y,z,k)))
