import csv

# Some constants from the assignment description
POINTS_POSIBLE_QUIZZES = 120
POINTS_POSSIBLE_HOMEWORK = 150
POINTS_POSSIBLE_TEAM_PROJECT = 55
POINTS_POSSIBLE_FINAL_EXAM = 80
WEIGHT_QUIZ = 0.15
WEIGHT_HOMEWORK = 0.25
WEIGHT_TEAM_PROJECT = 0.25
WEIGHT_FINAL_EXAM = 0.35

# If you renamed the file you will need to update this to match
FILE_NAME = "Python-HW-WeightedSums-Data.csv"


def csv_read() -> list:
    with open(FILE_NAME, 'r') as data:
        csv_reader = csv.DictReader(data)
        results = [row for row in csv_reader]
    return results

# Helper: Calculate final grade for a student dict
def calculate_final_grade(student):
    quiz_score = float(student["Quizzes"]) / POINTS_POSIBLE_QUIZZES * WEIGHT_QUIZ * 100
    hw_score = float(student["Homework"]) / POINTS_POSSIBLE_HOMEWORK * WEIGHT_HOMEWORK * 100
    project_score = float(student["Team Project"]) / POINTS_POSSIBLE_TEAM_PROJECT * WEIGHT_TEAM_PROJECT * 100
    final_exam_score = float(student["Final Exam"]) / POINTS_POSSIBLE_FINAL_EXAM * WEIGHT_FINAL_EXAM * 100
    total_score = quiz_score + hw_score + project_score + final_exam_score
    return round(total_score, 2)

# Question 1
def question_one_grade_calculation(data) -> None:
    for student in data:
        final_grade = calculate_final_grade(student)
        print(f"{student['Name']} has a grade of {final_grade} in the course.")

# Question 2
def question_two_grade_needed_on_final(data) -> None:
    no_final_missing = True
    for student in data:
        final_exam_score = float(student["Final Exam"])
        if final_exam_score == 0:
            no_final_missing = False
            # Calculate score without Final Exam
            quiz_score = float(student["Quizzes"]) / POINTS_POSIBLE_QUIZZES * WEIGHT_QUIZ * 100
            hw_score = float(student["Homework"]) / POINTS_POSSIBLE_HOMEWORK * WEIGHT_HOMEWORK * 100
            project_score = float(student["Team Project"]) / POINTS_POSSIBLE_TEAM_PROJECT * WEIGHT_TEAM_PROJECT * 100
            current_total = quiz_score + hw_score + project_score

            needed_total = 90
            remaining_needed = needed_total - current_total
            needed_percentage_on_final = remaining_needed / (WEIGHT_FINAL_EXAM * 100)
            needed_score_on_final = needed_percentage_on_final * POINTS_POSSIBLE_FINAL_EXAM

            if needed_score_on_final > POINTS_POSSIBLE_FINAL_EXAM:
                print(f"{student['Name']} cannot get an A in the course.")
            else:
                needed_score_on_final = max(0, round(needed_score_on_final, 2))
                print(f"{student['Name']} needs a score of at least {needed_score_on_final} on the final to get an A.")
    if no_final_missing:
        print("All students have a Final score.")

# Question 3
def question_three_weakness(data) -> None:
    for student in data:
        quiz_percent = float(student["Quizzes"]) / POINTS_POSIBLE_QUIZZES
        hw_percent = float(student["Homework"]) / POINTS_POSSIBLE_HOMEWORK
        project_percent = float(student["Team Project"]) / POINTS_POSSIBLE_TEAM_PROJECT
        final_percent = float(student["Final Exam"]) / POINTS_POSSIBLE_FINAL_EXAM

        weighted_scores = [
            quiz_percent * WEIGHT_QUIZ,
            hw_percent * WEIGHT_HOMEWORK,
            project_percent * WEIGHT_TEAM_PROJECT,
            final_percent * WEIGHT_FINAL_EXAM
        ]

        max_scores = [WEIGHT_QUIZ, WEIGHT_HOMEWORK, WEIGHT_TEAM_PROJECT, WEIGHT_FINAL_EXAM]
        losses = [max_scores[i] - weighted_scores[i] for i in range(4)]
        max_loss = max(losses)

        final_grade = calculate_final_grade(student)
        if final_grade >= 100:
            print(f"{student['Name']} got a perfect score in the course.")
        else:
            worst_areas = []
            categories = ["Quizzes", "Homework", "Team Project", "Final Exam"]
            for i in range(4):
                if abs(losses[i] - max_loss) < 1e-6:
                    worst_areas.append(categories[i])

            if len(worst_areas) == 1:
                print(f"{student['Name']} lost the most score in {worst_areas[0]}.")
            else:
                print(f"{student['Name']} had multiple areas that held them back.")

# Question 4
def question_four_equal_students(data) -> None:
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            s1 = data[i]
            s2 = data[j]
            if (
                    s1["Quizzes"] == s2["Quizzes"]
                    and s1["Homework"] == s2["Homework"]
                    and s1["Team Project"] == s2["Team Project"]
                    and s1["Final Exam"] == s2["Final Exam"]
            ):
                print(f"{s1['Name']} and {s2['Name']} have the same scores.")
                return
    print("No students had matching scores.")

def main() -> None:
    data = csv_read()
    question_one_grade_calculation(data)
    question_two_grade_needed_on_final(data)
    question_three_weakness(data)
    question_four_equal_students(data)

if __name__ == '__main__':
    main()

