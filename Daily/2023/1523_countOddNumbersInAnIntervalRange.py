class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # half = (hight - low) // 2

        # take odds: [1, 5], even: [2, 6]
        # [odd, odd]
        # (1, 5) -> [1, 3, 5] => half + 1

        # [odd, even]
        # (1, 6) -> [1, 3, 5] => half + 1

        # [even, odd]
        # (2, 5) => [3, 5]    => half + 1

        # [even, even]
        # (2, 6) => [3, 5]    => half

        half = (high - low) // 2
        return half if low % 2 == 0 and high % 2 == 0 else half + 1
