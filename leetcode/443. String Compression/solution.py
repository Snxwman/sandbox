class Solution:
    def compress(self, chars: list[str]) -> int:
        write, read = 0, 0

        while read < len(chars):
            cur_char = chars[read]
            repeats = 0

            while read < len(chars) and chars[read] == cur_char:
                repeats += 1
                read += 1

            chars[write] = cur_char

            if repeats > 1:
                for digit in str(repeats):
                    write += 1
                    chars[write] = digit

            write += 1

        chars = chars[:write]
        return len(chars)
