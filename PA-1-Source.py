import random
import time

def main():
    #Random integer pairs are in a 2D pairsay ([numOne, numTwo])
    pairs = generatePairs(-10000, 10000)
    
    #gcdsBruteForce, timesBruteForce = calculateBruteForce(pairs)
    #generateResults(gcdsBruteForce, timesBruteForce)
    #generateStatistics(timesBruteForce)
    
    gcdsEuclid, timesEuclid = calculateEuclid(pairs)
    #generateResults(gcdsEuclid, timesEuclid)
    #generateStatistics(timesEuclid)
    
    #gcdsImproved, timesImproved = calculateImproved(pairs)
    #generateResults(gcdsImproved, timesImproved)
    #generateStatistics(timesImproved)

    #generateConclusion(timesBruteForce, timesEuclid, timesImproved)
    
#Generate 100 pairs of random integers
def generatePairs(rangeMin, rangeMax):
    numOne = random.sample(range(rangeMin, rangeMax), 100)
    numTwo = random.sample(range(rangeMin, rangeMax), 100)
    return [numOne, numTwo]

#Calculate the GCD of all pairs using the Brute Force Algorithm
#def calculateBruteForce(pairs):

#Calculate the GCD of all pairs using Euclid's Algorithm
def calculateEuclid(pairs):
    gcds = []
    times = []
    
    for x in range(100):
        a = abs(pairs[0][x])
        b = abs(pairs[1][x])
        startTime = time.time()
        
        if a == 0:
            gcds.append(b)
            print("The GCD of ", pairs[0][x], " and ", pairs[1][x],  "is ",  b)
        elif b == 0:
            gcds.append(a)
            print("The GCD of ", pairs[0][x], " and ", pairs[1][x],  "is ",  a)
        elif a == 1:
            gcds.append(a)
            print("The GCD of ", pairs[0][x], " and ", pairs[1][x],  "is ",  a)
        elif b == 1:
            gcds.append(b)
            print("The GCD of ", pairs[0][x], " and ", pairs[1][x],  "is ",  b)
        else:
            y = max(a, b)
            z = min(a, b)
            remainder = None
            
            while remainder != 0:
                remainder = y % z
                y = z
                z = remainder
                
            gcds.append(y)
            print("The GCD of ", pairs[0][x], " and ", pairs[1][x],  "is ",  y)

        elapsedTime = (time.time() - startTime) * 1000
        times.append(elapsedTime)

    return gcds, times

#Calculate the GCD of all pairs using Euclid's Algorithm (Improved)
#def calculateImproved(pairs):
    
#Generate an Excel spreadsheet for each algorithm with the following columns for each pair:
#Number One, Number Two, Their GCD, Time Spent
#def generateResults(gcds, times):

#Generate an Excel spreadsheet for each algorithm with the following information:
#Maximum Time, Minimum Time, Average Time, Median Time
#def generateStatistics(times):

#Determine how the algorithms performed against each other and save results to Conclusions.txt
def generateConclusion(timesBruteForce, timesEuclid, timesImproved):
    output = ""
    
    #Compare Euclid's Algorithm with the Brute Force Algorithm
    count = 0
    savedTime = 0
    
    for x in range(100):
        if timesEuclid[x] < timesBruteForce[x]:
            savedTime += (timesBruteForce[x] - timesEuclid[x])
            count += 1

    avgSavedTime = savedTime/count
    output += "Out of 100 pairs of integers, the original version of Euclid "
    output += "outperformed brute-force in %s pairs; and the average " % count
    output += "saved time for these %s pairs of integers was %s " % (count,avgSavedTime)
    output += "milliseconds.\n"
        
    
    #Compare Euclid's Algorithm (Improved) with the Brute Force Algorithm
    count = 0
    savedTime = 0

    for x in range(100):
        if timesImproved[x] < timesBruteForce[x]:
            savedTime += (timesBruteForce[x] - timesImproved[x])
            count += 1

    avgSavedTime = savedTime/count
    output += "Out of 100 pairs of integers, the second version of Euclid "
    output += "outperformed brute-force in %s pairs; and the average " % count
    output += "saved time for these %s pairs of integers was %s " % (count,avgSavedTime)
    output += "milliseconds.\n"

    #Compare Euclid's Algorithm (Improved) with Euclid's Algorithm
    count = 0
    savedTime = 0

    for x in range(100):
        if timesImproved[x] < timesEuclid[x]:
            savedTime += (timesEuclid[x] - timesImproved[x])
            count += 1

    avgSavedTime = savedTime/count
    output += "Out of 100 pairs of integers, the second version of Euclid "
    output += "outperformed the original one in %s pairs; and the average " % count
    output += "saved time for these %s pairs of integers was %s " % (count,avgSavedTime)
    output += "milliseconds."

    #Write results to file
    file = open("Conclusions.txt", "w")
    file.write(output)
    file.close()
    print("Conclusions.txt successfully created.")
    
if __name__ == "__main__":
    main()