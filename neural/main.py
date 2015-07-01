from . import network

CARRY = (1, )
NO_CARRY = (0, )


def to_binary(n):
    return tuple(int(char) for char in bin(n)[2:])


def main():
    brain = network.NeuralNetwork(6, 6, 4)
    brain.randomize()
    brain.teach(to_binary(3) + to_binary(2), NO_CARRY + to_binary(5))
    brain.teach(to_binary(2) + to_binary(3), NO_CARRY + to_binary(5))
    brain.teach(to_binary(1) + to_binary(0), NO_CARRY + to_binary(1))
    brain.teach(to_binary(7) + to_binary(7), CARRY + to_binary(6))
    result = brain.solve(to_binary(4) + to_binary(2))
    print(result)


if __name__ == '__main__':
    main()
