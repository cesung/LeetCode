from collections import defaultdict

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        size = len(ideas)
        ideas_set = set(ideas)
        first_letters_set = set(
            [ ideas[idx][0] for idx in range(size) ]
        )

        idea_to_new_ideas = defaultdict(list)

        for idea in ideas:
            for first_letter in first_letters_set:
                new_idea = first_letter + idea[1:]
                if new_idea not in ideas_set:
                    idea_to_new_ideas[idea].append(new_idea)
        
        cntr = defaultdict(lambda : defaultdict(int))
        for idea in idea_to_new_ideas:
            for new_idea in idea_to_new_ideas[idea]:
                cntr[idea[0]][new_idea[0]] += 1
    
        ret = 0
        for ch1_ascii in range(ord('a'), ord('z') + 1):
            for ch2_ascii in range(ch1_ascii + 1, ord('z') + 1):
                ch1, ch2 = chr(ch1_ascii), chr(ch2_ascii)
                ret += cntr[ch1][ch2] * cntr[ch2][ch1] * 2
        
        return ret
