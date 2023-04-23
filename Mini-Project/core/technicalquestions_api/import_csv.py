import csv
from technicalquestions_api.models import QuizQuestion

# Read the CSV file
with open('/home/ajay/final_technical_q_dataset_finalized.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Loop through the rows and create new QuizQuestion objects
    for row in reader:
        quiz_question = QuizQuestion(
            topic=row['Topic'],
            question=row['Question'],
            option_a=row['a'],
            option_b=row['b'],
            option_c=row['c'],
            option_d=row['d'],
            correct_answer=row['Correct Answer'],
            difficulty=row['Difficulty'],
            cognitive_level=row['Cognitive Level'],
            subject=row['Subject']
        )
        
        # Save the object to the database
        quiz_question.save()