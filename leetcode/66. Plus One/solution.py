class Solution:
    def plusOne_1(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        carry = 1
        while carry:
            if digits[i] == 9:
                digits[i] = 0

                if i - 1 < 0:
                    digits = [1] + digits
                    carry = 0
            else:
                digits[i] += 1
                carry = 0

            i -= 1

        return digits        


    def plusOne_2(self, digits: list[int]) -> list[int]:
        digits = digits[::-1]
        i = 0
        carry = 1
        while carry:
            if digits[i] == 9:
                digits[i] = 0

                if i+1 == len(digits):
                    digits.append(1)
                    carry = 0
            else:
                digits[i] += 1
                carry = 0

            i += 1


        return digits[::-1]
        
