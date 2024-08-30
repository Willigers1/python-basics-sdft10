import math
#BDD
# 1. Feature - calculate the number of ways to pair boys and girls 

#Scenario: Pairing 2 boys and 2 girls from a group of  5 boys and girls 
# given an array [5,5,4] where  5 represents the number of boys 
# and 5 represents the number of girls and 4 represents the number of people to pair
# 
# When I run the MatchinCouples function 
# 
# Then the function should return 200 because there are 10 waus to choose 2 boys from 5 , 
# 10 ways to to choose 2 girls from 5 and 2 ways to pair the selected boys and girls  

# pseudo code 
# Function MatchingCouples(arr)
#   Input: arr, an array of 3 integers [B, G, N]
#   Output: Integer representing the number of different ways to pair boys and girls

# Step 1: Extract the values from the array
# B = arr[0] no of boys 
# G = arr[1] no of girls 
# N = arr[2] no of people to pair together

# Step 2: Calculate the number of bpys and girls to pair
# Half = N / 2 

# Step 3: Calculate the number of ways to choose HalfN boys from B boys
# Boys = Cmn(B, HalfN)

# Step 4: Calculate the number of ways to choose HalfN girls from G girls 
# Girs = Cmn(G, HalfN)

# Step 5: Calculate the number of ways to arrange the selected boys and girls
# Result = Factorial(HalfN)

# Step 6: Calculate the number of ways to pair the boys and girls together
# Total ways  = Boys * Girs * Result

# Step 7: Return the result as total number of ways 
# Return Total ways


#solution
def MatchingCouples(arr):
    B, G, N = arr
    half = N // 2

    BCombination = math.comb(B, half)
    GCombination = math.comb(G, half)

    arrangements = math.factorial(half)

    total_ways = BCombination * GCombination * arrangements

    return total_ways



print(MatchingCouples([5, 5, 4])) # 200
print(MatchingCouples([2,2,2])) # 4