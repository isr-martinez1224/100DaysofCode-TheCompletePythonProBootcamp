student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score = sum(student_scores)

total_sum = 0
for score in student_scores:
    total_sum += score

print(total_sum)

print(max(student_scores))

high_score = 0
for num in student_scores:
    if high_score < num:
        high_score = num
print(high_score)


print(range(1, 10))
