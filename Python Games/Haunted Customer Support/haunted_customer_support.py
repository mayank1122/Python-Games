#!/usr/bin/env python3
"""Haunted Customer Support: an AI-generated offline Tkinter puzzle game."""

TITLE = 'Haunted Customer Support'
EYEBROW = 'AFTERLIFE SERVICES  /  NIGHT OPERATIONS'
TAGLINE = 'Every haunting is an unresolved ticket. Please stay on the line.'
BG = '#10171b'
PANEL = '#192328'
CARD = '#26343a'
INK = '#f1eadc'
MUTED = '#a6b9bb'
ACCENT = '#80d9bd'
UNIT = 'CALL'
STYLE = 'switchboard'
PANEL_LABEL = '01 / THE OTHER END'
EVIDENCE_LABEL = '02 / OPEN THE CASE FILE'
DECISION_LABEL = '03 / RESOLVE THE HAUNTING'
SUBMIT = 'Close the ticket →'
NEXT = 'Connect next caller →'
SUCCESS = 'Soul at rest'
FAILURE = 'Ticket unresolved'
GUIDE = 'Read the caller’s records. Select both the cause and the remedy. A correct pair earns 100 points. Wrong answers earn 0; every caller receives an explanation. Five callers, no timer.'

CASES = [{'name': 'Agnes Bell',
  'subtitle': 'RESIDENT • ROOM 404',
  'tag': 'INCOMING / STATIC ON LINE',
  'intro': '“I keep setting two cups. He never comes home. Your hold music is dreadful, by the way.”',
  'brief': 'A widow calls every night at 11:11. Find the unfinished promise and give her a way to keep it.',
  'evidence': [('Listen to the recording',
                'Agnes ignores questions about money. She asks whether Platform Nine still has its blue '
                'bench.'),
               ('Open the tenant record',
                'Agnes died in 1962. A train ticket for two remains in her coat; departure was 11:11 PM.'),
               ('Check undelivered mail',
                'Her husband wrote: “I reached the sea. I will wait where we planned to watch the sunrise.” '
                'The letter was never delivered.')],
  'slots': [('What binds her?',
             ['An unpaid household bill', 'A journey she thinks was abandoned', 'A stolen wedding ring']),
            ('Authorize a remedy',
             ['Deliver the letter and route her to the sunrise train',
              'Refund her rent',
              'Disconnect the line permanently'])],
  'answer': [1, 0],
  'explanation': 'Agnes was waiting on a promise, not a person in the house. The letter tells her the '
                 'journey can still be completed. She finally takes the train.'},
 {'name': 'Basil Finch',
  'subtitle': 'NIGHT BAKER • DECEASED',
  'tag': 'INCOMING / FLOUR IN RECEIVER',
  'intro': '“The oven is cold, the queue is long, and someone keeps calling my buns biscuits.”',
  'brief': 'A bakery is trapped in an endless opening morning. Identify the task Basil never finished.',
  'evidence': [('Taste the spectral pastry',
                'Perfect cinnamon. No burnt flour, poison, or evidence of sabotage.'),
               ('Read the order book',
                'Every order is crossed out except one: a loaf for the shelter. Payment: none.'),
               ('Check the delivery bell',
                'The shelter bell has been broken since the night Basil died. The loaf still waits at the '
                'bakery door.')],
  'slots': [('What binds him?',
             ['Fear his recipe was stolen', 'An undelivered act of kindness', 'A dangerous oven']),
            ('Authorize a remedy',
             ['Replace the recipe with a popular one',
              'Evacuate the bakery',
              'Repair the bell and deliver the shelter loaf'])],
  'answer': [1, 2],
  'explanation': 'Basil finished baking but never completed his last delivery. Fixing the bell lets the '
                 'shelter receive it, and the endless opening morning ends.'},
 {'name': 'Captain Orla Reed',
  'subtitle': 'LIGHTHOUSE KEEPER • LINE 7',
  'tag': 'INCOMING / DISTRESS SIGNAL',
  'intro': '“They are still out there. I cannot extinguish the lamp. Please stop asking me to reboot it.”',
  'brief': 'The lighthouse shines into empty water. Establish whether the rescue is still in progress.',
  'evidence': [('Review the radio log',
                'Orla sent an SOS for the trawler Mercy. The receiver failed before any reply arrived.'),
               ('Read the harbor manifest',
                'Mercy docked safely at 03:20. Every crew member signed the arrivals ledger.'),
               ('Ask about the haunting',
                'The light returns whenever anyone says “lost at sea.” Orla asks for names, not repairs.')],
  'slots': [('What binds her?',
             ['A rescue she believes failed', 'Ownership of the lighthouse', 'A broken lamp filament']),
            ('Authorize a remedy',
             ['Replace the lamp',
              'Read the signed arrivals over the repaired receiver',
              'Turn off every harbor light'])],
  'answer': [0, 1],
  'explanation': 'The crew survived, but Orla never heard confirmation. Reading their signed arrivals closes '
                 'the rescue rather than abandoning it.'},
 {'name': 'Milo March',
  'subtitle': 'JUNIOR MAGICIAN • AGE 87',
  'tag': 'INCOMING / APPLAUSE LOOP',
  'intro': '“I can escape any box. Except, apparently, the reviews section.”',
  'brief': 'A theater repeats the final minute of a vanished magician’s show. Find what the audience never '
           'received.',
  'evidence': [('Play the final performance',
                'Milo enters a cabinet. The curtain falls before the assistant opens the empty compartment.'),
               ('Inspect the cabinet',
                'The escape passage works. Milo left safely; the disappearance was deliberate stagecraft.'),
               ('Read the stage manager notes',
                'A power cut stopped the finale. The audience left believing the trick had failed. The final '
                'cue was a bow.')],
  'slots': [('What binds him?',
             ['He is physically trapped in the box',
              'His final performance has no ending',
              'His assistant stole the cabinet']),
            ('Authorize a remedy',
             ['Smash the cabinet', 'Arrest the assistant', 'Restore the final cue and invite him to bow'])],
  'answer': [1, 2],
  'explanation': 'Milo escaped the cabinet long ago. He needs the missing final bow so his performance, and '
                 'the audience’s memory of it, can end.'},
 {'name': 'The Voice on Hold',
  'subtitle': 'UNKNOWN CALLER • LINE 0',
  'tag': 'INCOMING / YOUR OWN HOLD MUSIC',
  'intro': '“You said someone would be with me shortly. That was forty-three years ago.”',
  'brief': 'The last caller has no name. The switchboard insists the call is internal.',
  'evidence': [('Trace the connection',
                'Line 0 loops to the support desk itself. No external address exists.'),
               ('Read the old shift log',
                'Operator Evelyn stayed during a flood to answer every call. The final entry reads: '
                '“Awaiting relief operator.”'),
               ('Listen without speaking',
                'The voice recites the staff handover checklist. It goes quiet when you say: “I can take it '
                'from here.”')],
  'slots': [('What binds the caller?',
             ['An abandoned duty with no handover',
              'An unpaid telephone account',
              'A prank call from the basement']),
            ('Authorize a remedy',
             ['Send a bill', 'Accept the handover and sign the relief log', 'Put the caller back on hold'])],
  'answer': [0, 1],
  'explanation': 'Evelyn is the operator who never went off duty. You accept responsibility for the board '
                 'and sign the handover. For the first time in decades, Line 0 rests.'}]

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
