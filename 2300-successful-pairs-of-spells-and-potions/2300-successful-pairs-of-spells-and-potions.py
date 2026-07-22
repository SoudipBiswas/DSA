from typing import List
from bisect import bisect_left


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        num_potions = len(potions)
        result = []
        for spell_strength in spells:
            min_potion_strength = success / spell_strength
            insert_position = bisect_left(potions, min_potion_strength)
            successful_count = num_potions - insert_position
            result.append(successful_count)

        return result
