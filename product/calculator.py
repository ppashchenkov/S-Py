class Calculator:

    def sum(self, a, b = 0):
        return a + b

    def sub(self, a, b = 0):
        return a - b

    def  mult(self, a, b = 1):
        return a * b

    def power(self, a, b = 2):
        return a ** b

    def div(self, a, b = 1):
        if b == 0:
            raise ArithmeticError
        else:
            return a / b

    def avr(self, nums: [int]):
        if len(nums) == 0:
            return 0
        sum = 0
        for num in nums:
            if isinstance(num, str):
                raise Exception("Only [int]")
            else:
                sum += num
        return sum / len(nums)
