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