#!/usr/bin/env python3
"""Sabotage the Prophecy: an AI-generated offline Tkinter puzzle game."""

TITLE = 'Sabotage the Prophecy'
EYEBROW = 'THE ARCHIVE OF UNWRITTEN ENDS  /  FATE REVISION DESK'
TAGLINE = 'The words are inevitable. Their meaning is negotiable.'
BG = '#1b1420'
PANEL = '#281f2c'
CARD = '#3a2c3e'
INK = '#f5ecdf'
MUTED = '#c4adbf'
ACCENT = '#efbf7e'
UNIT = 'VERSE'
STYLE = 'prophecy'
PANEL_LABEL = '01 / THE SEALED VERSE'
EVIDENCE_LABEL = '02 / FIND THE LOOPHOLE'
DECISION_LABEL = '03 / REWRITE THE OUTCOME'
SUBMIT = 'Set fate in motion →'
NEXT = 'Unseal next verse →'
SUCCESS = 'Fate outwitted'
FAILURE = 'Fate finds its price'
GUIDE = 'Inspect the glossary, scene, and constraints. Choose all three parts of a plan. Every word of the verse must remain true while everyone stays safe. Only meanings explicitly permitted in the records count. A complete correct plan earns 100 points. Five verses, no timer.'

CASES = [{'name': 'The fall of the Crown',
  'subtitle': 'VERSE I • THE OBSIDIAN COURT',
  'tag': 'FATE / SUNSET',
  'intro': '“At sunset, the Crown shall fall before the gathered court.”',
  'brief': 'Fulfill the exact words while keeping the ruler alive and the kingdom intact. Only sanctioned '
           'meanings count.',
  'evidence': [('Read the royal glossary',
                '“The Crown” may mean the reigning monarch or the ceremonial headpiece. A replica is never '
                'called the Crown.'),
               ('Survey the court',
                'Both the throne room and public courtyard can hold the gathered court. An empty room '
                'cannot.'),
               ('Check the constraints',
                'The monarch must survive and the headpiece must stay undamaged. A tower drop shatters it. '
                'Lowering it onto a cushion counts as a fall; storing it without movement does not.')],
  'slots': [('THE CROWN', ['The reigning monarch', 'The real ceremonial headpiece', 'A painted replica']),
            ('SHALL FALL',
             ['Push from the high tower', 'Lower onto a velvet cushion', 'Leave motionless in a vault']),
            ('BEFORE THE COURT',
             ['An empty throne room',
              'A private locked bedroom',
              'The public courtyard with the court assembled'])],
  'answer': [1, 1, 2],
  'explanation': 'The real crown falls gently onto a cushion in front of the assembled court at sunset. The '
                 'verse holds and the monarch survives.'},
 {'name': 'The silencing of the Bell',
  'subtitle': 'VERSE II • THE WINTER MONASTERY',
  'tag': 'FATE / MIDNIGHT',
  'intro': '“At midnight, the Bell shall lose its voice, and no hand shall strike it.”',
  'brief': 'Silence the monastery’s warning bell without breaking it, touching it by hand, or harming the '
           'bell keeper.',
  'evidence': [('Read the monastery register',
                'Capital-B Bell is the bronze warning bell. The bell keeper, Bella, is not a recognized '
                'meaning.'),
               ('Inspect the mechanism',
                'A clockwork release can pull the clapper clear at midnight. Foam only muffles the sound; it '
                'does not silence it.'),
               ('Read the preservation oath',
                'Cracking the bronze is forbidden. The bell must remain whole, and the action must occur at '
                'midnight.')],
  'slots': [('THE BELL', ['Bella the keeper', 'The bronze warning bell', 'A drawing of the bell']),
            ('LOSE ITS VOICE',
             ['Crack the bronze', 'Wrap the tower in foam', 'Withdraw the clapper by clockwork']),
            ('THE MOMENT', ['At midnight', 'At noon', 'After the morning service'])],
  'answer': [1, 2, 0],
  'explanation': 'Clockwork withdraws the intact bell’s clapper exactly at midnight. The bell cannot sound, '
                 'no hand strikes it, and nothing is damaged.'},
 {'name': 'The devouring Wolf',
  'subtitle': 'VERSE III • THE NORTHERN ROAD',
  'tag': 'FATE / BEFORE DAWN',
  'intro': '“Before dawn, the Wolf shall devour the last heir.”',
  'brief': 'Preserve the living heir. The village permits symbolic stand-ins only where the registry '
           'explicitly authorizes them.',
  'evidence': [('Read the village registry',
                'The Wolf is either the wild animal or the tavern furnace named Wolf. A costume does not '
                'qualify.'),
               ('Inspect the heir charter',
                'A wax effigy bearing the heir’s official signet is a legally recognized stand-in. A plain '
                'doll is not.'),
               ('Inspect the furnace',
                'The Wolf furnace burns wax completely. Feeding anything to the wild animal risks the heir’s '
                'life and violates your protection oath.')],
  'slots': [('THE WOLF', ['The tavern furnace named Wolf', 'The wild wolf', 'A dancer in a wolf costume']),
            ('THE LAST HEIR', ['The living heir', 'A plain wooden doll', 'The signet-bearing wax effigy']),
            ('THE ACT', ['Display beside the furnace', 'Burn completely before dawn', 'Burn after sunrise'])],
  'answer': [0, 2, 1],
  'explanation': 'Before dawn, the furnace named Wolf consumes the officially recognized wax heir. The '
                 'living heir remains safe and the words are satisfied.'},
 {'name': 'The breaking of the Line',
  'subtitle': 'VERSE IV • THE SALT HARBOR',
  'tag': 'FATE / HIGH TIDE',
  'intro': '“At high tide, the royal Line shall break upon the shore.”',
  'brief': 'Keep the dynasty and its ship safe while fulfilling the harbor’s recorded meanings.',
  'evidence': [('Read the harbor glossary',
                '“Royal Line” may mean the dynasty or the blue ceremonial rope bearing the royal seal. '
                'Ordinary fishing line does not count.'),
               ('Read the safety report',
                'The sealed rope is decorative and carries no load. Cutting the mooring rope would endanger '
                'the royal ship.'),
               ('Consult the tide table',
                'High tide is at 06:40. The sandy beach is the shore; the offshore jetty is excluded by the '
                'harbor charter.')],
  'slots': [('THE ROYAL LINE', ['The dynasty', 'An ordinary fishing line', 'The sealed ceremonial rope']),
            ('SHALL BREAK',
             ['Cut the decorative rope', 'Cut the ship’s loaded mooring', 'Leave everything intact']),
            ('WHERE AND WHEN',
             ['On the jetty at 06:40', 'On the beach at high tide, 06:40', 'On the beach at low tide'])],
  'answer': [2, 0, 1],
  'explanation': 'The ceremonial royal Line breaks on the sandy shore at high tide. The dynasty remains '
                 'intact and the ship’s actual mooring is untouched.'},
 {'name': 'The death of Hope',
  'subtitle': 'VERSE V • THE FINAL VIGIL',
  'tag': 'FATE / FIRST LIGHT',
  'intro': '“With first light, Hope must die, and the city shall awaken.”',
  'brief': 'Finish the last verse without killing anyone or extinguishing the city’s real hope.',
  'evidence': [('Read the city naming book',
                'Hope is the old night-watch beacon’s official name. A child also bears that name, but no '
                'painted word or replica qualifies.'),
               ('Inspect the beacon',
                'Its flame can be extinguished safely using the timed snuffer. Smashing the tower would hurt '
                'the watch staff.'),
               ('Read the dawn protocol',
                'First light triggers both the beacon snuffer and the public waking chimes. Silencing the '
                'chimes leaves the city asleep.')],
  'slots': [('HOPE', ['The child named Hope', 'The old night-watch beacon', 'The word painted on a wall']),
            ('MUST DIE',
             ['Shatter the occupied tower',
              'Keep the flame burning',
              'Extinguish the beacon with the timed snuffer']),
            ('THE CITY SHALL AWAKEN',
             ['Sound the waking chimes at first light',
              'Silence the chimes',
              'Sound the chimes at midnight'])],
  'answer': [1, 2, 0],
  'explanation': 'At first light, the beacon Hope goes dark while the waking chimes ring. The prophecy '
                 'finishes without a death. Fate kept its wording; you kept your city.'}]

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
