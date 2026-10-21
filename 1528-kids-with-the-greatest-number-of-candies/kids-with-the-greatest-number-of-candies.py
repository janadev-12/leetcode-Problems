class Solution:

  def kidsWithCandies(self, candies, extraCandies):
    # Step 1: Ellarukum irukkura candies-la romba adhigam (maximum) evlo nu kandupidikkrom
    max_candies = max(candies)

    # Step 2: Ovvoru kid-oda candies-oda extraCandies-ah sertha,
    # adhu max_candies-ku samaama illadha adhigamaa irukkannu check panrom.
    result = []
    for candy in candies:
      if candy + extraCandies >= max_candies:
        result.append(True)
      else:
        result.append(False)

    return result