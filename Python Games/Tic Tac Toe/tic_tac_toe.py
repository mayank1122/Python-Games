#!/usr/bin/env python3
"""Two-player Tic-Tac-Toe with a polished desktop UI and saved scores.

This source code is AI-generated. It was written by an AI coding assistant
in Cursor and was not hand-written as an original human implementation.
"""

import json
import tkinter as tk
from pathlib import Path

SCORES_PATH = Path(__file__).with_name("scores.json")

BG = "#0b1020"
BG_RAISED = "#141b2d"
CARD = "#1c2640"
CARD_EDGE = "#2a3654"
LINE = "#33415f"
TEXT = "#f4f7fb"
MUTED = "#93a0b8"
X_COLOR = "#5eead4"
O_COLOR = "#fb7185"
WIN = "#fbbf24"
HOVER = "#243152"
BTN = "#2563eb"
BTN_HOVER = "#1d4ed8"
GHOST = "#243049"


def load_scores():
    if not SCORES_PATH.exists():
        return {}
    try:
        data = json.loads(SCORES_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    if not isinstance(data, dict):
        return {}
    clean = {}
    for name, record in data.items():
        if isinstance(record, dict):
            clean[str(name)] = {
                "wins": int(record.get("wins", 0)),
                "losses": int(record.get("losses", 0)),
                "draws": int(record.get("draws", 0)),
            }
    return clean


def save_scores(scores):
    SCORES_PATH.write_text(
        json.dumps(scores, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def record_for(scores, name):
    return scores.setdefault(name, {"wins": 0, "losses": 0, "draws": 0})


class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.geometry("760x860")

        self.scores = load_scores()
        self.names = ["Player 1", "Player 2"]
        self.marks = ("X", "O")
        self.colors = (X_COLOR, O_COLOR)
        self.board = [""] * 9
        self.turn = 0
        self.game_over = False
        self.winning_line = []
        self.hover_cell = None

        self._build()
        self._center()
        self._draw_board()
        self.after(120, self._ask_names)

    def _center(self):
        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        x = (self.winfo_screenwidth() - w) // 2
        y = (self.winfo_screenheight() - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _build(self):
        header = tk.Frame(self, bg=BG)
        header.pack(fill="x", padx=36, pady=(28, 6))

        tk.Label(
            header,
            text="TIC TAC TOE",
            font=("Helvetica Neue", 28, "bold"),
            fg=TEXT,
            bg=BG,
        ).pack(anchor="w")
        tk.Label(
            header,
            text="Two players  ·  scores saved on this computer",
            font=("Helvetica Neue", 13),
            fg=MUTED,
            bg=BG,
        ).pack(anchor="w", pady=(2, 0))

        cards = tk.Frame(self, bg=BG)
        cards.pack(fill="x", padx=36, pady=(18, 8))
        cards.columnconfigure(0, weight=1)
        cards.columnconfigure(1, weight=1)

        self.card_frames = []
        self.name_labels = []
        self.score_labels = []
        self.mark_labels = []

        for index, side in enumerate(("left", "right")):
            card = tk.Frame(
                cards,
                bg=CARD,
                highlightbackground=CARD_EDGE,
                highlightthickness=1,
                padx=16,
                pady=14,
            )
            card.grid(row=0, column=index, sticky="nsew", padx=(0 if index == 0 else 8, 8 if index == 0 else 0))
            mark = tk.Label(
                card,
                text=self.marks[index],
                font=("Helvetica Neue", 22, "bold"),
                fg=self.colors[index],
                bg=CARD,
            )
            mark.pack(anchor="w")
            name = tk.Label(
                card,
                text=self.names[index],
                font=("Helvetica Neue", 16, "bold"),
                fg=TEXT,
                bg=CARD,
                anchor="w",
            )
            name.pack(anchor="w", pady=(2, 0))
            score = tk.Label(
                card,
                text="0 wins",
                font=("Helvetica Neue", 12),
                fg=MUTED,
                bg=CARD,
                anchor="w",
            )
            score.pack(anchor="w")
            self.card_frames.append(card)
            self.mark_labels.append(mark)
            self.name_labels.append(name)
            self.score_labels.append(score)

        self.status = tk.Label(
            self,
            text="",
            font=("Helvetica Neue", 15, "bold"),
            fg=TEXT,
            bg=BG,
        )
        self.status.pack(pady=(10, 6))

        board_wrap = tk.Frame(
            self,
            bg=BG_RAISED,
            highlightbackground=CARD_EDGE,
            highlightthickness=1,
        )
        board_wrap.pack(padx=36, pady=8)
        self.canvas = tk.Canvas(
            board_wrap,
            width=560,
            height=560,
            bg=BG_RAISED,
            highlightthickness=0,
            bd=0,
        )
        self.canvas.pack(padx=18, pady=18)
        self.canvas.bind("<Button-1>", self._on_click)
        self.canvas.bind("<Motion>", self._on_motion)
        self.canvas.bind("<Leave>", lambda _e: self._set_hover(None))

        self.result_panel = tk.Frame(
            board_wrap,
            bg=CARD,
            highlightbackground=WIN,
            highlightthickness=2,
            padx=28,
            pady=22,
        )
        self.result_title = tk.Label(
            self.result_panel,
            text="",
            font=("Helvetica Neue", 22, "bold"),
            fg=TEXT,
            bg=CARD,
        )
        self.result_title.pack()
        self.result_detail = tk.Label(
            self.result_panel,
            text="Scores are saved. Play another round, or close the window when you're done.",
            font=("Helvetica Neue", 12),
            fg=MUTED,
            bg=CARD,
            wraplength=320,
            justify="center",
        )
        self.result_detail.pack(pady=(6, 14))
        self._button(self.result_panel, "Play again", self._reset_board, primary=True).pack()

        actions = tk.Frame(self, bg=BG)
        actions.pack(pady=(16, 8))
        self._button(actions, "Play again", self._reset_board, primary=True).pack(side="left", padx=6)
        self._button(actions, "Change names", self._ask_names).pack(side="left", padx=6)
        self._button(actions, "Reset these scores", self._reset_scores).pack(side="left", padx=6)

    def _button(self, parent, text, command, primary=False):
        bg = BTN if primary else GHOST
        btn = tk.Label(
            parent,
            text=text,
            font=("Helvetica Neue", 13, "bold"),
            fg=TEXT,
            bg=bg,
            padx=16,
            pady=10,
            cursor="hand2",
        )
        hover = BTN_HOVER if primary else CARD

        def enter(_e):
            btn.configure(bg=hover)

        def leave(_e):
            btn.configure(bg=bg)

        btn.bind("<Enter>", enter)
        btn.bind("<Leave>", leave)
        btn.bind("<Button-1>", lambda _e: command())
        return btn

    def _cell_size(self):
        return 560 / 3

    def _cell_at(self, x, y):
        size = self._cell_size()
        col, row = int(x // size), int(y // size)
        if 0 <= col < 3 and 0 <= row < 3:
            return row * 3 + col
        return None

    def _set_hover(self, cell):
        if cell == self.hover_cell:
            return
        self.hover_cell = cell
        self._draw_board()

    def _on_motion(self, event):
        cell = self._cell_at(event.x, event.y)
        if cell is None or self.board[cell] or self.game_over:
            cell = None
        self._set_hover(cell)

    def _on_click(self, event):
        if self.game_over:
            return
        cell = self._cell_at(event.x, event.y)
        if cell is None or self.board[cell]:
            return
        self.board[cell] = self.marks[self.turn]
        winner = self._winner()
        if winner:
            self.game_over = True
            self.winning_line = winner
            self._apply_result("win")
        elif all(self.board):
            self.game_over = True
            self._apply_result("draw")
        else:
            self.turn = 1 - self.turn
            self._refresh_status()
        self.hover_cell = None
        self._draw_board()

    def _winner(self):
        lines = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        )
        for line in lines:
            a, b, c = (self.board[i] for i in line)
            if a and a == b == c:
                return line
        return None

    def _apply_result(self, kind):
        left, right = self.names
        if kind == "draw":
            record_for(self.scores, left)["draws"] += 1
            record_for(self.scores, right)["draws"] += 1
            self.status.configure(
                text="It's a draw",
                fg=WIN,
            )
        else:
            winner = self.turn
            loser = 1 - self.turn
            record_for(self.scores, self.names[winner])["wins"] += 1
            record_for(self.scores, self.names[loser])["losses"] += 1
            self.status.configure(
                text=f"{self.names[winner]} wins",
                fg=self.colors[winner],
            )
        save_scores(self.scores)
        self._refresh_cards()
        self._show_replay()

    def _refresh_status(self):
        if not self.game_over:
            name = self.names[self.turn]
            self.status.configure(
                text=f"{name}'s turn   ·   {self.marks[self.turn]}",
                fg=self.colors[self.turn],
            )
        for index, card in enumerate(self.card_frames):
            active = (not self.game_over and index == self.turn) or (
                self.game_over and self.winning_line and index == self.turn
            )
            card.configure(
                highlightbackground=self.colors[index] if active else CARD_EDGE,
                highlightthickness=2 if active else 1,
            )

    def _refresh_cards(self):
        for index, name in enumerate(self.names):
            stats = record_for(self.scores, name)
            self.name_labels[index].configure(text=name)
            self.score_labels[index].configure(
                text=f"{stats['wins']} wins   ·   {stats['losses']} losses   ·   {stats['draws']} draws"
            )
        self._refresh_status()

    def _show_replay(self):
        if self.winning_line:
            self.result_title.configure(
                text=f"{self.names[self.turn]} wins",
                fg=self.colors[self.turn],
            )
        else:
            self.result_title.configure(text="It's a draw", fg=WIN)
        self.result_panel.place(relx=0.5, rely=0.5, anchor="center")
        self.result_panel.lift()

    def _reset_board(self):
        self.result_panel.place_forget()
        self.board = [""] * 9
        self.turn = 0
        self.game_over = False
        self.winning_line = []
        self.hover_cell = None
        self._refresh_status()
        self._draw_board()

    def _reset_scores(self):
        for name in self.names:
            self.scores[name] = {"wins": 0, "losses": 0, "draws": 0}
        save_scores(self.scores)
        self._refresh_cards()

    def _ask_names(self):
        dialog = tk.Toplevel(self)
        dialog.title("Players")
        dialog.configure(bg=BG)
        dialog.resizable(False, False)
        dialog.transient(self)
        dialog.grab_set()

        tk.Label(
            dialog,
            text="Who's playing?",
            font=("Helvetica Neue", 20, "bold"),
            fg=TEXT,
            bg=BG,
        ).pack(anchor="w", padx=28, pady=(24, 4))
        tk.Label(
            dialog,
            text="Names are used to keep each player's score.",
            font=("Helvetica Neue", 12),
            fg=MUTED,
            bg=BG,
        ).pack(anchor="w", padx=28, pady=(0, 16))

        entries = []
        for index, label in enumerate(("Player X", "Player O")):
            tk.Label(
                dialog,
                text=label,
                font=("Helvetica Neue", 11, "bold"),
                fg=self.colors[index],
                bg=BG,
            ).pack(anchor="w", padx=28)
            entry = tk.Entry(
                dialog,
                font=("Helvetica Neue", 14),
                bg=CARD,
                fg=TEXT,
                insertbackground=TEXT,
                relief="flat",
                highlightthickness=1,
                highlightbackground=CARD_EDGE,
                highlightcolor=self.colors[index],
            )
            entry.insert(0, self.names[index] if not self.names[index].startswith("Player ") else "")
            entry.pack(fill="x", padx=28, pady=(4, 14), ipady=8)
            entries.append(entry)

        def confirm(_event=None):
            first = entries[0].get().strip() or "Player 1"
            second = entries[1].get().strip() or "Player 2"
            if first.lower() == second.lower():
                second = f"{second} (O)"
            self.names = [first, second]
            record_for(self.scores, first)
            record_for(self.scores, second)
            save_scores(self.scores)
            self._refresh_cards()
            self._reset_board()
            dialog.destroy()

        go = tk.Label(
            dialog,
            text="Start game",
            font=("Helvetica Neue", 13, "bold"),
            fg=TEXT,
            bg=BTN,
            padx=18,
            pady=10,
            cursor="hand2",
        )
        go.pack(pady=(4, 24))
        go.bind("<Button-1>", confirm)
        go.bind("<Enter>", lambda _e: go.configure(bg=BTN_HOVER))
        go.bind("<Leave>", lambda _e: go.configure(bg=BTN))
        entries[0].focus_set()
        dialog.bind("<Return>", confirm)
        dialog.protocol("WM_DELETE_WINDOW", dialog.destroy)

        dialog.update_idletasks()
        w, h = dialog.winfo_width(), dialog.winfo_height()
        x = self.winfo_rootx() + (self.winfo_width() - w) // 2
        y = self.winfo_rooty() + (self.winfo_height() - h) // 2
        dialog.geometry(f"{max(w, 380)}x{h}+{x}+{y}")

    def _draw_board(self):
        canvas = self.canvas
        canvas.delete("all")
        size = self._cell_size()
        pad = 18

        for index in range(9):
            row, col = divmod(index, 3)
            x0, y0 = col * size, row * size
            x1, y1 = x0 + size, y0 + size
            winning = index in self.winning_line
            hovered = index == self.hover_cell
            fill = "#3a2f14" if winning else (HOVER if hovered else BG_RAISED)
            canvas.create_rectangle(x0 + 8, y0 + 8, x1 - 8, y1 - 8, fill=fill, outline="", width=0)

            mark = self.board[index]
            cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
            color = WIN if winning else (X_COLOR if mark == "X" else O_COLOR)
            if mark == "X":
                arm = size * 0.26
                canvas.create_line(cx - arm, cy - arm, cx + arm, cy + arm, fill=color, width=10, capstyle="round")
                canvas.create_line(cx + arm, cy - arm, cx - arm, cy + arm, fill=color, width=10, capstyle="round")
            elif mark == "O":
                radius = size * 0.26
                canvas.create_oval(
                    cx - radius,
                    cy - radius,
                    cx + radius,
                    cy + radius,
                    outline=color,
                    width=10,
                )

        for i in (1, 2):
            pos = i * size
            canvas.create_line(pos, pad, pos, 560 - pad, fill=LINE, width=4, capstyle="round")
            canvas.create_line(pad, pos, 560 - pad, pos, fill=LINE, width=4, capstyle="round")


if __name__ == "__main__":
    TicTacToe().mainloop()
