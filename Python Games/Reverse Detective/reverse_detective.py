#!/usr/bin/env python3
"""Reverse Detective: an AI-generated, offline Tkinter deduction game."""

import random
import tkinter as tk
from dataclasses import dataclass, field

BG, PANEL, CARD = "#10151b", "#171e26", "#202a35"
INK, MUTED, GOLD, RED, GREEN = "#eee9dd", "#9aa8b6", "#e5b86b", "#ed8580", "#83c9b1"


@dataclass(frozen=True)
class Suspect:
    name: str
    role: str
    initials: str
    location: str
    motive: str
    detail: str


SUSPECTS = (
    Suspect("Clara Voss", "THE BOTANIST", "CV", "Conservatory", "An inheritance denied", "Her green coat was seen near the glasshouse. She never entered the study."),
    Suspect("Felix Ward", "THE CLOCKMAKER", "FW", "Workshop", "A debt called in", "He worked alone until midnight. His tools leave distinctive triangular marks."),
    Suspect("Mara Vale", "THE PIANIST", "MV", "Ballroom", "A stolen composition", "Six guests heard her play from 10:00 to 10:30. She wears violet perfume."),
)
LOCATIONS = ("Study", "Conservatory", "Workshop", "Ballroom")


@dataclass(frozen=True)
class Evidence:
    title: str
    kind: str
    text: str
    strength: int
    location: str = "Study"
    person: int = -1
    conflicts: str = ""


EVIDENCE = (
    Evidence("A monogrammed glove", "PHYSICAL", "A personal belonging at the scene. Quietly persuasive.", 22),
    Evidence("An unsigned threat", "MOTIVE", "A bitter letter demanding that the victim settle an old score.", 17),
    Evidence("A witness in the fog", "TESTIMONY", "A passerby claims to have seen your target enter the study at 10:15.", 27, conflicts="alibi"),
    Evidence("Green wool fibers", "PHYSICAL", "Fibers matching Clara's coat, caught on the study's broken latch.", 26, person=0),
    Evidence("Triangular tool marks", "PHYSICAL", "Fresh marks on the lock match Felix's specialist tools.", 26, person=1),
    Evidence("Violet perfume", "PHYSICAL", "Mara's unmistakable perfume lingers beside the victim's desk.", 26, person=2),
    Evidence("A trail of muddy steps", "TIMELINE", "Footprints imply the suspect left their usual location for the study.", 21, conflicts="trail"),
    Evidence("A missing ledger page", "MOTIVE", "A torn account suggests the suspect stood to gain from the death.", 19),
)


@dataclass
class Case:
    culprit: int = 0
    target: int = 1
    planted: list = field(default_factory=list)
    budget: int = 4

    def audit(self):
        problems = []
        for index, location in self.planted:
            clue = EVIDENCE[index]
            if location != clue.location:
                problems.append(f"{clue.title}: the crime scene is the Study, not the {location}.")
            if clue.person >= 0 and clue.person != self.target:
                problems.append(f"{clue.title}: points to {SUSPECTS[clue.person].name}, not your target.")
            if clue.conflicts == "alibi" and self.target == 2:
                problems.append("The witness contradicts Mara's six-person ballroom alibi.")
            if clue.conflicts == "trail" and self.target == 2:
                problems.append("Mara could not leave a trail: she was performing throughout the murder.")
        return problems

    def suspicion(self):
        scores = [12, 12, 12]
        scores[self.culprit] = 38
        for index, location in self.planted:
            clue = EVIDENCE[index]
            person = self.target if clue.person < 0 else clue.person
            scores[person] += clue.strength if location == clue.location else 3
        scores[self.target] = max(0, scores[self.target] - 24 * len(self.audit()))
        return scores

    def plant(self, index, location):
        if len(self.planted) >= self.budget or any(i == index for i, _ in self.planted):
            return False
        self.planted.append((index, location))
        return True

    def verdict(self):
        scores = self.suspicion()
        winner = max(range(3), key=lambda i: scores[i])
        won = (self.target != self.culprit and winner == self.target
               and scores.count(scores[winner]) == 1 and not self.audit()
               and len(self.planted) >= 3)
        return won, winner


class ReverseDetective(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reverse Detective • The Glasshouse Murder")
        self.geometry("1180x840")
        self.minsize(980, 720)
        self.configure(bg=BG)
        self.selected = 0
        self.location = tk.StringVar(value="Study")
        self.finished = False
        self.new_case()

    def label(self, parent, text, size=11, color=INK, bold=False, **kwargs):
        return tk.Label(parent, text=text, bg=parent.cget("bg"), fg=color,
                        font=("Helvetica", size, "bold" if bold else "normal"), **kwargs)

    def button(self, parent, text, command, accent=False):
        button = tk.Button(parent, text=text, command=command, bg=GOLD if accent else CARD,
                           fg=BG if accent else INK, activebackground=GREEN,
                           activeforeground=BG, relief="flat", bd=0, padx=14, pady=9,
                           highlightthickness=0, font=("Helvetica", 11, "bold"), cursor="hand2")
        return button

    def new_case(self):
        culprit = random.randrange(3)
        self.case = Case(culprit, (culprit + 1) % 3)
        self.finished = False
        self.selected = 0
        self.render()

    def render(self):
        for child in self.winfo_children():
            child.destroy()
        header = tk.Frame(self, bg=BG, padx=26, pady=18)
        header.pack(fill="x")
        self.label(header, "R / D     •     BLACKTHORN ARCHIVES", 10, GOLD, True).pack(anchor="w")
        self.button(header, "New case ↗", self.new_case).pack(side="right")
        self.label(header, "Reverse Detective", 29, INK, True).pack(anchor="w", pady=(7, 0))
        self.label(header, "Everyone wants the truth. You need a better story.", 12, MUTED).pack(anchor="w", pady=(3, 0))

        briefing = tk.Frame(self, bg=PANEL, padx=18, pady=12)
        briefing.pack(fill="x", padx=26, pady=(0, 14))
        self.label(briefing, "CASE 001  /  THE GLASSHOUSE MURDER", 11, GOLD, True).pack(anchor="w")
        self.label(briefing, "Lord Ashford was killed in his study at 10:15 PM. The town votes at dawn.", 12).pack(anchor="w", pady=4)
        self.label(briefing, f"CONFIDENTIAL  •  {SUSPECTS[self.case.culprit].name} did it. Frame someone else with 3–4 consistent clues.", 11, GREEN).pack(anchor="w")

        body = tk.Frame(self, bg=BG)
        body.pack(fill="both", expand=True, padx=26)
        body.columnconfigure(0, weight=3, uniform="body")
        body.columnconfigure(1, weight=4, uniform="body")
        body.columnconfigure(2, weight=3, uniform="body")
        body.rowconfigure(0, weight=1)
        left = tk.Frame(body, bg=PANEL, padx=14, pady=14)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        self.label(left, "01 / CHOOSE YOUR FALL GUY", 10, GOLD, True).pack(anchor="w", pady=(0, 8))
        for i, suspect in enumerate(SUSPECTS):
            card = tk.Frame(left, bg=CARD, padx=12, pady=10, highlightthickness=1,
                            highlightbackground=GOLD if i == self.case.target else CARD)
            card.pack(fill="x", pady=5)
            self.label(card, suspect.role, 9, MUTED, True).pack(anchor="w")
            self.label(card, suspect.name + ("  •  GUILTY" if i == self.case.culprit else ""), 14, INK, True).pack(anchor="w", pady=4)
            self.label(card, suspect.motive, 10, GOLD).pack(anchor="w")
            self.label(card, suspect.detail, 10, MUTED, wraplength=230, justify="left").pack(anchor="w", pady=6)
            if i != self.case.culprit:
                self.button(card, "✓ Framing" if i == self.case.target else "Choose suspect", lambda n=i: self.choose(n)).pack(fill="x")

        middle = tk.Frame(body, bg=PANEL, padx=14, pady=14)
        middle.grid(row=0, column=1, sticky="nsew", padx=(0, 10))
        self.label(middle, "02 / PLANT YOUR EVIDENCE", 10, GOLD, True).pack(anchor="w")
        self.label(middle, "Select a card, then choose where to leave it.", 10, MUTED).pack(anchor="w", pady=(5, 10))
        grid = tk.Frame(middle, bg=PANEL)
        grid.pack(fill="x")
        for col in range(2):
            grid.columnconfigure(col, weight=1, uniform="clue")
        for i, clue in enumerate(EVIDENCE):
            used = any(index == i for index, _ in self.case.planted)
            card = tk.Frame(grid, bg=CARD, highlightthickness=1,
                            highlightbackground=GOLD if self.selected == i else CARD, padx=8, pady=7)
            card.grid(row=i // 2, column=i % 2, sticky="nsew", padx=3, pady=3)
            self.label(card, clue.kind + ("  ✓" if used else ""), 8, GREEN if used else MUTED).pack(anchor="w")
            btn = self.button(card, clue.title, lambda n=i: self.select(n))
            btn.configure(font=("Helvetica", 10, "bold"), padx=0, pady=7, wraplength=150)
            btn.pack(fill="x")
        clue = EVIDENCE[self.selected]
        self.label(middle, clue.text, 11, INK, wraplength=340, justify="left").pack(anchor="w", pady=12)
        location_row = tk.Frame(middle, bg=PANEL)
        location_row.pack(fill="x")
        self.label(location_row, "LEAVE IN", 9, MUTED, True).pack(side="left")
        menu = tk.OptionMenu(location_row, self.location, *LOCATIONS)
        menu.configure(bg=CARD, fg=INK, highlightthickness=0, relief="flat")
        menu.pack(side="right")
        self.button(middle, "＋ Plant evidence", self.plant, True).pack(fill="x", pady=10)

        right = tk.Frame(body, bg=PANEL, padx=14, pady=14)
        right.grid(row=0, column=2, sticky="nsew")
        self.label(right, "03 / THE TOWN'S WHISPERS", 10, GOLD, True).pack(anchor="w")
        scores = self.case.suspicion()
        for i, suspect in enumerate(SUSPECTS):
            self.label(right, f"{suspect.name}    {scores[i]}", 11, INK, True).pack(anchor="w", pady=(13, 4))
            bar = tk.Canvas(right, height=5, bg=CARD, highlightthickness=0)
            bar.pack(fill="x")
            bar.create_rectangle(0, 0, min(240, scores[i] * 2), 6, fill=GOLD if i == self.case.target else MUTED, outline="")
        self.label(right, f"CASEBOARD  /  {len(self.case.planted)} OF 4 CLUES", 10, GOLD, True).pack(anchor="w", pady=(20, 5))
        if not self.case.planted:
            self.label(right, "No evidence planted yet.", 10, MUTED).pack(anchor="w", pady=5)
        for position, (index, location) in enumerate(self.case.planted):
            self.button(right, f"× {EVIDENCE[index].title}\n   {location}", lambda n=position: self.remove(n)).pack(fill="x", pady=2)
        problems = self.case.audit()
        self.label(right, "CONTRADICTION AUDIT", 10, GOLD, True).pack(anchor="w", pady=(16, 5))
        self.label(right, "\n".join(problems) if problems else "✓ Your story holds together.", 10,
                   RED if problems else GREEN, wraplength=230, justify="left").pack(anchor="w")

        footer = tk.Frame(self, bg=BG, padx=26, pady=14)
        footer.pack(fill="x")
        self.label(footer, "Remove clues with ×. Changing your target clears the board.", 10, MUTED).pack(side="left")
        self.button(footer, "Call the town vote →", self.vote, True).pack(side="right")

    def select(self, index):
        self.selected = index
        self.render()

    def choose(self, index):
        if self.finished or index == self.case.target:
            return
        self.case.target = index
        self.case.planted.clear()
        self.render()

    def plant(self):
        if not self.finished:
            self.case.plant(self.selected, self.location.get())
            self.render()

    def remove(self, index):
        if not self.finished:
            self.case.planted.pop(index)
            self.render()

    def vote(self):
        if self.finished:
            return
        self.finished = True
        won, winner = self.case.verdict()
        popup = tk.Toplevel(self)
        popup.title("The verdict")
        popup.configure(bg=PANEL, padx=30, pady=30)
        popup.transient(self)
        popup.grab_set()
        self.label(popup, "DAWN BREAKS IN BLACKTHORN", 10, GOLD, True).pack(pady=(0, 15))
        self.label(popup, "A perfect deception." if won else "Your story unravels.", 25, GREEN if won else RED, True).pack()
        reason = (f"The town blames {SUSPECTS[winner].name}.\nThe real killer walks free."
                  if won else "The investigator rejects your case." if self.case.audit() or len(self.case.planted) < 3
                  else f"The town is unconvinced by your chosen target.\n{SUSPECTS[winner].name} draws the most suspicion.")
        self.label(popup, reason, 13, INK, wraplength=460, justify="center").pack(pady=18)
        self.label(popup, "A winning case needs 3+ clues, a clear suspicion lead,\nand zero contradictions against an innocent suspect.", 11, MUTED).pack()
        self.button(popup, "Play another case", lambda: (popup.destroy(), self.new_case()), True).pack(fill="x", pady=(22, 0))


if __name__ == "__main__":
    ReverseDetective().mainloop()
