"""Challenge: Data Type Transformer
Write a Python function that takes a mixed list of different data types 
(integers, floats, strings, booleans) and returns a dictionary 
summarizing the count of each type and a transformed version of the list where:
Integers are squared
Floats are rounded to 2 decimal places
Strings are reversed
Booleans are flipped (True → False, False → True)"""

def transformdata(data): #defines the function
    summary = { #sets up a dictionary so the data types can be counted
        "int": 0,      #will be added to later
        "flo": 0,
        "str": 0,
        "bool": 0
    }
    transformed = []    #initializes an empty list so its added onto later

    for thingy in data: #loops through every thingy inside data 
        if isinstance(thingy, int) and not isinstance(thingy,bool): #ensures that
            #the booleans are not treated as integers and the integers are not treated as booleans
            summary["int"] += 1 #if the thingy is an integer then add onto the count in the dictionary
            transformed.append(thingy**2)  #and square it and add into the empty list

        elif isinstance(thingy,float): #if the thingy is a float (number with decimals)
            summary["flo"] += 1  #then yhu gyatta add onto the count in the dictionary
            transformed.append(round(thingy, 2)) #and also round it 2 decimal places and put into list

        elif isinstance(thingy, str): #if the thing is a string
            summary["str"] += 1  #yhu gyatta add onto the count in the dictionary
            transformed.append(thingy[::-1]) #and reverse the word order

        elif isinstance(thingy, bool): #if the thingy is a boolean (true or false)
            summary["bool"] += 1 #then yhu gyatta add onto the count in the dictionary
            transformed.append(not thingy) #and negate the original word 
                                    #(true to false) and (false to true)
        
        else: #if anything else
            raise TypeError(f"Unsupported data type: {type(thingy)}")
             #its wrong and print the following sentence 

    return {"summary": summary, "transformed": transformed}
        #returns the summary and transformed outcomes
        #now the user can view the results

def convert_value(value):
    value = value.strip()  # Remove any leading/trailing spaces
    
    # Convert to integer if possible
    if value.isdigit():
        return int(value)
    
    # Convert to float if possible
    try:
        return float(value)
    except ValueError:
        pass
    
    # Convert "True" or "False" to boolean
    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    
    # Otherwise, keep it as a string
    return value



user_input = input("Enter values separated by commas: ")
data = [convert_value(item) for item in user_input.split(",")]

# Transform the data
result = transformdata(data)

# Print result
print(result)
        