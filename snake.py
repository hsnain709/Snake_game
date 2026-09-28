import tkinter as tk
import random
import time
import os
import sys
from food_creation import create_food, create_better_food
from obstacles import load_easy_obstacles, draw_easy_obstacles, load_medium_obstacles, draw_medium_obstacles, load_hard_obstacles, draw_hard_obstacles
from start_screen import start_screen
from game_over_screen import game_over_screen
area = tk.Tk()
area.title("Snake Game")

cell_size = 20
grid_size = 30
board_size = cell_size * grid_size

high_score = 0
folder = os.path.dirname(os.path.abspath(sys.executable))
high_score_file = os.path.join(folder, "high_score.txt")
with open (high_score_file, "r") as file:
        high_score = int(file.read())

high_score_text = tk.Label(
                                area, 
                                text=f"High score: {high_score}",
                                font=("Arial", 20, "bold")
                        )
high_score_text.pack()

score_text = tk.Label(
                                area, 
                                text=f"Score: 0",
                                font=("Arial", 20, "bold")
                        )
score_text.pack()


play_area = tk.Canvas(area, width=board_size, height=board_size, takefocus=True, bg="white")
play_area.focus_set()
play_area.pack()


def draw_grid():
        for x in range(grid_size):
                for y in range(grid_size):
                        play_area.create_rectangle(x * cell_size, y * cell_size,
                                   (x + 1) * cell_size, (y + 1) * cell_size) 

snake = [(15, 15), (14, 15), (13, 15)]
score = 0
direction = "right"
next_direction = "right"
direction_locked = False
growth = 0
speed = 200
appear_time = 0
delete_time = 0
current_time = 0
appear_expire_time = 0
delete_expire_time = 0
paused_appear_timer = False
paused_delete_timer = False

buttons_gm = []
current_difficulty = None
e_obstacles = None
m_obstacles = None
h_obstacles = None

better_food = None
better_food_x = None
better_food_y = None
better_square = None
food = None
food_x = None
food_y = None
better_food_delete_timer = None


game_over = False
start_game = True


def start(buttons, difficulty):
        global start_game, better_food_appear_timer, appear_time, appear_expire_time, current_time, food, current_difficulty
        if start_game == True:
                start_game = False
                play_area.delete("all")

                for button in buttons:
                        button.destroy()
                
                appear_time = random.randint(15000, 25000)
                current_time = time.time() * 1000
                better_food_appear_timer = play_area.after(appear_time, appear_better_food)
                appear_expire_time = current_time + appear_time

                if difficulty == "easy":
                        easy_obstacles()
                        current_difficulty = "easy"
                        food, food_x, food_y = create_food(snake, better_food, e_obstacles, m_obstacles, h_obstacles)
                elif difficulty == "medium":
                        medium_obstacles()
                        current_difficulty = "medium"
                        food, food_x, food_y = create_food(snake, better_food, e_obstacles, m_obstacles, h_obstacles)
                elif difficulty == "hard":
                        hard_obstacles()
                        current_difficulty = "hard"
                        food, food_x, food_y = create_food(snake, better_food, e_obstacles, m_obstacles, h_obstacles)
                else:
                        current_difficulty = "super_easy"
                        food, food_x, food_y = create_food(snake, better_food, e_obstacles, m_obstacles, h_obstacles)
                        

                draw_grid()
                draw_snake()
                draw_food(food_x, food_y)
                move()

start_screen(play_area, start)

def easy_obstacles():
        global e_obstacles
        e_obstacles = load_easy_obstacles()
        draw_easy_obstacles(e_obstacles, play_area, cell_size)

def medium_obstacles():
        global m_obstacles
        m_obstacles = load_medium_obstacles()
        draw_medium_obstacles(m_obstacles, play_area, cell_size)

def hard_obstacles():
        global h_obstacles
        h_obstacles = load_hard_obstacles()
        draw_hard_obstacles(h_obstacles, play_area, cell_size)

def change_difficulty( new_difficulty):
        global current_difficulty
        current_difficulty = new_difficulty
        play_again()

def delete_better_food():
        global better_square, better_food_appear_timer, better_food, better_food_x, better_food_y, better_food_delete_timer, appear_time, current_time, appear_expire_time
        play_area.delete(better_square)
        better_square = None
        better_food = None
        better_food_delete_timer = None

        
        appear_time = random.randint(15000, 25000)
        current_time = time.time() * 1000
        better_food_appear_timer = play_area.after(appear_time, appear_better_food)
        appear_expire_time = current_time + appear_time

def draw_snake():
        for x, y in snake:
                play_area.create_rectangle(x * cell_size, y * cell_size,
                                                        (x + 1) * cell_size, (y + 1) * cell_size, fill="green")

def draw_food(food_x, food_y):
        play_area.create_rectangle(food_x * cell_size, food_y * cell_size,
                                   (food_x + 1) * cell_size, (food_y + 1) * cell_size, fill="red")
        

def draw_better_food(better_food_x, better_food_y):
        global better_square, better_food_delete_timer, delete_time, current_time, delete_expire_time

        better_square = play_area.create_rectangle(better_food_x * cell_size, better_food_y * cell_size,
                                   (better_food_x + 1) * cell_size, (better_food_y + 1) * cell_size, fill="yellow")

        delete_time = random.randint(7000, 10000)
        current_time = time.time() * 1000
        better_food_delete_timer = play_area.after(delete_time, delete_better_food)
        delete_expire_time = current_time + delete_time

def appear_better_food():
        global better_food, better_food_x, better_food_y, better_food_appear_timer
        better_food_appear_timer = None
        better_food, better_food_x, better_food_y = create_better_food(snake, better_food, e_obstacles, m_obstacles, h_obstacles)
        draw_better_food(better_food_x, better_food_y)

def move_up(event):
        global next_direction, direction_locked
        if not paused:
                if not direction_locked and direction != "down":
                        next_direction = "up"
                        direction_locked = True
      
        
def move_down(event):
        global next_direction, direction_locked
        if not paused:
                if not direction_locked and direction != "up":
                        next_direction = "down"
                        direction_locked = True

def move_left(event):
        global next_direction, direction_locked
        if not paused:
                if not direction_locked and direction != "right":
                        next_direction = "left"
                        direction_locked = True

def move_right(event):
        global next_direction, direction_locked
        if not paused:
                if not direction_locked and direction != "left":
                        next_direction = "right"
                        direction_locked = True

def move():
        global food, buttons_gm, better_food, score, game_over, growth, speed, direction, next_direction, direction_locked, high_score, better_food_appear_timer, better_food_delete_timer, better_square, appear_time, current_time, appear_expire_time

        if game_over or paused:
                return
        
        direction = next_direction
        x, y = snake[0]

        if direction == "up":
                new_head = (x, y - 1)
        elif direction == "down":
                new_head = (x, y + 1)
        elif direction == "left":
                new_head = (x - 1, y)
        elif direction == "right":
                new_head = (x + 1, y)
        new_x, new_y = new_head

        if ((new_x < 0 or new_x >=grid_size or new_y < 0 or new_y >=grid_size)
             or new_head in snake or (e_obstacles is not None and new_head in e_obstacles)
              or (m_obstacles is not None and new_head in m_obstacles)
              or (h_obstacles is not None and new_head in h_obstacles)):
                buttons_gm = game_over_screen(play_area, high_score, score, current_difficulty, change_difficulty)
                game_over = True
                return

        tail_x, tail_y = snake[-1]
        ate_food = new_head == food
        ate_better_food = better_food is not None and new_head == better_food
        
        snake.insert(0, new_head)

        if ate_food or ate_better_food:
                removed_tail = False

        elif growth > 0:
                growth -= 1
                removed_tail = False

        else:
         snake.pop()
         removed_tail = True

        play_area.create_rectangle(new_x * cell_size, new_y * cell_size,
    (new_x + 1) * cell_size, (new_y + 1) * cell_size,fill="green")
        
        if ate_food:
                score += 1
                if score > high_score:
                        high_score = score

                        with open("high_score.txt", "w") as file:
                                file.write(str(high_score))


                score_text.config(text=f"Score: {score}")
                high_score_text.config(text=f"High score: {high_score}")

                
                food, food_x, food_y = create_food(snake, better_food, e_obstacles, m_obstacles, h_obstacles)
                draw_food(food_x, food_y)

                if h_obstacles is None:
                        if score % 5 == 0 and score < 21:
                                speed -= 20

        if ate_better_food:
                score += 3
                growth += 2
                if score > high_score:
                        high_score = score

                        with open("high_score.txt", "w") as file:
                                file.write(str(high_score))


                score_text.config(text=f"Score: {score}")
                high_score_text.config(text=f"High score: {high_score}")

                if better_food_delete_timer is not None:
                        play_area.after_cancel(better_food_delete_timer)
                        better_food_delete_timer = None

                play_area.delete(better_square)
                better_square = None
                better_food = None

                appear_time = random.randint(15000, 25000)
                current_time = time.time() * 1000
                better_food_appear_timer = play_area.after(appear_time, appear_better_food)
                appear_expire_time = current_time + appear_time
                                
                if h_obstacles is None:
                        if score % 5 == 0 or (score - 2) % 5 == 0 or (score - 1) % 5 == 0 and score < 21:
                                speed -= 20


        if removed_tail:
                play_area.create_rectangle(tail_x * cell_size, tail_y * cell_size,
                                   (tail_x+ 1) * cell_size, (tail_y + 1) * cell_size, fill="white")


        direction_locked = False
        play_area.after(speed, move)

paused = False
paused_text = None
p_held = False

def pause(event):
        global paused, paused_text, p_held, direction_locked, current_time, appear_expire_time, delete_expire_time, better_food_appear_timer, better_food_delete_timer, appear_time, delete_time, paused_appear_timer, paused_delete_timer
        if p_held:
                return
        p_held = True

        if paused:
                paused = False
                play_area.delete(paused_text)
                paused_text = None

                if paused_appear_timer:
                        better_food_appear_timer = play_area.after(appear_time, appear_better_food)
                        paused_appear_timer = False
                elif paused_delete_timer:
                        better_food_delete_timer = play_area.after(delete_time, delete_better_food)
                        paused_delete_timer = False
                move()
                

        else:
                paused = True

                current_time = time.time() * 1000

                if better_food_appear_timer is not None:
                        play_area.after_cancel(better_food_appear_timer)
                        appear_time = int(appear_expire_time - current_time)
                        paused_appear_timer = True

                elif better_food_delete_timer is not None:
                        play_area.after_cancel(better_food_delete_timer)
                        delete_time = int(delete_expire_time - current_time)
                        paused_delete_timer = True

                paused_text = play_area.create_text(
                        60, 30, 
                        text="PAUSED",
                        font=("Arial", 20, "bold")
                )

def release_p(event):
        global p_held
        p_held = False


def play_again(event=None):
        global game_over, buttons_gm, snake, food, direction, score, growth, speed, paused, direction_locked, next_direction, score_text, better_square, better_food, better_food_x, better_food_y, better_food_delete_timer, better_food_appear_timer, appear_time, current_time, appear_expire_time, current_difficulty, e_obstacles, m_obstacles, h_obstacles

        if game_over == True:
                snake = [(15, 15), (14, 15), (13, 15)]
                score = 0
                direction = "right"
                next_direction = "right"
                direction_locked = False
                speed = 200
                growth = 0
                paused = False

                for button in buttons_gm:
                        button.destroy()

                game_over = False

                if better_square != None:
                        play_area.delete(better_square)
                        better_square = None
                
                if better_food_appear_timer is not None:
                        play_area.after_cancel(better_food_appear_timer)
                        better_food_appear_timer = None

                if better_food_delete_timer is not None:
                        play_area.after_cancel(better_food_delete_timer)
                        better_food_delete_timer = None

                play_area.delete("all")

                score_text.config(text="Score: 0")
                high_score_text.config(text=f"High score: {high_score}")
                
                draw_grid()
                                
                draw_snake()

                if e_obstacles is not None:
                        e_obstacles = None

                elif m_obstacles is not None:
                        m_obstacles = None

                elif h_obstacles is not None:
                        h_obstacles = None

                if current_difficulty == "easy":
                                        easy_obstacles()
                                        
                                        
                elif current_difficulty == "medium":
                                        medium_obstacles()
                                        
                                        
                elif current_difficulty == "hard":
                                        hard_obstacles()
                                        
                                        
                else:
                                        current_difficulty = "super_easy"

                                        

                food, food_x, food_y  = create_food(snake, better_food, e_obstacles, m_obstacles, h_obstacles)
                better_food = None
                better_food_x = None
                better_food_y = None

                draw_food(food_x, food_y)

                appear_time = random.randint(15000, 25000)
                current_time = time.time() * 1000
                better_food_appear_timer = play_area.after(appear_time, appear_better_food)
                appear_expire_time = current_time + appear_time
                                
                move()

play_area.bind("<Up>", move_up)
play_area.bind("<Down>", move_down)
play_area.bind("<Left>", move_left)
play_area.bind("<Right>", move_right)
play_area.bind("<r>", play_again)
play_area.bind("<p>", pause)
play_area.bind("<KeyRelease-p>", release_p)

play_area.mainloop()