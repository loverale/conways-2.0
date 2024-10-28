import tkinter as tk
import random

# primarily ui
class GameOfLife:
    def __init__(self, root, rows=30, cols=30, cell_size=20):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.running = False
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.initial_grid = [row[:] for row in self.grid]

        # set up the GUI
        self.canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size, bg="white")
        self.canvas.pack()

        # create buttons for control
        control_frame = tk.Frame(root)
        control_frame.pack()
        self.start_button = tk.Button(control_frame, text="Start", command=self.start)
        self.start_button.pack(side="left")
        self.stop_button = tk.Button(control_frame, text="Stop", command=self.stop)
        self.stop_button.pack(side="left")
        self.clear_button = tk.Button(control_frame, text="Clear", command=self.clear_grid)
        self.clear_button.pack(side="left")
        self.random_button = tk.Button(control_frame, text="Random", command=self.random_grid)
        self.random_button.pack(side="left")
        self.reset_button = tk.Button(control_frame, text="Reset", command=self.reset_grid)
        self.reset_button.pack(side="left")

        # bind click events for toggling cells
        self.canvas.bind("<Button-1>", self.toggle_cell)

    def draw_grid(self):
        self.canvas.delete("all")
        for row in range(self.rows):
            for col in range(self.cols):
                x0 = col * self.cell_size
                y0 = row * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                color = "black" if self.grid[row][col] == 1 else "white"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="gray")

    def toggle_cell(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        self.grid[row][col] = 1 - self.grid[row][col]
        self.draw_grid()

    def random_grid(self):
        self.grid = [[random.choice([0, 1]) for _ in range(self.cols)] for _ in range(self.rows)]
        self.draw_grid()

    def clear_grid(self):
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.draw_grid()

    def start(self):
        self.running = True
        self.initial_grid = [row[:] for row in self.grid]
        self.run_game()

    def stop(self):
        self.running = False

    def reset_grid(self):
        self.grid = [row[:] for row in self.initial_grid]
        self.draw_grid()

    def run_game(self):
        if not self.running:
            return
        self.update_grid()
        self.draw_grid()
        self.root.after(100, self.run_game)

    def update_grid(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                alive_neighbors = self.count_alive_neighbors(row, col)
                if self.grid[row][col] == 1:
                    new_grid[row][col] = 1 if alive_neighbors >= 2 else 0
                else:
                    new_grid[row][col] = 1 if alive_neighbors == 3 else 0
        self.grid = new_grid

    def count_alive_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c]
        return count


# create the main window and run the game
root = tk.Tk()
root.title("conways game of life, but new rules")
game = GameOfLife(root)
game.draw_grid()
root.mainloop()