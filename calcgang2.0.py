print("Easy 2.0 calcgang")
# Mode
print("Select a mode")
print('''
        Mode 1 - Add
        Mode 2 - Subtract
        Mode 3 - Mutiply
        Mode 4 - Power
        Mode 5 - Divide
                       ''')
# User Input
Mode = int(input("Select a Mode!: "))
N1 = float(input("First Number here!: "))
N2 = float(input("Second Number here!: "))
# Funtions
def Add():
    return N1 + N2

def Subtract():
    return N1 - N2
    
def Mutiple():
    return N1 * N2

def power():
    return N1 ** N2

def Divide():
    return N1 / N2 
# When user picks a mode.
if Mode == 1:
    print(f"{N1} + {N2} = {Add()}")
elif Mode == 2:
    print(f"{N1} - {N2} = {Subtract()}") 
elif Mode == 3:
    print(f"{N1} + {N2} = {Mutiple()}")
elif Mode == 4:
    print(f"{N1} * {N2} = {power()}")
elif Mode == 5:
    print(f"{N1} / {N2} = {Divide()}")
else:
    print("What are you doing in my swamp")