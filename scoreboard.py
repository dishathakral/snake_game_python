from turtle import Turtle
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score=0
        self.highest_score = self.load_high_score()
        self.goto(0, 320)
        self.update_score()
        self.score_list=[]
    def update_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))
    def increase_score(self):
        self.score=self.score+1
        self.update_score()

    def load_high_score(self):
        """Loads the highest score from a file."""
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())  # ✅ Read the highest score
        except (FileNotFoundError, ValueError):  # If file is missing or corrupted
            return 0  # Default high score is 0

    def save_high_score(self):
        """Saves the highest score to a file."""
        with open("high_score.txt", "w") as file:
            file.write(str(self.highest_score))

    def game_over(self):
        self.goto(0, 0)
        self.score_list.append(self.score)
        # ✅ Check if new high score is achieved
        if self.score > self.highest_score:
            self.highest_score = self.score  # ✅ Update high score
            self.save_high_score()
        self.write(f"GAME OVER\nYour Score: {self.score}\nHighest Score: {self.highest_score}",
                   align="center", font=("Arial", 20, "bold"))




