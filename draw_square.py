import turtle
# 可以在电脑上移动并画东西的玩意

def draw_square(some_turtle):
    for i in range(0, 4):
        some_turtle.forward(100)  #turtle.forward(distance) 向前移动 这里是100像素
        some_turtle.right(90)  #turtle.right(angle) 向右转90度

# def draw_triangle(some_turtle):
#     for i in range(0, 3):
#         some_turtle.forward(100)
#         some_turtle.right(120)

def draw_art():    
    window = turtle.Screen()  # 创建一个屏幕
    window.bgcolor("orange")  # 背景颜色

    # Create the turtle Brad - Draw a square
    brad = turtle.Turtle()  # 开始画画 创建一个class Turtle 并将它起名为brad
    brad.shape("square")  # 设置乌龟形状
    brad.color("white")  # 设置线条颜色
    brad.speed(12)  #设置画画速度
    
    for i in range(0, 120):
        draw_square(brad)
        brad.right(3)

    # # Create teh turtle Angie - Draw a circle
    # angie = turtle.Turtle()  # 创建一个class Turtle 并给他起名为angie
    # angie.shape("circle")
    # angie.color("blue")
    # angie.circle(100)  # 设置圆的半径为100
    # # Create the turtle Koko - Draw a triangle
    # koko = turtle.Turtle()
    # koko.shape("arrow")
    # koko.color("red")
    # koko.speed(1)
    # draw_triangle(koko)
    
    window.exitonclick()  # 可以点击关闭这个屏幕窗口

draw_art()
