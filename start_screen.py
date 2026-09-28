import tkinter as tk

def start_screen(play_area, start):
        play_area.create_text(
                                300, 200,
                                text="SNAKE!",
                                font=("Arial", 30, "bold"))

        play_area.create_text(
                                                300, 260,
                                                text="Select a difficulty to start.",
                                                font=("Arial", 15, "bold")
                                                
                                                
                                     )
        
        buttons = []
        button_s = tk.Button(play_area, text="SUPER EASY", bg="lime", fg="black", command=lambda: start(buttons, "super_easy"))
        button_s.place(x=235, y=300, width=130, height=40)
        buttons.append(button_s)

        button_e = tk.Button(play_area, text="EASY", bg="green", fg="black", command=lambda: start(buttons, "easy"))
        button_e.place(x=235, y=350, width=130, height=40)
        buttons.append(button_e)
        
        button_m = tk.Button(play_area, text="MEDIUM",  bg="yellow", fg="black", command=lambda: start(buttons, "medium"))
        button_m.place(x=235, y=400, width=130, height=40)
        buttons.append(button_m)

        button_h = tk.Button(play_area, text="HARD",  bg="red", fg="black", command=lambda: start(buttons, "hard"))
        button_h.place(x=235, y=450, width=130, height=40)
        buttons.append(button_h)

        return buttons