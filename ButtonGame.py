import tkinter as tk
import tkinter.messagebox
import time
import threading
import random

if __name__=="__main__":

    def game_th():
        global counter, stop_threads
        try:
            while(counter>=0):
                row=random.randrange(var_row.get())
                column=random.randrange(var_column.get())
                btn_dict[f"{row},{column}"]["bg"]="red"
                time.sleep(1.2)
                btn_dict[f"{row},{column}"]["bg"] = "white"
                if stop_threads:
                    stop_threads=False
                    break
        except:
            pass

    def timer_th():
        global counter, stop_threads, score
        while(counter>=0):
            lbl_time_c["text"]=counter
            counter -= 1
            time.sleep(1)
            if stop_threads:
                stop_threads=False
                break
        tkinter.messagebox.showinfo("Score", f"You scored: {score}")

    def color_tap(e):
        global th_timer,clicked, missed, score
        if th_game.is_alive():
            clicked+=1
            btn=e.widget
            if btn["bg"]=="red":
                score+=1
            else:
                missed+=1
            var_missed.set(missed)
            var_clicked.set(clicked)
            var_result.set(score)

    def start_game():
        global counter, clicked, missed, score, th_game, th_timer, stop_threads
        stop_threads=False
        counter = 120
        clicked = missed = score = 0
        th_game=threading.Thread(target=game_th)
        th_game.setDaemon(True)
        th_game.start()
        th_timer=threading.Thread(target=timer_th)
        th_timer.setDaemon(True)
        th_timer.start()

    btn_dict={}
    grid_count=0
    def create_grid():#Multiple frame over another can't be destroyed
        global frame_lower, btn_name, grid_count
        if grid_count==0:
            grid_count+=1
            frame_lower = tk.Frame(root)
            frame_lower.grid(row=1, column=0)
            s=""
            for i in range(var_row.get()):
                for j in range(var_column.get()):
                    btn_dict[f"{i},{j}"]=tk.Button(frame_lower, text=f"{i},{j}", bg="white", width="8")
                    btn_dict[f"{i},{j}"].bind("<Button-1>", color_tap)
                    btn_dict[f"{i},{j}"].grid(row=i, column=j)
            btn_start=tk.Button(frame_upper, text="Start", width=10, command=start_game)
            btn_start.grid(row=2, column=4)
        else:
            tkinter.messagebox.showinfo("Error", "Please reset the grid first!")

    def reset_grid():
            global frame_lower, counter, clicked, missed, score, stop_threads, btn_dict, grid_count
            frame_lower.destroy()
            stop_threads=True
            btn_dict.clear()
            counter = 120
            clicked = missed = score = 0
            lbl_time_c["text"]=counter
            var_result.set(0)
            var_clicked.set(0)
            var_missed.set(0)
            grid_count=0

    root = tk.Tk()
    root.state("zoomed")
    frame_upper = tk.Frame(root)
    frame_upper.grid(row=0, column=0)

    lbl_row = tk.Label(frame_upper, text="Row", width=6, anchor="w")
    lbl_row.grid(row=0, column=0)
    lbl_column = tk.Label(frame_upper, text="Column", width=6, anchor="w")
    lbl_column.grid(row=1, column=0)
    var_row = tk.IntVar()
    txt_row = tk.Entry(frame_upper, textvariable=var_row)
    txt_row.grid(row=0, column=1)
    var_column = tk.IntVar()
    txt_column = tk.Entry(frame_upper, textvariable=var_column)
    txt_column.grid(row=1, column=1)

    btn_create=tk.Button(frame_upper, text="Create Grid", width=10, command=create_grid)
    btn_create.grid(row=0, column=2)
    btn_reset=tk.Button(frame_upper, text="Reset", width=10, command=reset_grid)
    btn_reset.grid(row=1, column=2)

    lbl_clicked=tk.Label(frame_upper, text="Clicked", width=6, anchor="w")
    lbl_clicked.grid(row=0, column=3)
    lbl_missed=tk.Label(frame_upper, text="Missed", width=6, anchor="w")
    lbl_missed.grid(row=1, column=3)
    var_clicked = tk.StringVar()
    txt_clicked = tk.Entry(frame_upper, textvariable=var_clicked, state="disabled")
    txt_clicked.grid(row=0, column=4)
    var_missed = tk.StringVar()
    txt_missed = tk.Entry(frame_upper, textvariable=var_missed, state="disabled")
    txt_missed.grid(row=1, column=4)

    lbl_result=tk.Label(frame_upper, text="Score", width=6, anchor="w")
    lbl_result.grid(row=2, column=0)
    var_result=tk.StringVar()
    txt_result=tk.Entry(frame_upper, textvariable=var_result, state="disabled")
    txt_result.grid(row=2, column=1)

    lbl_time=tk.Label(frame_upper, text="Time", width=6, anchor="w")
    lbl_time.grid(row=2, column=2)
    lbl_time_c = tk.Label(frame_upper, text=120, width=6, anchor="w")
    lbl_time_c.grid(row=2, column=3)


    root.mainloop()