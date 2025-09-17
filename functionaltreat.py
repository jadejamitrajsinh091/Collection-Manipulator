# List of student marks

smark = [75, 56, 53, 59, 85, 47, 69, 77, 81, 61, 63, 54, 58, 57, 74, 84, 94, 62, 79, 88]

# Basic analysis

total_students = len(smark)

if total_students == 0:
    print("No marks available to analyze.")

else:
    print("Student marks analysis")
 
    highest_mark = max(smark)
    lowest_mark = min(smark)
    total_sum = sum(smark)
    average_mark = total_sum / total_students

    pass_count = 0
    fail_count = 0
    perfect_count = 0

    for A in smark:
        if A >= 40:
            pass_count += 1

        else:              
            fail_count += 1

        if A == 100:
            perfect_count += 1

    pass_percentage = (pass_count / total_students) * 100

    print(f"Total students : {total_students}")
    print(f"Highest mark   : {highest_mark}")
    print(f"Lowest mark    : {lowest_mark}")
    print(f"Average mark   : {average_mark}")
    print(f"Passed (>=40)  : {pass_count}")
    print(f"Failed (<40)   : {fail_count}")
    print(f"Scored 100     : {perfect_count}")
    print(f"Pass percent   : {pass_percentage}%")

    ascending = sorted(smark)
    descending = sorted(smark, reverse=True)
    print(f"Ascending order : {ascending}")
    print(f"Descending order: {descending}")

    u_sorted = sorted(set(smark))

    if len(u_sorted) >= 2:
        second_lowest = u_sorted[1]
        second_highest = u_sorted[-2]
        print(f"Second lowest   : {second_lowest}")
        print(f"Second highest  : {second_highest}")

    else:
        print("Not enough distinct values to determine second highest/lowest.")

