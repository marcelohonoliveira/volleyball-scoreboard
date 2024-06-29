import tkinter as tk
from PIL import Image, ImageTk
import random


class Team:
    def __init__(self, name, flag_image):
        self.name = name
        self.flag_image = flag_image
        self.points = 0
        self.sets = 0


class VolleyballScoreboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Placar de Vôlei")

        self.team_left = None
        self.team_right = None

        self.flag_images = self.load_flag_images()

        self.setup_teams()
        self.create_widgets()
        self.update_scoreboard()

        self.root.bind("<Left>", self.increase_left_score)
        self.root.bind("<Right>", self.increase_right_score)
        self.root.bind("e", self.decrease_left_score)
        self.root.bind("d", self.decrease_right_score)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def load_flag_images(self):
        # Carregando imagens de bandeiras
        flags = {}
        countries = ["Brazil", "USA", "Italy", "Japan", "France"]
        for country in countries:
            flags[country] = ImageTk.PhotoImage(
                Image.open(f"flags/{country}.png"))
        return flags

    def random_flag(self):
        # Criando uma bandeira aleatória
        random_flag = Image.new('RGB', (50, 30), (random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255)))
        return ImageTk.PhotoImage(random_flag)

    def setup_teams(self):
        # Configurar times
        left_name = input("Nome do time à esquerda: ")
        right_name = input("Nome do time à direita: ")

        left_flag = self.flag_images.get(left_name, self.random_flag())
        right_flag = self.flag_images.get(right_name, self.random_flag())

        self.team_left = Team(left_name, left_flag)
        self.team_right = Team(right_name, right_flag)

    def create_widgets(self):
        # Criar os widgets do placar
        self.left_team_label = tk.Label(
            self.root, text=self.team_left.name, font=("Helvetica", 16))
        self.left_team_label.grid(row=0, column=0, padx=20)

        self.left_flag_label = tk.Label(
            self.root, image=self.team_left.flag_image)
        self.left_flag_label.grid(row=1, column=0)

        self.right_team_label = tk.Label(
            self.root, text=self.team_right.name, font=("Helvetica", 16))
        self.right_team_label.grid(row=0, column=2, padx=20)

        self.right_flag_label = tk.Label(
            self.root, image=self.team_right.flag_image)
        self.right_flag_label.grid(row=1, column=2)

        self.left_score_label = tk.Label(
            self.root, text="0", font=("Helvetica", 48))
        self.left_score_label.grid(row=1, column=1, padx=20)

        self.right_score_label = tk.Label(
            self.root, text="0", font=("Helvetica", 48))
        self.right_score_label.grid(row=1, column=3, padx=20)

        self.left_sets_label = tk.Label(
            self.root, text="Sets: 0", font=("Helvetica", 16))
        self.left_sets_label.grid(row=2, column=0, padx=20)

        self.right_sets_label = tk.Label(
            self.root, text="Sets: 0", font=("Helvetica", 16))
        self.right_sets_label.grid(row=2, column=2, padx=20)

    def update_scoreboard(self):
        # Atualizar o placar
        self.left_score_label.config(text=str(self.team_left.points))
        self.right_score_label.config(text=str(self.team_right.points))
        self.left_sets_label.config(text=f"Sets: {self.team_left.sets}")
        self.right_sets_label.config(text=f"Sets: {self.team_right.sets}")

    def increase_left_score(self, event):
        self.team_left.points += 1
        self.check_set_winner()
        self.update_scoreboard()

    def increase_right_score(self, event):
        self.team_right.points += 1
        self.check_set_winner()
        self.update_scoreboard()

    def decrease_left_score(self, event):
        if self.team_left.points > 0:
            self.team_left.points -= 1
        self.update_scoreboard()

    def decrease_right_score(self, event):
        if self.team_right.points > 0:
            self.team_right.points -= 1
        self.update_scoreboard()

    def check_set_winner(self):
        if (self.team_left.points >= 25 or self.team_right.points >= 25) and (self.team_left.sets + self.team_right.sets < 4):
            if abs(self.team_left.points - self.team_right.points) >= 2:
                self.declare_set_winner()
        elif (self.team_left.points >= 15 or self.team_right.points >= 15) and (self.team_left.sets + self.team_right.sets == 4):
            if abs(self.team_left.points - self.team_right.points) >= 2:
                self.declare_set_winner()
        elif self.team_left.points == 8 and self.team_left.sets + self.team_right.sets == 4:
            self.switch_sides()
        elif self.team_right.points == 8 and self.team_left.sets + self.team_right.sets == 4:
            self.switch_sides()

    def declare_set_winner(self):
        if self.team_left.points > self.team_right.points:
            self.team_left.sets += 1
        else:
            self.team_right.sets += 1
        self.team_left.points = 0
        self.team_right.points = 0
        self.switch_sides()
        self.update_scoreboard()

    def switch_sides(self):
        self.team_left, self.team_right = self.team_right, self.team_left
        self.update_side_labels()

    def update_side_labels(self):
        self.left_team_label.config(text=self.team_left.name)
        self.left_flag_label.config(image=self.team_left.flag_image)
        self.right_team_label.config(text=self.team_right.name)
        self.right_flag_label.config(image=self.team_right.flag_image)

    def on_closing(self):
        self.root.destroy()
