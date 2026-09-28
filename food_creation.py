import random

def create_food(snake, better_food, e_obstacles, m_obstacles, h_obstacles):
        while True:
                x = random.randint(0, 29)
                y = random.randint(0, 29)

                food = (x, y)
                food_x, food_y = food
                if (food not in snake and (better_food is None or food != better_food)
                     and (e_obstacles is None or food not in e_obstacles)
                     and (m_obstacles is None or food not in m_obstacles)
                     and (h_obstacles is None or food not in h_obstacles)):
                        break

        return food, food_x, food_y

def create_better_food(snake, food, e_obstacles, m_obstacles, h_obstacles):
        while True:
                x = random.randint(0, 29)
                y = random.randint(0, 29)

                better_food = (x, y)
                better_food_x, better_food_y = better_food
                if (better_food not in snake and (better_food is None or better_food != food)
                     and (e_obstacles is None or better_food not in e_obstacles)
                     and (m_obstacles is None or better_food not in m_obstacles)
                     and (h_obstacles is None or better_food not in h_obstacles)):
                        break

        return better_food, better_food_x, better_food_y