class_roster = ["Yaman", "Iswarya", "Neethu", "Durga"]
test_scores = [80, 81,84,87]
Cities_ZC = ["Plano", 75074, "Frisco", 75034]
print(class_roster)
print(test_scores)
print(Cities_ZC)

for student in class_roster:
    print(student)

for score in test_scores:
    print(score)


for i in range(len(class_roster)):
    student = class_roster[i]
    score = test_scores[i]
    print(student , score )