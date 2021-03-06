import math
import copy

class PolyNode:
    def __init__(self, coefficient, exponent):
        self.__coef = coefficient
        self.__exp = exponent
        self.__link = None

    @property
    def coef(self):
        return self.__coef
    
    @coef.setter
    def coef(self, co):
        self.__coef = co

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, ex):
        self.__exp = ex
    
    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, ln):
        self.__link = ln

class PolyList:
    @staticmethod
    def print_poly(poly):
        cur = poly.head.link
        while cur:
            if cur.link:
                print("{}x^{} + ".format(cur.coef, cur.exp), end="")
            elif cur.exp:
                print("{}x^{}".format(cur.coef, cur.exp))
            else:
                print(cur.coef)
            cur=cur.link

    def __init__(self):
        self.head = PolyNode(math.inf, -1)

    def attach(self, coef, exp):
        new_node = PolyNode(coef, exp)
        
        bef = self.head
        cur = self.head.link
        
        while cur:
            if cur.exp < exp:
                new_node.link=bef.link
                bef.link=new_node
                return
            bef = cur
            cur = cur.link

        bef.link = new_node

    def __add__(self, other):
        temp = PolyList()
        p1_it = self.head.link
        p2_it = other.head.link

        while p1_it and p2_it:
            if p1_it.exp > p2_it.exp:
                temp.attach(p1_it.coef, p1_it.exp)
                p1_it = p1_it.link
            elif p1_it.exp < p2_it.exp:
                temp.attach(p2_it.coef, p2_it.exp)
                p2_it = p2_it.link
            else:
                coef = p1_it.coef + p2_it.coef
                temp.attach(coef, p1_it.exp)
                p1_it=p1_it.link
                p2_it=p2_it.link

        while p1_it:
            temp.attach(p1_it.coef, p1_it.exp)
            p1_it = p1_it.link

        while p2_it:
            temp.attach(p2_it.coef, p2_it.exp)
            p2_it = p2_it.link

        return temp

    def __sub__(self, other):
        p1 = self
        p2 = copy.deepcopy(other)
        p2_it = p2.head.link
        while p2_it:
            p2_it.coef = -p2_it.coef
            p2_it = p2_it.link
        return p1 + p2

    def __mul__(self, other):
        p1 = self; p2 = other
        poly_list = []
        p1_it = p1.head.link

        while p1_it:
            p2_it = p2.head.link
            temp_poly = PolyList()
            while p2_it:
                coef = p1_it.coef * p2_it.coef
                exp = p1_it.exp + p2_it.exp
                temp_poly.attach(coef, exp)
                p2_it = p2_it.link
            poly_list.append(temp_poly)
            p1_it = p1_it.link
        
        res = PolyList()
        for p in poly_list:
            res += p

        return res

if __name__ == "__main__":
    p1 = PolyList()
    p2 = PolyList()

    #p1 = 3x^3 + 1x^2      + 3
    p1.attach(3, 3)
    p1.attach(3, 0)
    p1.attach(1, 2)
    PolyList.print_poly(p1)

    #p2 = 2x^3 +       7x  + 12
    p2.attach(2, 3)
    p2.attach(7, 1)
    p2.attach(12, 0)
    PolyList.print_poly(p2)

    #res = 5x^3 + x^2 + 7x + 15
    print('polynomial addition')
    res = p1 + p2
    PolyList.print_poly(res)
    print()

    #res = x^3 + x^2 + -7x^1 - 9
    print('polynomial subtraction')
    res = p1 - p2
    PolyList.print_poly(res)
    print()

    print("polynomial multiplication")
    #p3 = 3x - 2
    p3 = PolyList()
    p3.attach(3, 1)
    p3.attach(-2, 0)
    PolyList.print_poly(p3)

    #p4 = 2x^2 -2x +3 
    p4 = PolyList()
    p4.attach(2, 2)
    p4.attach(-2, 1)
    p4.attach(3, 0)
    PolyList.print_poly(p4)

    #res = 6x^3 + -10x^2 + 13x^1 + -6
    res = p3 * p4
    PolyList.print_poly(res)