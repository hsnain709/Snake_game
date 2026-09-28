import tkinter as tk

def game_over_screen(play_area, high_score, score, current_difficulty, change_difficulty):
        global buttons_gm
        play_area.create_text(
                                300, 250,
                                text="GAME OVER",
                                font=("Arial", 30, "bold"))
        play_area.create_text(
                                300, 285,
                                text=f"Total score: {score}",
                                font=("Arial", 20, "bold")
                                
                                
                        )

        play_area.create_text(
                                        300, 310,
                                        text=f"High score: {high_score}",
                                        font=("Arial", 20, "bold")
                                        
                                        
                                )
        
        play_area.create_text(
                                                300, 335,
                                                text="Press R to play again",
                                                font=("Arial", 15, "bold")
                                                
                                                
                                        )

        play_area.create_text(
                                                300, 410,
                                                text="Or change difficulty:",
                                                font=("Arial", 20, "bold"))

        buttons_gm = []
        position = 0
        x_positions = [95, 235, 375]

        if current_difficulty != "super_easy":
                button_s_gm = tk.Button(play_area, text="SUPER EASY", bg="lime", fg="black", command=lambda: change_difficulty("super_easy"))
                button_s_gm.place(x=x_positions[position], y=440, width=130, height=40)
                position += 1
                buttons_gm.append(button_s_gm)

        if current_difficulty != "easy":
                button_e_gm = tk.Button(play_area, text="EASY", bg="green", fg="black", command=lambda: change_difficulty("easy"))
                button_e_gm.place(x=x_positions[position], y=440, width=130, height=40)
                position += 1
                buttons_gm.append(button_e_gm)

        if current_difficulty != "medium":
                button_m_gm = tk.Button(play_area, text="MEDIUM",  bg="yellow", fg="black", command=lambda: change_difficulty("medium"))
                button_m_gm.place(x=x_positions[position], y=440, width=130, height=40)
                buttons_gm.append(button_m_gm)
                position += 1

        if current_difficulty != "hard":
                button_h_gm = tk.Button(play_area, text="HARD",  bg="red", fg="black", command=lambda: change_difficulty("hard"))
                button_h_gm.place(x=x_positions[position], y=440, width=130, height=40)
                buttons_gm.append(button_h_gm)
                position +=1
        
        return buttons_gm