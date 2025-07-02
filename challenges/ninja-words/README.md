# Ninja Words

A ninja word is a word which hides in a sentence: it will appear continuously, but must be broken up by one or more spaces. For example, the word "star" is a ninja word in the phrase "be**st ar**tist, but is NOT a ninja word in the phrase "twinkle twinkle little **star**. (Ninja words must be hidden, and thus always contain spaces).

Ninja words and the sentences they appear in will always be case-insensitive.

In addition, sentences may contain ninja stars (denoted with an asterisk "*"). Ninja stars can be any character, including a space. Given a list of possible ninja words, and a target sentnece, return the score of the ninja words that appear in the sentence, according to the rules below.

## Inputs

`targetWords`: A list of possible ninja words

- e.g., ["Sun", "Moon", "Star", "Planet"]

`sentence`: A target sentence which may contain ninja words

- Sentences will contain ASCII characters Aa-Zz, spaces, and asterisks
- e.g., "All the stars under the sky twinkle in slo mo on a clear night"

## Output

Determine the score of the uncovered ninja words according to the following rules:

- 1 point for every ninja word found
- 1 additional point for each ninja star contained in the word
  - "nin ja" -> 1 point
  - "**n ja" -> 3 points
- Each ninja word should only be counted once per sentence. If a ninja word appears multiple times, only count the instance which gives the most points

## Example 

- `targetWords`: ["Sun", "Moon", "Star", "Planet"]
- `sentence`: "All the stars under the sky twinkle in slo mo on a clear night"
- Analysis: The target sentence contains 2 ninja words:
  - "Sun", in "stars under"
  - "Moon", in "slo mo on"
- The word "star" is in the sentence, but it is NOT a ninja word, because it is not split up by a space. 
- Each ninja word is worth 1 point for a total of 2.
- Return 2
