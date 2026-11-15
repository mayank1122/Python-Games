#!/usr/bin/env python3
"""Dream Customs: an AI-generated offline Tkinter puzzle game."""

TITLE = 'Dream Customs'
EYEBROW = 'MINISTRY OF WAKING AFFAIRS  /  BORDER POST 03'
TAGLINE = 'Some things should stay on the other side of sleep.'
BG = '#121629'
PANEL = '#1b2239'
CARD = '#2b3452'
INK = '#f4ebdf'
MUTED = '#aab4d4'
ACCENT = '#c6b1ff'
UNIT = 'ARRIVAL'
STYLE = 'customs'
PANEL_LABEL = '01 / TRAVELER DOSSIER'
EVIDENCE_LABEL = '02 / INSPECT THE IMPOSSIBLE'
DECISION_LABEL = '03 / STAMP THE MANIFEST'
SUBMIT = 'Issue border ruling →'
NEXT = 'Call next traveler →'
SUCCESS = 'Charter upheld'
FAILURE = 'Border violation'
GUIDE = 'Apply these rules in order:\n\n1. RETURN objects containing another person’s identity-linked memories or rewriting waking reality.\n\n2. Otherwise QUARANTINE growing objects or anything lacking an intact waking seal.\n\n3. ADMIT everything else.\n\nEach correct ruling earns 100 points. Five arrivals, no timer.'

CASES = [{'name': 'A jar of borrowed sunrise',
  'subtitle': 'TRAVELER: THE NIGHT GARDENER',
  'tag': 'ARRIVAL / GATE 03',
  'intro': '“Just a little daylight for my tomatoes. They have been very patient.”',
  'brief': 'Classify the jar under the border charter. Objects may be admitted, quarantined, or returned to '
           'the dream.',
  'evidence': [('Read the declaration',
                'Declared: captured daylight. Purpose: greenhouse illumination. No live creatures or '
                'memories.'),
               ('Run the waking-world scanner',
                'Stable light output. No growth, duplication, or changes to surrounding objects.'),
               ('Open the seal registry',
                'Container has a valid waking seal. The seal stays intact during testing.')],
  'slots': [('Border decision',
             ['ADMIT • release into reality',
              'QUARANTINE • contain for review',
              'RETURN • send back to the dream'])],
  'answer': [0],
  'explanation': 'The sunrise is stable and properly sealed. It neither contains a person nor grows or '
                 'rewrites reality, so it is admitted.'},
 {'name': 'The pocket thunderstorm',
  'subtitle': 'TRAVELER: A VERY WET ACCOUNTANT',
  'tag': 'ARRIVAL / PRESSURE WARNING',
  'intro': '“It is a comfort cloud. It helps me sleep through tax season.”',
  'brief': 'A suitcase rumbles from within. Evaluate the storm, not the traveler’s excellent umbrella.',
  'evidence': [('Read the declaration',
                'Declared: miniature weather. The traveler reports that it doubles in size whenever it hears '
                'its own thunder.'),
               ('Run the containment scan',
                'No people, memories, or reality rewriting. Growth is active, but the case currently '
                'contains it.'),
               ('Check the waking seal',
                'The certified seal is intact. It can hold the current storm while specialists '
                'investigate.')],
  'slots': [('Border decision',
             ['ADMIT • release into reality',
              'QUARANTINE • contain for review',
              'RETURN • send back to the dream'])],
  'answer': [1],
  'explanation': 'Self-growing objects require quarantine while safely contained. The intact seal permits '
                 'holding the storm; it cannot be released into reality.'},
 {'name': 'A bottle of somebody’s childhood',
  'subtitle': 'TRAVELER: THE MEMORY MERCHANT',
  'tag': 'ARRIVAL / IDENTITY ALERT',
  'intro': '“Pre-owned happiness. Excellent condition. No refunds after remembering.”',
  'brief': 'A bottle contains a summer afternoon. Determine whether it is a souvenir or a person’s protected '
           'memory.',
  'evidence': [('Read the provenance',
                'The memory belongs to a living stranger. The merchant bought it from a dream market without '
                'consent.'),
               ('Listen through the glass',
                'A child’s voice gives a real name and home address. The memory is identity-linked.'),
               ('Check the waking seal',
                'Valid and intact. A seal does not override the identity protection rule.')],
  'slots': [('Border decision',
             ['ADMIT • release into reality',
              'QUARANTINE • contain for review',
              'RETURN • send back to the dream'])],
  'answer': [2],
  'explanation': 'Another person’s identity-linked memories cannot cross. Identity protection takes priority '
                 'over an intact seal, so return the bottle.'},
 {'name': 'The unfinished paper fox',
  'subtitle': 'TRAVELER: A SLEEPWALKING CARTOGRAPHER',
  'tag': 'ARRIVAL / UNSEALED MOVEMENT',
  'intro': '“I folded him myself. He only bites imaginary fingers.”',
  'brief': 'An animated origami fox scratches at a paper box. Apply the charter in order.',
  'evidence': [('Observe the fox',
                'It stays the same size, repeats three harmless motions, and does not copy itself.'),
               ('Check identity and reality effects',
                'No human identity, borrowed memories, or changes to reality detected.'),
               ('Inspect the box',
                'The waking seal is absent. A secure quarantine cabinet is available at this gate.')],
  'slots': [('Border decision',
             ['ADMIT • release into reality',
              'QUARANTINE • contain for review',
              'RETURN • send back to the dream'])],
  'answer': [1],
  'explanation': 'The fox triggers no return rule, but it lacks a waking seal. It must be quarantined for '
                 'safe certification before any admission.'},
 {'name': 'The key to yesterday',
  'subtitle': 'TRAVELER: AN APOLOGETIC HISTORIAN',
  'tag': 'ARRIVAL / CAUSALITY BREACH',
  'intro': '“One small correction. Nobody would even notice the empire.”',
  'brief': 'The key promises to repair the traveler’s greatest mistake. Decide before it finds a lock.',
  'evidence': [('Read the label',
                'Opens any door onto the previous day. Changes made there persist in the present.'),
               ('Run a controlled simulation',
                'A removed coin disappears from the present-day inventory. Recorded history changes to '
                'match.'),
               ('Check the seal and growth',
                'The key is stable and sealed. Neither condition prevents its reality-rewriting effect.')],
  'slots': [('Border decision',
             ['ADMIT • release into reality',
              'QUARANTINE • contain for review',
              'RETURN • send back to the dream'])],
  'answer': [2],
  'explanation': 'Objects that rewrite waking reality must be returned, even when stable and sealed. The key '
                 'changes established events and cannot cross.'}]

# This code is AI-generated by OpenAI Codex. Review before reuse.
import tkinter as tk
from tkinter import messagebox
from dataclasses import dataclass, field


@dataclass
class Session:
    index: int = 0
    score: int = 0
    resolved: bool = False
    choices: dict = field(default_factory=dict)
    revealed: set = field(default_factory=set)
    history: list = field(default_factory=list)

    @property
    def case(self):
        return CASES[self.index]

    def choose(self, slot, value):
        if not self.resolved and 0 <= slot < len(self.case['slots']):
            if 0 <= value < len(self.case['slots'][slot][1]):
                self.choices[slot] = value

    def reveal(self, index):
        if not self.resolved and 0 <= index < len(self.case['evidence']):
            self.revealed.add(index)

    def submit(self):
        if self.resolved or len(self.choices) != len(self.case['slots']):
            return None
        correct = all(self.choices.get(i) == answer for i, answer in enumerate(self.case['answer']))
        self.score += 100 if correct else 0
        self.history.append(correct)
        self.resolved = True
        return correct

    def advance(self):
        if not self.resolved or self.index == len(CASES) - 1:
            return False
        self.index += 1
        self.resolved = False
        self.choices.clear()
        self.revealed.clear()
        return True


class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry('1240x880')
        self.minsize(1020, 720)
        self.configure(bg=BG)
        self.session = Session()
        self.bind('<Control-Return>', lambda e: self.submit())
        self.bind('<Command-Return>', lambda e: self.submit())
        self.render()

    def text(self, parent, content, size=11, color=None, bold=False, wrap=0):
        label = tk.Label(parent, text=content, bg=parent.cget('bg'), fg=color or INK,
                         font=('Helvetica', size, 'bold' if bold else 'normal'),
                         justify='left', anchor='w', wraplength=wrap)
        return label

    def button(self, parent, content, command, primary=False, selected=False):
        button = tk.Button(parent, text=content, command=command, relief='flat',
                           bg=ACCENT if primary or selected else CARD,
                           fg=BG if primary or selected else INK,
                           activebackground=ACCENT, activeforeground=BG,
                           font=('Helvetica', 11, 'bold'), cursor='hand2',
                           highlightthickness=0, bd=0, padx=12, pady=10,
                           anchor='w', wraplength=285, justify='left')
        return button

    def section(self, parent, title):
        frame = tk.Frame(parent, bg=PANEL, padx=16, pady=16)
        self.text(frame, title, 10, ACCENT, True).pack(fill='x', pady=(0, 12))
        return frame

    def render(self):
        scroll_y = self.scroll.yview()[0] if hasattr(self, 'scroll') else 0
        for widget in self.winfo_children():
            widget.destroy()
        s = self.session
        case = s.case
        header = tk.Frame(self, bg=BG, padx=28, pady=20)
        header.pack(fill='x')
        self.button(header, '↺  Restart shift', self.restart).pack(side='right')
        self.text(header, EYEBROW, 10, ACCENT, True).pack(anchor='w')
        self.text(header, TITLE, 29, bold=True).pack(anchor='w', pady=(6, 3))
        self.text(header, TAGLINE, 12, MUTED).pack(anchor='w')
        strip = tk.Frame(self, bg=PANEL, padx=20, pady=12)
        strip.pack(fill='x', padx=28, pady=(0, 14))
        self.text(strip, f"{UNIT} {s.index + 1:02d} / {len(CASES):02d}     •     {case['tag']}", 11, ACCENT, True).pack(side='left')
        self.text(strip, f'SHIFT SCORE  {s.score:03d}', 11, INK, True).pack(side='right')

        holder = tk.Frame(self, bg=BG)
        holder.pack(fill='both', expand=True, padx=28)
        self.scroll = tk.Canvas(holder, bg=BG, highlightthickness=0)
        bar = tk.Scrollbar(holder, command=self.scroll.yview)
        bar.pack(side='right', fill='y')
        self.scroll.configure(yscrollcommand=bar.set)
        self.scroll.pack(side='left', fill='both', expand=True)
        body = tk.Frame(self.scroll, bg=BG)
        window = self.scroll.create_window(0, 0, anchor='nw', window=body)
        body.bind('<Configure>', lambda event: self.scroll.configure(scrollregion=self.scroll.bbox('all')))
        self.scroll.bind('<Configure>', lambda event: self.scroll.itemconfigure(window, width=event.width))
        for col, weight in enumerate((3, 4, 4)):
            body.columnconfigure(col, weight=weight, uniform='panels')
        left = self.section(body, PANEL_LABEL)
        left.grid(row=0, column=0, sticky='nsew', padx=(0, 10))
        art = tk.Canvas(left, width=225, height=180, bg=PANEL, highlightthickness=0)
        art.pack(fill='x', pady=(0, 12))
        self.draw_art(art)
        self.text(left, case['name'], 19, bold=True, wrap=235).pack(fill='x')
        self.text(left, case['subtitle'], 10, ACCENT, True, 235).pack(fill='x', pady=(6, 15))
        self.text(left, case['intro'], 12, wrap=235).pack(fill='x')
        self.text(left, 'YOUR FIELD GUIDE', 10, ACCENT, True).pack(fill='x', pady=(22, 8))
        self.text(left, GUIDE, 11, MUTED, wrap=235).pack(fill='x')
        self.text(left, 'SHIFT RECORD', 10, ACCENT, True).pack(fill='x', pady=(22, 8))
        self.text(left, '   '.join('✓' if won else '×' for won in s.history) or 'Awaiting your first decision.', 12, MUTED, wrap=230).pack(fill='x')

        middle = self.section(body, EVIDENCE_LABEL)
        middle.grid(row=0, column=1, sticky='nsew', padx=(0, 10))
        self.text(middle, case['brief'], 13, wrap=310).pack(fill='x', pady=(0, 15))
        for i, (title, content) in enumerate(case['evidence']):
            opened = i in s.revealed
            self.button(middle, ('−  ' if opened else '+  ') + title, lambda n=i: self.reveal(n)).pack(fill='x', pady=(5, 0))
            if opened:
                self.text(middle, content, 11, MUTED, wrap=300).pack(fill='x', padx=8, pady=(6, 10))
        self.text(middle, 'Inspections are free. Read everything you need.\nDecisions lock when you submit.', 10, MUTED, wrap=300).pack(fill='x', pady=18)

        right = self.section(body, DECISION_LABEL)
        right.grid(row=0, column=2, sticky='nsew')
        for slot, (name, options) in enumerate(case['slots']):
            self.text(right, name, 10, MUTED, True).pack(fill='x', pady=(5, 5))
            for value, option in enumerate(options):
                self.button(right, ('●  ' if s.choices.get(slot) == value else '○  ') + option,
                            lambda a=slot, b=value: self.choose(a, b),
                            selected=s.choices.get(slot) == value).pack(fill='x', pady=3)
        if s.resolved:
            won = s.history[-1]
            self.text(right, '✓  ' + SUCCESS if won else '×  ' + FAILURE, 15, ACCENT if won else '#f29898', True, 300).pack(fill='x', pady=(18, 8))
            self.text(right, case['explanation'], 11, wrap=300).pack(fill='x', pady=5)
            if s.index < len(CASES) - 1:
                self.button(right, NEXT, self.advance, True).pack(fill='x', pady=14)
            else:
                self.text(right, f'SHIFT COMPLETE  •  {s.score}/{len(CASES) * 100}\n' + ('Perfect record.' if all(s.history) else 'Restart to try a different approach.'), 13, ACCENT, True, 300).pack(fill='x', pady=16)
                self.button(right, 'Start a new shift ↗', self.restart, True).pack(fill='x')
        else:
            ready = len(s.choices) == len(case['slots'])
            submit = self.button(right, SUBMIT if ready else 'Select every decision above', self.submit, True)
            submit.pack(fill='x', pady=18)
            if not ready:
                submit.configure(state='disabled', disabledforeground=MUTED)
        self.update_idletasks()
        self.scroll.yview_moveto(scroll_y)

    def draw_art(self, c):
        if STYLE == 'switchboard':
            c.create_rectangle(10, 12, 220, 165, fill=CARD, outline=ACCENT, width=2)
            for row in range(3):
                for col in range(6):
                    x, y = 30 + col * 34, 38 + row * 39
                    c.create_oval(x-6, y-6, x+6, y+6, fill=ACCENT if (row+col) % 3 == 0 else BG, outline=MUTED)
            c.create_line(30, 38, 30, 146, 164, 146, 164, 77, fill=ACCENT, width=4, smooth=True)
            c.create_text(114, 163, text='LINE 0' + str(self.session.index+1) + '   /   CONNECTED', fill=INK, font=('Helvetica', 9, 'bold'))
        elif STYLE == 'customs':
            c.create_oval(28, 5, 202, 179, outline=ACCENT, width=2)
            c.create_oval(38, 15, 192, 169, outline=MUTED, dash=(3, 5))
            c.create_rectangle(73, 63, 157, 123, fill=CARD, outline=ACCENT, width=3)
            c.create_arc(97, 45, 133, 81, start=0, extent=180, outline=ACCENT, width=3, style='arc')
            c.create_line(115, 75, 115, 110, fill=ACCENT, width=2)
            c.create_text(115, 146, text='DREAM / REALITY', fill=INK, font=('Helvetica', 10, 'bold'))
        else:
            c.create_oval(36, 9, 194, 167, outline=ACCENT, width=2)
            c.create_polygon(115, 20, 184, 140, 46, 140, outline=ACCENT, fill=CARD, width=2)
            c.create_oval(77, 74, 153, 116, outline=ACCENT, width=2)
            c.create_oval(107, 83, 123, 103, fill=ACCENT, outline='')
            c.create_text(115, 165, text='FATE IS A DRAFT', fill=INK, font=('Helvetica', 10, 'bold'))

    def reveal(self, index):
        self.session.reveal(index)
        self.render()

    def choose(self, slot, value):
        self.session.choose(slot, value)
        self.render()

    def submit(self):
        if self.session.submit() is not None:
            self.render()

    def advance(self):
        if self.session.advance():
            self.render()
            self.scroll.yview_moveto(0)

    def restart(self):
        if self.session.index or self.session.choices or self.session.history or self.session.revealed:
            if not messagebox.askyesno('Restart shift?', 'Clear this shift and start again?', parent=self):
                return
        self.session = Session()
        self.render()
        self.scroll.yview_moveto(0)


if __name__ == '__main__':
    Game().mainloop()
