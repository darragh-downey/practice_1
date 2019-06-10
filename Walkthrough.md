The problem is relatively simple, can you build any of the words in this list from this jumble of letters I have here.

jumble of letters: 'nweiornvinenevndvkerrdh' 
can you make these: ['ace', 'iron', 'never', 'when', 'divine']

It is initially a 'how many times does this letter appear' problem. 

Take all of the letters in the jumble and count them. A dictionary is really useful here [store that for later]. 

jumble_count = {'n': 3, 'w': 1, 'i': 2, 'e': 4, 'o': 1, 'r': 3, 'd': 1, 'h': 1, 'k': 1, 'v': 3}

Then do the same thing for each of the candidate words but we need to map the results against each word. So for example, 'divine' results in {'d': 1, 'i': 2, 'n': 1, 'e': 1} so:

words_count['divine'] = {'d': 1, 'i': 2, 'n': 1, 'e': 1}

Do that for each word.

Now, we want to cull each word that has a letter missing from the jumble. A set would have been great here if I wasn't timing myself; 

is_subset = set(words_count['divine'].keys()).issubset(set(jumble_count.keys()))

I instead, iterated through each letter and tested whether the 'key' from the word was in the 'keys' for the jumble_count dictionary. If true, test and see if that 'key' occurs less than or equal times in the jumble. 

Finally take your list of remaining words and apply the longest common subsequence (LCS) to the list to return the longest word that can be deemed the 'LCS'.
