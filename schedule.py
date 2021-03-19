import csv
import bisect
import collections 

class Interval:
    def __init__(self, start, finish, value): 
        self.start  = start 
        self.finish = finish 
        self.value  = value

    def __str__(self):
        return "[Start: {0}, Finish: {1}, | Value: {2}]".format(self.start, self.finish, self.value)

def schedule(intervals):

    M = collections.defaultdict(float)      # dict holds most recent high value
    begin = [x.start for x in intervals]    # list holds start values
    end = [x.finish for x in intervals]     # list holds end values
    
    for i in range(len(intervals)+1):
        if i == 0: 
            M[0] = 0
        elif i == 1: 
            M[1] = intervals[0].value
        else:
            value_accrued = M[i-1]
            cur = intervals[i-1].value + M[bisect.bisect_left(end, begin[i-1])]
               
            if cur > value_accrued:
                M[i] = cur
            elif value_accrued >= cur:
                M[i] = M[i-1]

    return M[len(intervals)]

# Wraps schedule()
# Takes individual file name and returns max value
def test(file):
    intervals = []
    with open(file, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line in csv_reader:
            intervals.append(Interval(float(line['START']), 
            float(line['FINISH']), 
            float(line['VALUE'])))

    # Sort intervals by non-decreasing order
    intervals.sort(key=lambda start: start.finish)
    return(schedule(intervals))

# Tests file input
def isFile(fn):
    try:
      open(fn, "r")
      return True
    except IOError:
      print ("Nice try, file doesn't exist!")
      return False

def main():

    # Internal test files
    test_files = ["requests-a.csv", "requests-b.csv",
                    "requests-c.csv", "requests-d.csv"]
    
    # Tests internal test files
    for file in test_files:
        print("Max weight for", file, "is", test(file))

    # User is given option to test their own file
    while "valid":
        preference = str(input("Test your own file? (y/n) ")).lower().strip()
        if preference[:1] == 'y':
            user_file = str(input("CSV file name: ")).strip()
            if isFile(user_file):
                print("Max weight for", user_file, "is", test(user_file))
            else:
                return False
            return True
        if preference[:1] == 'n':
            return False
        
if __name__ == "__main__":
    main()