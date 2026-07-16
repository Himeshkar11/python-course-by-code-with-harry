#wind chill
preT = [10.00,0.00,-10.00]
preW = [15,25,35]
i =0;
while(i<3):
    wind_chill =34.75+0.6215*preT[i]-35.5*(preW[i]**0.16)+0.4275*preT[i]*(preW[i]**0.16)
    print(f"Temperature ( degree F): {preT[i]}") 
    print(f"WindSpeed (MPH): {preW[i]}") 
    print(f"Windchill temperature index  : {wind_chill}")
    i=i+1
T = float(input("Enter the temperature in farenheit "))
W = float(input("Enter the windspeed in MPH "))
wind_chill =34.75+0.6215*T-35.5*(W**0.16)+0.4275*T*(W**0.16)
print(f"Temperature ( degree F):{T}") 
print(f"WindSpeed (MPH): {W}") 
print(f"Windchill temperature index  : {wind_chill}")


