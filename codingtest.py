import sys
import os.path
calculationOptions = ["sum", "avg", "median"]
comparisonOptions = ["gt", "lt", "eq"]
def validateArguments():
    if len(sys.argv) == 3 or len(sys.argv) == 5:
        if not os.path.isfile(sys.argv[1]):
            print("\""+sys.argv[1]+"\" is not a valid file path")
            sys.exit()
        if sys.argv[2] not in calculationOptions:
            print("\""+sys.argv[2]+"\" not recognized. Accepted values: sum, avg, median")
            sys.exit()
        if len(sys.argv) == 5:
            if sys.argv[3] not in comparisonOptions:
                print("\""+sys.argv[3]+"\" not recognized. Accepted values: gt, lt, eq")
                sys.exit()
            try:
                float(sys.argv[4])
            except:
                print("\""+sys.argv[4]+"\" needs to be a numerical value")
                sys.exit()
    else:
        print("Incorrect number of arguments:\nExample: codingtest.py <file_name> <sum|avg|median> [<gt|lt|eq> <n>]")
        sys.exit()


def calculate(calc, file):
    length = 0
    sum = 0.0
    avg = 0.0
    median = 0.0
    with open(file) as f:
        num_list = f.readlines()

    for num in num_list:
        sum+=float(num)
    
    length = len(num_list)

    if calc == "sum":
        print("Sum is: ",sum)
        return sum
    elif calc == "avg":
        avg = sum/length
        print("Average is: ",avg)
        return avg
    elif calc == "median":
        sorted_list = sorted(num_list, key=float)
        middle = float(length/2)
        if middle % 2 != 0:
            median = sorted_list[int(middle - .5)]
            print("Median is: ",median)
            return median
        else:
            median = (float(sorted_list[int(middle)])+float(sorted_list[int(middle-1)]))/2
            print("Median is: ",median)
            return median

def compare(arg, ans, comparison):
    if(arg=="gt"):
        if ans > comparison:
            print(ans," is greater than ",comparison)
        else:
            print(ans," is not greater than ",comparison)
    elif(arg=="lt"):
        if ans < comparison:
            print(ans," is lesser than ",comparison)
        else:
            print(ans," is not lesser than ",comparison)
    elif(arg=="eq"):
        if ans == comparison:
            print(ans," is equal to ",comparison)
        else:
            print(ans," is not equal to ",comparison)

def main():
    validateArguments()
    ans = calculate(sys.argv[2],sys.argv[1])
    if len(sys.argv) == 5:
        compare(sys.argv[3], ans, float(sys.argv[4]))


if __name__ == "__main__": main()

