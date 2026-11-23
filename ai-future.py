import random
class AITeacher:
    def __init__(self):
        self.bullish = 78
        self.robots = 10
    def ai_brain_response(self, subject, question):
        if subject == "Maths":
            return f"2+2=4 - Biyu da biyu hudu ne! - {question} - Bullish {self.bullish}%"
        elif subject == "English":
            return f"My name is BRB AI! - {question}"
        else:
            return f"BRB AI - {subject} - {question} - Bullish {self.bullish}%"

ai = AITeacher()
print(ai.ai_brain_response("Maths", "What is 2+2?"))
