import sys


class Hanoi:
    def __init__(self, count):
        if count <= 0:
            raise ValueError("Wrong number")
        self.n = count
        self.pegA = list(reversed(range(1, count + 1)))
        self.pegB = []
        self.pegC = []
        self.stepCount = 0
        self.recCount = 0

    # method solve
    def solve(self):
        self.sol(self.n, self.pegA, self.pegB, self.pegC)

    def sol(self, n, pegA, pegB, pegC):
        if n > 0:
            self.sol(n - 1, pegA, pegC, pegB)
            self.recCount += 1
            self.move(pegA, pegC)
            self.sol(n - 1, pegB, pegA, pegC)
            self.recCount += 1

    def display(self):
        sys.stdout.write("\n0:")
        for i in range(len(self.pegA)):
            sys.stdout.write(" " + str(self.pegA[i]))
        sys.stdout.write("\n1:")
        for i in range(len(self.pegB)):
            sys.stdout.write(" " + str(self.pegB[i]))
        sys.stdout.write("\n2:")
        for i in range(len(self.pegC)):
            sys.stdout.write(" " + str(self.pegC[i]))
        sys.stdout.write("\n")

    def move(self, pegA, pegB):
        if pegA[0]:
            disk = pegA.pop()
            pegB.append(disk)
            self.stepCount += 1
            if verbose == 1:
                han.display()


verbose = 0
diskCount = 0
if len(sys.argv) == 3:
    if sys.argv[1] == "-v":
        verbose = 1
        diskCount = int(sys.argv[2])
    elif sys.argv[2] == "-v":
        verbose = 1
        diskCount = int(sys.argv[1])
    else:
        print("Unknown argument")
        exit(1)
elif len(sys.argv) == 2:
    diskCount = int(sys.argv[1])
else:
    print("Unknown argument")
    exit(1)
try:
    han = Hanoi(diskCount)
except ValueError as e:
    print e.message
    exit(1)

if verbose == 1:
    han.display()
han.solve()
print("\ntotalSteps: " + str(han.stepCount))
print("recursionSteps: " + str(han.recCount))
