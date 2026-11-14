# Tic Tac Toe

**This code is AI-generated.** `tic_tac_toe.py` was written by an AI coding assistant in Cursor. It is not an original hand-written implementation. Review the file before you depend on it, change it, or turn it in as your own work.

Two people play Tic Tac Toe in a desktop window. They enter their names, take turns on a 3×3 board, and can play as many rounds as they want. Wins, losses, and draws are kept for those names and saved on this computer until the window is closed.

## How to run

From this folder:

```bash
python3 tic_tac_toe.py
```

A name window opens first. Type both names and choose **Start game**. If a name is left blank, the game uses `Player 1` or `Player 2`. If both names are the same, the second player is shown as that name plus `(O)` so the scores stay separate.

## How the game works

1. Player X goes first. The highlighted card and the line under the title show whose turn it is.
2. A player clicks an empty cell. X is drawn in teal and O in rose. A filled cell cannot be changed.
3. The game checks the eight winning lines: three rows, three columns, and two diagonals. Three matching marks end the round. The winning cells turn gold, that player's win count goes up by one, and the other player's loss count goes up by one.
4. If every cell is filled and nobody has three in a row, the round is a draw. Both players get one draw.
5. A panel then appears on the board with **Play again**. That button clears only the board. Names and scores stay. The same two players can keep playing new rounds.
6. Closing the window ends the session. The next time the game starts, saved scores for those names are loaded again.

Buttons under the board:

- **Play again** starts a fresh board for the current players and keeps their scores.
- **Change names** asks for two names again. Scores already stored for a name are loaded instead of wiped.
- **Reset these scores** sets wins, losses, and draws to zero for the two people who are playing now. Other names stored in the score file are left as they are.

## Scores

Scores are written to `scores.json` in this folder. That file is created the first time a result is saved. It is local play data, so it is not part of this repository.

Each name stores three numbers:

```json
{
  "Asha": { "wins": 2, "losses": 1, "draws": 0 },
  "Rohan": { "wins": 1, "losses": 2, "draws": 0 }
}
```

The file is updated when a round ends, when names are confirmed, and when these players' scores are reset.

## Libraries

No third-party packages are required. There is no `pip install` step.

| Library | Where it comes from | What it is used for |
| --- | --- | --- |
| `tkinter` | Python standard library (needs Tcl/Tk) | The window, name dialog, player cards, board, and buttons |
| `json` | Python standard library | Reading and writing `scores.json` |
| `pathlib` | Python standard library | Locating `scores.json` next to the script |

## System and software requirements

- **Operating system:** macOS, Windows, or a current Linux desktop. The game needs a graphical display. It will not run over a plain text-only SSH session.
- **Python:** 3.9 or newer, with Tkinter available. This project was run with Python 3.15 and Tk 9.0 on macOS.
- **Tkinter:** included with the installers from [python.org](https://www.python.org/downloads/) on macOS and Windows. On Debian or Ubuntu, install it with `sudo apt install python3-tk` if `import tkinter` fails.
- **Disk:** a few megabytes for Python itself. The game also needs permission to create `scores.json` in this folder.
- **Display:** a window of about 760×860 pixels. The window size is fixed.
- **Network:** not required to play. Network access is required only if you clone this repository.
- **Other software:** a terminal to start the script, or any way you normally run a Python file. Git is needed only to download the project, not to play.

## Files in this folder

| File | Purpose |
| --- | --- |
| `tic_tac_toe.py` | The whole game. AI-generated. |
| `README.md` | This explanation |
| `scores.json` | Created on your computer when you play. Not stored in Git. |
