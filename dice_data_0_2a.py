# S.W.Hillman (2018) rev.1.0.1
# test program to output random number between 1 & 6
# for 2 dice and get total.
# write results to .csv file
from  csv import writer
from os import path
from random import randint

score = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}    # Dictionary for score per throw                                                                                                      


for i in range(0,100000):                                     
        roll=randint(1,6) + randint(1,6)                    # Roll 2 dice
        score[roll]+=1
        i+=1                                                # Increment loop counter
filename = "/users/steve/desktop/result.csv"                # Write data to .csv file
                                                            # Setup output file

if path.isfile('/users/steve/desktop/result.csv')==False:   # If file does not exist, write file with a header row
        with open(filename, "w") as output:
             writer = writer(output)                        # Write to file
             writer.writerow(['Two', 'Three','Four','Five','Six','Seven','Eight' ,'Nine','Ten','Eleven','Twelve'])                     # Header row
             writer.writerow([score[2],score[3],score[4],score[5],score[6],score[7],score[8],score[9],score[10],score[11],score[12]])  # result row
else:
        with open(filename, "a") as output:                 # If file does exist, append  data to existing file        
            writer = writer(output)                         # Write to file
            writer.writerow([score[2],score[3],score[4],score[5],score[6],score[7],score[8],score[9],score[10],score[11],score[12]])  # result row
            

print ("FINISHED")                                          # Acknowledge the run is complete
