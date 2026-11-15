# Sabotage the Prophecy

**This game's code is AI-generated.** `sabotage_the_prophecy.py` was produced by OpenAI Codex, an AI coding assistant. It is not an original hand-written implementation. Review and test it before reusing it, changing it, or submitting it as your own work. The accompanying puzzle content and documentation were also AI-generated.

A semantic puzzle game about fulfilling ominous prophecies without letting anyone get hurt. Use authorized alternate meanings to turn five threatening verses into harmless events.

## System and software requirements

| Requirement | Details |
| --- | --- |
| Operating system | macOS, Windows, or Linux with a graphical desktop |
| Python | Python 3.9 or newer |
| GUI toolkit | Tkinter with Tcl/Tk available to the Python interpreter |
| Display | At least 1020 × 720 pixels of usable window space; default window 1240 × 880 |
| Dependencies | Python standard library only; no third-party packages or `pip install` step |
| Storage | The script and this README; no downloaded assets, database, or save files |
| Network | Not required to play; only needed to download or clone the project |
| Input | Mouse or trackpad, with keyboard navigation for standard Tkinter controls |
| Other software | A terminal or Python-capable IDE; Git is optional for downloading |

No minimum CPU or RAM benchmark is claimed. The window contains a vertical scrollbar: drag it when expanded records or decisions extend below the visible area.

## How to run

From the repository root:

```bash
python3 "Python Games/Sabotage the Prophecy/sabotage_the_prophecy.py"
```

Or from this game's folder:

```bash
python3 sabotage_the_prophecy.py
```

On Windows, use `py sabotage_the_prophecy.py` if `python3` is not available. You can also open the script in an IDE and run it with a Python interpreter that has Tkinter installed.

Check Tkinter independently with:

```bash
python3 -m tkinter
```

A demonstration window should open. If importing Tkinter fails, install a Python distribution with Tcl/Tk support. Python installers from [python.org](https://www.python.org/downloads/) normally include Tkinter on macOS and Windows. Debian/Ubuntu commonly supplies it through `sudo apt install python3-tk`. A text-only SSH session cannot display this game.

## How to play

1. Read the sealed verse and the safety objective in the left panel.
2. Open the glossary, scene reports, and constraints under **Find the Loophole**.
3. Choose all three parts of your plan in **Rewrite the Outcome**.
4. Make sure the verse remains literally true, the selected meanings are explicitly permitted, and the safety objective is satisfied.
5. Click **Set fate in motion**. Read the explanation, then choose **Unseal next verse**.
6. Complete all five verses for your final score. Replay to try different interpretations.

## Game rules and features

- Five verses: the Crown, the Bell, the Wolf, the royal Line, and Hope.
- Each verse has three investigation records and three plan components with three options each.
- Each complete correct plan earns 100 points; a plan with any incorrect component earns 0. Maximum shift score: 500.
- Only meanings authorized by each puzzle’s records count. Invented synonyms and arbitrary stand-ins do not qualify.
- All three selected components must satisfy the timing, place, meaning, and protection conditions together.
- Verses have fixed solutions. This is a multiple-choice puzzle game, not a free-text language parser.
- Amber-and-plum archive interface, a geometric fate emblem, and an explanation of every loophole.

## Shared controls and behavior

- **Restart shift** clears the current score, selections, inspections, and history after a confirmation prompt when a shift has started.
- Click an inspection heading to reveal its contents. Open records stay open for the current case.
- The submit button becomes available only after every required decision is selected.
- **Control+Enter** or **Command+Enter** also submits a complete decision.
- After submission, choices and records are locked, the result is explained, and points can be awarded only once.
- Advance using the next-case button. Decisions and inspections reset for each new case; your shift score and result history remain.
- There is no timer, resource cost, combat, or real online AI service. All dialogue, records, and outcomes are local authored content.
- Closing the window exits. Progress and scores are not saved between launches.

## Libraries used

| Library | Source | Purpose |
| --- | --- | --- |
| `tkinter` | Python standard library; requires Tcl/Tk | Window, panels, illustration canvas, buttons, scrollable caseboard, and keyboard bindings |
| `tkinter.messagebox` | Python standard library | Confirmation before clearing a shift |
| `dataclasses` | Python standard library | Session state: case index, score, decisions, opened records, and result history |

No external fonts, images, sound files, or Python packages are required. Helvetica is requested; Tk uses a system fallback where unavailable. The game is text-based and has no audio or voice acting.

## Files

| File | Purpose |
| --- | --- |
| `sabotage_the_prophecy.py` | Standalone AI-generated game, puzzle data, rules, and Tkinter interface |
| `README.md` | Requirements, setup, instructions, scoring, controls, and AI-generation disclosure |

## Verification

The development environment provides Python 3.15.2 and Tk 9.0. Validation covers Python compilation, authored-case completeness, successful and unsuccessful answers, incomplete submissions, scoring only once, locked decisions, and progression through an entire shift. Tk desktop smoke tests passed at 1240 × 880 and 1020 × 720, with all records expanded and every result screen rendered. Automated UI checks do not replace manual playtesting; screenshot-based visual review and cross-platform verification were not completed.
