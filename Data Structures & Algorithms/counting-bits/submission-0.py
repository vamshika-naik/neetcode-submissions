class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0] * (n+1)
        for i in range(0, n+1):
            bits = [int(bit) for bit in format(i, 'b')]
            for j in bits:
                if j==1:
                    count[i] += 1
        return count