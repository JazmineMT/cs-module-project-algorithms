'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, memory=None):
    # Your code here

    # a case for zero cookies 
   
    # a case for a negative number
    if n == 0:
        return 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    elif n == 3:
        return 4
    
    elif memory and memory[n] > 0:
        return memory[n]
    else:
        if not memory:
            memory = {i: 0 for i in range(n+1)}
        memory[n] = eating_cookies(n-1, memory) + eating_cookies(n-2, memory) + eating_cookies(n-3, memory)
    return memory[n]
        
    
        



if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
