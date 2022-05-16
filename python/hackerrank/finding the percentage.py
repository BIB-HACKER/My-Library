#Output Format

# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

# Sample Input 1

# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh
# Sample Output 1

# 26.50

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    s = 0
    
    for i in student_marks[query_name]:
        s+=i
        
    print("{0:.2f}".format(s/3))