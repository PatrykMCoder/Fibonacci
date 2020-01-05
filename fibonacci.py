import matplotlib.pyplot as plt


class Fibonacci:

    def __init__(self):
        pass

    def get_all_fibonacci(self):
        numbers = [0, 1]
        for i in range(20):
            length_list = len(numbers)
            x = numbers[length_list - 2]
            y = numbers[length_list - 1]
            z = x + y
            numbers.append(z)
        return numbers

    def get_n_fibonacii(self, n):
        numbers = [0, 1]
        for i in range(n):
            length_list = len(numbers)
            x = numbers[length_list - 2]
            y = numbers[length_list - 1]
            z = x + y
            numbers.append(z)
        return numbers

    def get_nth_fibonacci(self, n):
        numbers = [0, 1]
        for i in range(n):
            length_list = len(numbers)
            x = numbers[length_list - 2]
            y = numbers[length_list - 1]
            z = x + y
            numbers.append(z)
        return numbers[n - 1]

    def draw_chart(self, n):
        y2 = [0, 1]
        numbers = [0, 1]
        for i in range(n):
            length_list = len(numbers)
            x = numbers[length_list - 2]
            y = numbers[length_list - 1]
            z = x + y
            numbers.append(z)
            y2.append(i+2)

        x = numbers
        y = y2
        plt.plot(y, x)
        plt.show()