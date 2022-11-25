# f(x) = b₀ + b₁x₁
from typing import Tuple


class Model:
    def __init__(self, train_set=((0, 1),
                                  (2, 2),
                                  (4, 3),
                                  (9, 8),
                                  (3, 5))):
        self.train_set = train_set
        self.b0, self.b1 = self._training()

    def _training(self) -> Tuple[float, float]:
        x = [i[0] for i in self.train_set]
        y = [i[1] for i in self.train_set]

        x_sum = sum(x)
        x_square_sum = sum(map(lambda i: i ** 2, x))
        y_sum = sum(y)

        multiply_sum = 0
        for i in range(len(x)):
            multiply_sum += x[i] * y[i]

        b1 = (len(x) * multiply_sum - x_sum * y_sum) / (len(x) * x_square_sum - x_sum ** 2)
        b0 = ((y_sum - b1 * x_sum) / len(x))
        return b0, b1

    def predict(self, x: int) -> float:
        return self.b0 + self.b1 * x


if __name__ == '__main__':
    dm = Model()
    example_test_set = [(0, 1),
                        (2, 2),
                        (4, 3),
                        (9, 8),
                        (3, 5)]
    predicted = [dm.predict(point[0]) for point in example_test_set]
    print(predicted)
