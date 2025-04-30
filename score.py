
class InvalidScoreError(Exception):
    def __init__(self, score, message="Score must be between 0 and 100"):
        self.score = score
        self.message = message
        super().__init__(f"{self.message}. You entered: {score}")
def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(score)
    return f"Score {score} is valid."
try:
    user_input = input("Enter the exam score (0-100): ")
    score = float(user_input)  
    result = validate_score(score)
    print(result)

except InvalidScoreError as e:
    print(f"InvalidScoreError: {e}")

except ValueError:
    print("Invalid input. Please enter a numeric value.")
