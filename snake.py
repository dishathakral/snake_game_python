from turtle import  Turtle
directions=["up","down","right","left"]
MOVE_DISTANCE=10
#self.t_list[0]=head
class Snake:
    def __init__(self):
        self.t_list=[]
        self.create_snake()
        self.direction='right'
    def create_snake(self):
        x_position = [-40, -20, 0]
        for i in range(len(x_position)):
            t = Turtle()
            t.penup()
            t.shape('square')
            t.setposition(y=0, x=x_position[i])
            t.color('white')
            self.t_list.append(t)
    def move(self):

        for i in range(len(self.t_list) - 1, 0, -1):  # Correct range
            self.t_list[i].goto(self.t_list[i - 1].xcor(),
                           self.t_list[i - 1].ycor())# Move current segment to the previous one's position
        self.t_list[0].forward(MOVE_DISTANCE)
        if self.t_list[0].xcor() >= 350:
            for t in self.t_list:
                t.setx(-400)


    def up(self):
        if self.direction!='down':
            self.direction = 'up'
            self.t_list[0].setheading(90)

    def down(self):
        if self.direction!='up':
            self.direction = 'down'
            self.t_list[0].setheading(270)

    def left(self):
        if self.direction!='right':
            self.direction = 'left'
            self.t_list[0].setheading(180)

    def right(self):
        if self.direction!='left':
            self.direction = 'right'
            self.t_list[0].setheading(0)
    def grow(self):
        new_segment=Turtle()
        new_segment.penup()
        new_segment.shape('square')
        new_segment.color('white')
        #new segment will go to position of last segment
        last_segment=self.t_list[-1]
        new_segment.goto(last_segment.xcor(),last_segment.ycor())

        self.t_list.append(new_segment)
    def collision_with_wall(self):
        if self.t_list[0].xcor()>360 or self.t_list[0].xcor()<-360:
            return True
        if self.t_list[0].ycor()>340 or self.t_list[0].ycor()<-340:
            return True
        return False



