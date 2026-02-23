feedback=["great service", "good quality", "fast delivery", "excellent support", "satisfied with the product    "]
print(feedback)
feedback.append("will recommend to others")
print(feedback)
feedback.remove("fast delivery")
print(feedback)
feedback[1]="good quality and value for money"
print(feedback)
if "excellent support" in feedback:
    print("Thank you for your positive feedback on our support!")
else:    print("We appreciate your feedback and will work on improving our support.")
print("Number of feedback entries:", len(feedback))
print("All feedback:")
for entry in feedback:    print("- " + entry)
feedback_count = len(feedback)
print("Total feedback entries:", feedback_count)
feedback_positive_count = sum(1 for entry in feedback if "good" in entry or "great" in entry or "excellent" in entry)
print("Number of positive feedback entries:", feedback_positive_count)