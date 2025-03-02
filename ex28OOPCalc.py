#Design a class SeriesCalculator that calculates the sum of an arithmetic series.

class SeriesCalculator:
    def calculate(self, n, a=1, d=2):
        # Sum of the first n terms of an arithmetic series
        return n * (2 * a + (n - 1) * d) // 2

cls = SeriesCalculator()
print(cls.calculate(5))