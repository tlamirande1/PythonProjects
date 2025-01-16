# Wind Chill Calculator 

# This program is designed to calculate the wind chill based off the temperature and wind speed.
# The wind chill is displayed through a real feel temperature value in both Fahrenheit (F) and Celsius (C). 
# Along with finding the wind chill, the program assess frostbite risk if applicable (cold enough wind chill). 


def celsiusToFahrenheit(C):         
    return C * 1.8 + 32

def fahrenheitToCelsius(F):         
    return (F - 32) / 1.8

def mphToKmph(M):                    
    return M * 1.609

def kmphToMph(K):                    
    return K / 1.609

def calculateWindChill(T, S):       
    if S <= 3 or T >= 50:            # If the wind speed is <= 3 mph or temperature is >= 50 degrees F, real feel (wind chill) equals the air temperature. 
        return T                     
    else:                            # If the previous block of code isn't true, then the function calculates the wind chill based off the formula below. 
        windChill = (35.74 + 0.6215 * T - 35.75 * (S ** 0.16) + 0.4275 * T * (S ** 0.16))   # Wind chill formula 
        return windChill


def frostbite(windChillF):           # This function analyzes frostbite risk, based on the wind chill.
    if windChillF < -60:             # Function returns time values of when frostbite will occur based on the wind chill. 
        return "Frostbite occurs in 5 minutes."
    
    elif windChillF < -35:
        return "Frostbite occurs in 10 minutes."
    elif windChillF < -17:
        return "Frostbite occurs in 30 minutes."
    else:
        return "Frostbite is unlikely to occur."


def displayWindChill(windChillF):      # Function displays the wind chill real feel temperature with both Fahrenheit and Celsius values, and the frostbite risk. 
    windChillC = fahrenheitToCelsius(windChillF)
    frostbiteTime = frostbite(windChillF)

    print("\n" + "-"*40)              
    print(f"         Wind Chill Results")
    print("-"*40)
    print(f"  Wind Chill (Fahrenheit): {windChillF:.2f} F")
    print(f"  Wind Chill (Celsius):    {windChillC:.2f} C")
    print(f"\n {frostbiteTime}")
    print("-"*40 + "\n")




def windChillCalculator():   # This is the main function which gets the temperature value, the wind speed input, the wind chill calculation, and the display.  
    temperature, tempUnit = findTemp()      
    if tempUnit == 'C':
        temperature = celsiusToFahrenheit(temperature)


    windSpeed, windUnit = findWindSpeed()   
    if windUnit == 'kmph':
        windSpeed = kmphToMph(windSpeed)

    windChill = calculateWindChill(temperature, windSpeed)  
    displayWindChill(windChill)

def findTemp():             # This function is put in place to validate the temperature input and unit, exiting (terminating) the program if an input isn't valid. 
    while True:             
        temperature = input("Enter temperature value: ")
        try:               
            temperature = float(temperature)
            break           
        except ValueError: 
            print("Invalid Temperature Value")
            exit()

    while True:        
        tempUnit = input("Enter temperature unit (C/F): ").upper()  
        if tempUnit in ['C', 'F']:
            break
        else:           
            print("Invalid Tempetaure Unit")
            exit()
    return temperature, tempUnit        

def findWindSpeed():      # This function validates the wind speed, along with the wind unit in either mph or kmph. 
    while True:           
        windSpeed = input("Enter wind speed value: ")
        try:
            windSpeed = float(windSpeed)
            if windSpeed >= 0:      
                break
            else:       
                print("Wind speed can't be negative.")
                exit()      
        except ValueError:  
            print("Invalid wind speed value.")
            exit()  

    while True:    
        windUnit = input("Enter wind speed unit (mph/kmph): ").lower()  
        if windUnit in ['mph', 'kmph']:
            break
        else:              
            print("Invalid wind speed unit.")
            exit()         
    
    return windSpeed, windUnit   

windChillCalculator()            # See previous comments for function description





        




