#  Write a Python function student_result(**kwargs) that accepts subject names and marks, calculates total marks and percentage, identifies the highest-scoring subject, and displays Pass or Fail based on whether every subject has at least 40 marks.



def student_result(**kwargs):
    # Calculate total marks
    total_marks = sum(kwargs.values())
    
    # Calculate percentage
    percentage = total_marks / len(kwargs) if kwargs else 0
    
    # Identify highest-scoring subject
    highest_subject = max(kwargs, key=kwargs.get)
    highest_marks = kwargs[highest_subject]
    
    # Check pass/fail (every subject must have at least 40 marks)
    status = "Pass" if all(mark >= 40 for mark in kwargs.values()) else "Fail"
    
    # Display results
    print("Subjects and Marks:", kwargs)
    print("Total Marks:", total_marks)
    print("Percentage:", percentage)
    print("Highest Scoring Subject:", highest_subject, "with", highest_marks, "marks")
    print("Result:", status)


