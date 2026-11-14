# Reverse Detective

**The code in this game is AI-generated.** `reverse_detective.py` was produced by an AI coding assistant, not written by hand as an original human implementation. Review and test it before reusing it or submitting it as your own work.

A single-player, offline desktop deduction game with a dark caseboard interface, gold accents, suspect dossiers, evidence cards, live suspicion bars, and a contradiction audit.

## The story

Lord Ashford was murdered in his study at 10:15 PM. You already know who committed the crime. Your task is to convince the town to blame an innocent suspect by planting a consistent set of clues before the dawn vote. This is a fictional mystery game.

## System and software requirements

| Requirement | Details |
| --- | --- |
| Operating system | macOS, Windows, or Linux with a graphical desktop |
| Python | Python 3.9 or newer |
| GUI toolkit | Tkinter and Tcl/Tk must be available in your Python installation |
| Display | At least 980 × 720 pixels of usable window space; the default window is 1180 × 840 |
| Dependencies | Python standard library only; no third-party packages or `pip install` step |
| Storage | Space for this script and README; the game does not create save files |
| Network | Not needed to play; needed only to download or clone the repository |
| Other software | A terminal or an IDE that can run Python; Git is optional for downloading the project |

Python 3.15.2 and Tk 9.0 are available in the development environment. Game rules were checked independently of the GUI; visual layout and interactive desktop play have not been verified in this session. No minimum CPU or RAM benchmark has been measured.

## How to run

From the repository root:

```bash
python3 "Python Games/Reverse Detective/reverse_detective.py"
```

Or enter this game's folder and run:

```bash
python3 reverse_detective.py
```

On Windows, you can use `py reverse_detective.py` from the game folder. A desktop window opens immediately; no account, assets, or setup wizard is needed.

To check Tkinter availability:

```bash
python3 -m tkinter
```

This should open a small demonstration window. If Tkinter is missing, install a Python distribution with Tcl/Tk support. On Debian/Ubuntu, the usual system package is `python3-tk` (`sudo apt install python3-tk`). On macOS and Windows, the Python installer from [python.org](https://www.python.org/downloads/) normally includes Tkinter. A graphical display is required; a text-only terminal or headless SSH session cannot show the game.

## How to play

1. Read the confidential briefing. It identifies the real culprit, who changes randomly when a new case starts.
2. Read the three suspect dossiers. Use **Choose suspect** to select an innocent person to frame. The guilty suspect cannot be selected.
3. Select one of the eight evidence cards in the middle panel. Its description appears below the cards.
4. Choose a room in **LEAVE IN**, then click **Plant evidence**. Your caseboard can hold up to four unique cards.
5. Watch the suspicion bars and **CONTRADICTION AUDIT**. Match personal clues to your chosen suspect, respect alibis, and place evidence at the crime scene.
6. Click a planted clue's **×** button to remove it and free a slot. Changing your target clears the planted evidence so you can rebuild the case.
7. Click **Call the town vote** when ready. You win only if you planted at least three clues, your target has the unique highest suspicion score, and there are no contradictions.
8. Choose **Play another case** in the verdict window, or **New case** in the main window, to reset. Closing the verdict leaves the completed case locked until you start a new one.

## Rules and scoring

- Each suspect starts with 12 suspicion points. The real culprit starts with 38 instead.
- Evidence placed in the Study adds its listed internal strength (17–27 points) to the chosen target. Personal evidence points to its named owner instead. Evidence in another room adds only 3 points and creates a contradiction.
- Each contradiction subtracts 24 points from your target's total, with a minimum of zero. Any contradiction also prevents victory, even if your target still leads.
- Green wool belongs to Clara; triangular tool marks point to Felix; violet perfume points to Mara. These clues contradict a case against a different person.
- Mara's six witnesses establish her ballroom alibi. The fog witness and muddy footsteps contradict that alibi when she is your target.
- A tie, fewer than three clues, or a stronger case against someone else means a loss.
- Duplicate evidence cannot be planted, and a full caseboard does not accept more cards. Remove an existing clue to make room.
- There is no countdown: “dawn” is story context. Take as long as you like before calling the vote.

The scenario, suspects, and cards stay the same between rounds; only the real culprit and initial target change. Scores, progress, and past results are not saved after closing the app.

## Libraries used

| Library | Source | Purpose |
| --- | --- | --- |
| `tkinter` | Python standard library; requires Tcl/Tk | Desktop window, cards, buttons, room selector, suspicion bars, and verdict dialog |
| `random` | Python standard library | Selects the real culprit for each new case |
| `dataclasses` | Python standard library | Represents suspects, evidence, and mutable case state |

## Files

| File | Purpose |
| --- | --- |
| `reverse_detective.py` | Complete AI-generated game, including rules and desktop interface |
| `README.md` | Requirements, setup, instructions, scoring, and library details |
