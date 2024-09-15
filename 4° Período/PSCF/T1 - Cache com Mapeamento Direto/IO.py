import sys

class IO:
    def output(self, s):
        print(s, end='')

    def input(self, prompt):
        return input(prompt)