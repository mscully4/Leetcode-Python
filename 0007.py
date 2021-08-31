class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        string = str(abs(x))
        new = ""
        for char in string[::-1]:
            new = new + char
        reverse = int(new) * sign
        print(reverse, 2*32, -2*32)
        if reverse > (2*31) - 1 or reverse < -2*31:
            return 0
        return reverse