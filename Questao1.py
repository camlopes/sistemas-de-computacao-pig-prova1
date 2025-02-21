
import sys

class Particao:
    def __init__(self, *p):
        self._numeros = []
        self._sum = p
        self.todo = p
        for i in range(len(p)):
            self._numeros.append(p[i] / self._soma)

    @property
    def todo(self):
        return self._soma

    @todo.setter
    def todo(self, t):
        if type(t) == int or type(t) == float or type(t) == complex:
            self._todo = t
            for item in range(len(self._numeros)):
                self._numeros[item] = self._numeros[item] * self._todo
        else:
            self._soma = 0
            self._todo = 1
            for i in range(len(self._sum)):
                self._soma += self._sum[i]

    def __len__(self):
        return len(self._numeros)

    def __eq__(self, other):
        if self._numeros != other._numeros and self._todo != other._todo:
            return str(False) + "\n" + str(False)
        elif self._numeros != other._numeros and self._todo == other._todo:
            return str(False) + "\n" + str(True)
        elif self._numeros == other._numeros and self._todo != other._todo:
            return str(True) + "\n" + str(False)
        else:
            return str(True) + "\n" + str(True)

    def __getitem__(self, key):
        return self._numeros[key]

    def __setitem__(self, key, value):
        _aux = []
        for item in range(len(self._numeros)):
            _aux.append(self._numeros[item]/self._soma)
        _aux[key] = value
        self._numeros[1] = (value / (_aux[1] + _aux[0])) * self._todo
        self._numeros[0] = (self._todo / (_aux[1] + _aux[0])) * _aux[0]

    def __repr__(self):
        return " ".join(map(str, self._numeros)) + ":" + \
               " len = " + str(len(self._numeros)) + "," + " todo = %.6f" % self._todo

    def __str__(self):
        return " ".join(map(str, self._numeros))

def main():
    p = Particao(*[2,5,3])
    print("[%s]" % str(p).replace(" ", ", "))
    p.todo = 100
    print("%r" % p)
    p = Particao(5,6)
    print("%r" % p)
    p.todo = 11
    print(repr(p))
    q = Particao(5,6)
    print(q)
    print(p == q)
    print("({}, {})".format(p[0], p[1]))
    p[1] = 7
    print(f"({p[0]}, {p[1]})")

if __name__ == '__main__':
    sys.exit(main())


""" Resultado da execucao de main():
[ 0 . 2 , 0 . 5 , 0 . 3 ]
20.0 50.0 3 0 . 0 : l e n = 3 , todo = 100.000000
0.45454545454545453 0.5454545454545454: l e n = 2 , todo = 1.000000
5. 0 6 . 0 : l e n = 2 , todo = 11.000000
0.45454545454545453 0.5454545454545454
Fal s e
Fal s e
( 5 . 0 , 6 . 0 )
(0.6707317073170731 , 10.329268292682928 )
"""