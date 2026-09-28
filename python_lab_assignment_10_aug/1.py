# write a python fuction second_largest(*args) that accept any number of integer aand return the second largest unique number suing set().

def second_largest(*args):
    
    unique_numbers = set(args)
    
   
    if len(unique_numbers) < 2:
        return None
    
  
    sorted_numbers = sorted(unique_numbers, reverse=True)
    
  
    return sorted_numbers[1]


