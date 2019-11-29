import traceback
import sys

from mpmath.calculus.optimization import Newton


class Newton:
    X = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Y = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    def __init__(self):
        self.n=len(self.X)

    def calculate(self):
        try:
            print("    X         Y ")
            for a in range(int(self.X[9])*2+2):
                t= a
                print("{:7.2f} {:7.2f}".format(t, self.__interpolation(t)))

        except Exception as e:
            raise

    def __interpolation(self, t):
        try:
            c = [0 for _ in range(self.n)]
            w = [0 for _ in range(self.n)]

            for i in range (0, self.n):
                #print(i)
                w[i]=self.Y[i]
                for j in reversed(range(i)):
                    #print(j)
                    w[j] = (w[j + 1] - w[j]) / (self.X[i] - self.X[j])
                c[i]=w[0]
            s = c[self.n-1]
            for i in reversed(range(self.n)):
                s = s * (t -self.X[i])+c[i]
            return s
        except Exception as e:
            raise

if __name__=="__main__":
        try:
            obj = Newton()
            obj.calculate()
        except Exception as e:
            traceback.print_exc()
            sys.exit(1)





