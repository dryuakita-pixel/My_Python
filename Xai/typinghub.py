"""
 ████████╗██╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗ ██╗  ██╗██╗   ██╗██████╗
    ██╔══╝╚██╗ ██╔╝██╔══██╗██║████╗  ██║██╔════╝ ██║  ██║██║   ██║██╔══██╗
    ██║    ╚████╔╝ ██████╔╝██║██╔██╗ ██║██║  ███╗███████║██║   ██║██████╔╝
    ██║     ╚██╔╝  ██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══██║██║   ██║██╔══██╗
    ██║      ██║   ██║     ██║██║ ╚████║╚██████╔╝██║  ██║╚██████╔╝██████╔╝
    ╚═╝      ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝
                        Learn Typing the Smart Way
    Run: python typinghub.py   |   Requires Python 3.x (no extra installs)
"""

import tkinter as tk
from tkinter import font as tkfont
import time
import random
import json
import os

# ─── CONFIG ──────────────────────────────────────────────────────────────────
DATA_FILE = "typinghub_data.json"

COLORS = {
    "bg":        "#0d1117",
    "surface":   "#161b22",
    "border":    "#30363d",
    "accent":    "#58a6ff",
    "success":   "#3fb950",
    "error":     "#f85149",
    "warn":      "#d29922",
    "text":      "#e6edf3",
    "muted":     "#8b949e",
    "cursor":    "#58a6ff",
    "highlight": "#1f6feb",
    "pending":   "#8b949e",
}

LESSONS = {
    "🔰 Beginner": [
        "the cat sat on the mat and ate a hat",
        "a big dog ran and had a lot of fun",
        "she can see the sea from her bed",
        "he has a red pen in his bag",
        "the sun is hot and the sky is blue",
        "i like to eat fish with rice and sauce",
        "my dog is fast and can run far",
        "the old man sat by the big oak tree",
    ],
    "📘 Home Row": [
        "asd fjk lkj dsa asd fjk lkj dsa",
        "dad fad sad lad had glad flak flask",
        "all fall hall shall shall fall all hall",
        "ask a lass a flask of salsa",
        "glad flags flap as dadsalk fast lads",
        "has had lad sad fad glad flask shall",
        "add a dash of salt and a flask of soda",
    ],
    "⚡ Common Words": [
        "the quick brown fox jumps over the lazy dog",
        "to be or not to be that is the question",
        "all that glitters is not gold in this world",
        "practice makes perfect and perfect makes habit",
        "every day is a new chance to improve yourself",
        "focus on progress not perfection in your work",
        "small steps taken daily lead to great results",
    ],
    "💻 Programming": [
        "print hello world if x is greater than zero",
        "def main open file read lines and close it",
        "import os sys and json for file handling",
        "for i in range ten print the value of i",
        "while true break if condition is met else pass",
        "try except finally is used for error handling",
        "list dict tuple set are python data structures",
        "class object init self return none pass break",
    ],
    "🚀 Advanced": [
        "the phenomenon of quantum entanglement challenges classical physics",
        "extraordinary achievements require extraordinary levels of commitment",
        "the labyrinthine complexity of bureaucratic procedures frustrated citizens",
        "photosynthesis converts carbon dioxide and water into glucose and oxygen",
        "the juxtaposition of ancient architecture with modern skyscrapers is striking",
        "perseverance through difficulties builds character and resilience in individuals",
        "the philosophical implications of artificial intelligence remain deeply contested",
    ],
    "🔢 Numbers": [
        "the year 2024 brought many changes to the tech world",
        "call 123 456 7890 or email us at support at domain",
        "order 48 units at 12 dollars and 99 cents each",
        "the population reached 8 billion in 2022 according to the UN",
        "use port 8080 for local development and 443 for https",
        "the temperature dropped to minus 15 degrees on january 7",
    ],
}

TIPS = [
    "💡 Keep your fingers on the home row: A S D F  J K L ;",
    "💡 Don't look at the keyboard — trust your fingers!",
    "💡 Accuracy first, then speed. Don't rush.",
    "💡 Take short breaks every 20-30 minutes.",
    "💡 Sit up straight with both feet flat on the floor.",
    "💡 Your wrists should float, not rest on the desk.",
    "💡 Use all 10 fingers — each finger has assigned keys.",
    "💡 Slow down on hard words, then speed back up.",
    "💡 Consistent daily practice beats long weekend sessions.",
    "💡 Target 60+ WPM for professional typing speed.",
]

# ─── DATA MANAGER ─────────────────────────────────────────────────────────────
class DataManager:
    def __init__(self):
        self.data = {"sessions": [], "high_scores": {}, "total_tests": 0}
        self.load()

    def load(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    self.data = json.load(f)
            except Exception:
                pass

    def save(self):
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(self.data, f, indent=2)
        except Exception:
            pass

    def record(self, lesson, wpm, accuracy):
        self.data["total_tests"] += 1
        self.data["sessions"].append({
            "lesson": lesson, "wpm": wpm,
            "accuracy": accuracy, "time": time.strftime("%Y-%m-%d %H:%M")
        })
        if lesson not in self.data["high_scores"] or wpm > self.data["high_scores"][lesson]:
            self.data["high_scores"][lesson] = wpm
        if len(self.data["sessions"]) > 100:
            self.data["sessions"] = self.data["sessions"][-100:]
        self.save()

    def best_wpm(self, lesson):
        return self.data["high_scores"].get(lesson, 0)

    def avg_wpm(self):
        sessions = self.data["sessions"]
        if not sessions:
            return 0
        return round(sum(s["wpm"] for s in sessions) / len(sessions))

    def recent(self, n=5):
        return list(reversed(self.data["sessions"][-n:]))

# ─── MAIN APP ─────────────────────────────────────────────────────────────────
class TypingHub:
    def __init__(self, root):
        self.root = root
        self.root.title("TypingHub — Learn Typing on PC")
        self.root.geometry("900x620")
        self.root.minsize(800, 560)
        self.root.configure(bg=COLORS["bg"])
        self.root.resizable(True, True)

        # Try to set icon (silent fail if not available)
        try:
            self.root.iconbitmap(default="")
        except Exception:
            pass

        self.db = DataManager()
        self.current_lesson = list(LESSONS.keys())[0]
        self.target_text = ""
        self.start_time = None
        self.running = False
        self.errors = 0
        self.correct_chars = 0

        self._setup_fonts()
        self._build_ui()
        self._load_lesson(self.current_lesson)
        self._update_tip()

    # ── Fonts ──────────────────────────────────────────────────────────────────
    def _setup_fonts(self):
        self.font_ui    = tkfont.Font(family="Segoe UI", size=10)
        self.font_title = tkfont.Font(family="Segoe UI", size=18, weight="bold")
        self.font_mono  = tkfont.Font(family="Consolas", size=16)
        self.font_input = tkfont.Font(family="Consolas", size=16)
        self.font_stat  = tkfont.Font(family="Segoe UI", size=13, weight="bold")
        self.font_tip   = tkfont.Font(family="Segoe UI", size=9, slant="italic")

    # ── UI Layout ──────────────────────────────────────────────────────────────
    def _build_ui(self):
        # ── Top Bar
        top = tk.Frame(self.root, bg=COLORS["surface"], height=56)
        top.pack(fill="x")
        top.pack_propagate(False)

        tk.Label(top, text="⌨ TypingHub", font=self.font_title,
                 bg=COLORS["surface"], fg=COLORS["accent"]).pack(side="left", padx=18, pady=10)

        tk.Label(top, text="Learn Typing on PC", font=self.font_ui,
                 bg=COLORS["surface"], fg=COLORS["muted"]).pack(side="left", pady=10)

        self.lbl_total = tk.Label(top, text="Tests: 0", font=self.font_ui,
                                   bg=COLORS["surface"], fg=COLORS["muted"])
        self.lbl_total.pack(side="right", padx=18)

        btn_history = tk.Button(top, text="📊 Stats", font=self.font_ui,
                                bg=COLORS["highlight"], fg="white", bd=0,
                                padx=12, pady=4, cursor="hand2",
                                activebackground=COLORS["accent"],
                                command=self._show_stats)
        btn_history.pack(side="right", padx=6, pady=10)

        # ── Main Area
        main = tk.Frame(self.root, bg=COLORS["bg"])
        main.pack(fill="both", expand=True, padx=16, pady=10)

        # Left: lesson selector
        left = tk.Frame(main, bg=COLORS["surface"], width=190,
                        highlightbackground=COLORS["border"], highlightthickness=1)
        left.pack(side="left", fill="y", padx=(0, 10))
        left.pack_propagate(False)

        tk.Label(left, text="LESSONS", font=tkfont.Font(family="Segoe UI", size=9, weight="bold"),
                 bg=COLORS["surface"], fg=COLORS["muted"]).pack(pady=(14, 6), padx=10, anchor="w")

        self.lesson_btns = {}
        for name in LESSONS:
            btn = tk.Button(left, text=name, font=self.font_ui,
                            bg=COLORS["surface"], fg=COLORS["text"],
                            bd=0, padx=10, pady=7, anchor="w", width=22,
                            cursor="hand2", activebackground=COLORS["highlight"],
                            command=lambda n=name: self._load_lesson(n))
            btn.pack(fill="x", padx=6, pady=1)
            self.lesson_btns[name] = btn

        tk.Frame(left, bg=COLORS["border"], height=1).pack(fill="x", pady=8)

        self.lbl_best = tk.Label(left, text="Best: — WPM", font=self.font_ui,
                                  bg=COLORS["surface"], fg=COLORS["success"])
        self.lbl_best.pack(padx=10, anchor="w")

        self.lbl_avg = tk.Label(left, text="Avg:  — WPM", font=self.font_ui,
                                 bg=COLORS["surface"], fg=COLORS["accent"])
        self.lbl_avg.pack(padx=10, pady=(2, 0), anchor="w")

        # Right: typing area
        right = tk.Frame(main, bg=COLORS["bg"])
        right.pack(side="left", fill="both", expand=True)

        # Stats row
        stats_row = tk.Frame(right, bg=COLORS["bg"])
        stats_row.pack(fill="x", pady=(0, 10))

        self.lbl_wpm = self._stat_box(stats_row, "WPM", "0", COLORS["accent"])
        self.lbl_acc = self._stat_box(stats_row, "Accuracy", "100%", COLORS["success"])
        self.lbl_err = self._stat_box(stats_row, "Errors", "0", COLORS["error"])
        self.lbl_time = self._stat_box(stats_row, "Time", "0s", COLORS["warn"])

        # Target text display
        txt_frame = tk.Frame(right, bg=COLORS["surface"],
                             highlightbackground=COLORS["border"], highlightthickness=1)
        txt_frame.pack(fill="x", pady=(0, 10))

        self.txt_display = tk.Text(txt_frame, font=self.font_mono,
                                   bg=COLORS["surface"], fg=COLORS["pending"],
                                   height=3, wrap="word", bd=0,
                                   state="disabled", padx=16, pady=14,
                                   cursor="arrow", selectbackground=COLORS["surface"])
        self.txt_display.pack(fill="x")
        self.txt_display.tag_config("correct",  foreground=COLORS["text"])
        self.txt_display.tag_config("wrong",    foreground=COLORS["error"],
                                    background="#2d1014")
        self.txt_display.tag_config("current",  foreground=COLORS["cursor"],
                                    underline=True)
        self.txt_display.tag_config("pending",  foreground=COLORS["pending"])

        # Input box
        inp_frame = tk.Frame(right, bg=COLORS["surface"],
                             highlightbackground=COLORS["accent"], highlightthickness=2)
        inp_frame.pack(fill="x", pady=(0, 8))

        self.entry_var = tk.StringVar()
        self.entry_var.trace("w", self._on_type)

        self.entry = tk.Entry(inp_frame, textvariable=self.entry_var,
                              font=self.font_input, bg=COLORS["surface"],
                              fg=COLORS["text"], bd=0, insertbackground=COLORS["accent"],
                              highlightthickness=0)
        self.entry.pack(fill="x", ipady=12, padx=14)
        self.entry.bind("<space>",    self._on_space)
        self.entry.bind("<Return>",   self._on_enter)
        self.entry.bind("<Escape>",   lambda e: self._reset())

        # Bottom controls
        ctrl = tk.Frame(right, bg=COLORS["bg"])
        ctrl.pack(fill="x")

        self.btn_restart = tk.Button(ctrl, text="⟳  New Text  (Enter)",
                                     font=self.font_ui,
                                     bg=COLORS["highlight"], fg="white",
                                     bd=0, padx=16, pady=6, cursor="hand2",
                                     activebackground=COLORS["accent"],
                                     command=self._reset)
        self.btn_restart.pack(side="left", padx=(0, 8))

        self.btn_replay = tk.Button(ctrl, text="↺  Same Text",
                                    font=self.font_ui,
                                    bg=COLORS["border"], fg=COLORS["text"],
                                    bd=0, padx=16, pady=6, cursor="hand2",
                                    activebackground=COLORS["highlight"],
                                    command=self._replay)
        self.btn_replay.pack(side="left")

        # Tip label
        self.lbl_tip = tk.Label(right, text="", font=self.font_tip,
                                 bg=COLORS["bg"], fg=COLORS["muted"],
                                 wraplength=640, justify="left")
        self.lbl_tip.pack(anchor="w", pady=(8, 0))

        # Result banner (hidden by default)
        self.result_frame = tk.Frame(right, bg=COLORS["success"])
        self.lbl_result = tk.Label(self.result_frame, text="", font=self.font_stat,
                                    bg=COLORS["success"], fg="white", padx=14, pady=8)
        self.lbl_result.pack()

        self._update_totals()

    def _stat_box(self, parent, label, value, color):
        frame = tk.Frame(parent, bg=COLORS["surface"],
                         highlightbackground=COLORS["border"], highlightthickness=1)
        frame.pack(side="left", padx=(0, 8), ipadx=14, ipady=6)
        tk.Label(frame, text=label, font=self.font_ui,
                 bg=COLORS["surface"], fg=COLORS["muted"]).pack()
        lbl = tk.Label(frame, text=value, font=self.font_stat,
                       bg=COLORS["surface"], fg=color)
        lbl.pack()
        return lbl

    # ── Lesson Management ──────────────────────────────────────────────────────
    def _load_lesson(self, name):
        self.current_lesson = name
        for n, b in self.lesson_btns.items():
            b.configure(bg=COLORS["highlight"] if n == name else COLORS["surface"])
        best = self.db.best_wpm(name)
        self.lbl_best.configure(text=f"Best: {best} WPM" if best else "Best: — WPM")
        avg = self.db.avg_wpm()
        self.lbl_avg.configure(text=f"Avg:  {avg} WPM" if avg else "Avg:  — WPM")
        self._reset()

    def _reset(self):
        texts = LESSONS[self.current_lesson]
        self.target_text = random.choice(texts)
        self._start_fresh()

    def _replay(self):
        self._start_fresh()

    def _start_fresh(self):
        self.start_time = None
        self.running = False
        self.errors = 0
        self.correct_chars = 0
        self.typed_pos = 0

        self.entry_var.set("")
        self.entry.configure(state="normal")
        self.entry.focus_set()

        self.lbl_wpm.configure(text="0")
        self.lbl_acc.configure(text="100%")
        self.lbl_err.configure(text="0")
        self.lbl_time.configure(text="0s")

        self.result_frame.pack_forget()
        self._render_text("")
        inp_frame = self.entry.master
        inp_frame.configure(highlightbackground=COLORS["accent"])

    # ── Typing Logic ───────────────────────────────────────────────────────────
    def _on_type(self, *_):
        typed = self.entry_var.get()

        # Start timer on first keystroke
        if not self.running and typed:
            self.start_time = time.time()
            self.running = True
            self._tick()

        # Check for completion (user typed last char)
        if len(typed) >= len(self.target_text) and typed:
            self._finish(typed)
            return

        self._render_text(typed)
        self._update_live_stats(typed)

    def _on_space(self, event):
        pass  # allow normal space

    def _on_enter(self, event):
        self._reset()

    def _render_text(self, typed):
        self.txt_display.configure(state="normal")
        self.txt_display.delete("1.0", "end")

        target = self.target_text
        for i, ch in enumerate(target):
            if i < len(typed):
                tag = "correct" if typed[i] == ch else "wrong"
            elif i == len(typed):
                tag = "current"
            else:
                tag = "pending"
            self.txt_display.insert("end", ch, tag)

        self.txt_display.configure(state="disabled")

    def _update_live_stats(self, typed):
        if not self.start_time:
            return
        elapsed = max(time.time() - self.start_time, 0.1)
        words = len(typed.split())
        wpm = int((words / elapsed) * 60)

        # count errors
        errors = sum(1 for i, c in enumerate(typed)
                     if i < len(self.target_text) and c != self.target_text[i])
        correct = len(typed) - errors
        accuracy = int((correct / max(len(typed), 1)) * 100)

        self.lbl_wpm.configure(text=str(wpm))
        self.lbl_acc.configure(text=f"{accuracy}%")
        self.lbl_err.configure(text=str(errors))

        # Color entry border based on last char
        if typed:
            last_ok = (len(typed) <= len(self.target_text) and
                       typed[-1] == self.target_text[len(typed)-1])
            color = COLORS["success"] if last_ok else COLORS["error"]
            self.entry.master.configure(highlightbackground=color)

    def _tick(self):
        if self.running and self.start_time:
            elapsed = int(time.time() - self.start_time)
            self.lbl_time.configure(text=f"{elapsed}s")
            self.root.after(500, self._tick)

    def _finish(self, typed):
        self.running = False
        elapsed = max(time.time() - self.start_time, 0.1)

        words = len(self.target_text.split())
        wpm = int((words / elapsed) * 60)

        errors = sum(1 for i, c in enumerate(typed[:len(self.target_text)])
                     if c != self.target_text[i])
        total = len(self.target_text)
        accuracy = int(((total - errors) / total) * 100)

        self.lbl_wpm.configure(text=str(wpm))
        self.lbl_acc.configure(text=f"{accuracy}%")
        self.lbl_err.configure(text=str(errors))
        self.lbl_time.configure(text=f"{int(elapsed)}s")

        self.db.record(self.current_lesson, wpm, accuracy)
        self._update_totals()

        # Best score check
        best = self.db.best_wpm(self.current_lesson)
        self.lbl_best.configure(text=f"Best: {best} WPM")
        avg = self.db.avg_wpm()
        self.lbl_avg.configure(text=f"Avg:  {avg} WPM")

        # Show result banner
        is_best = (wpm == best)
        grade = self._grade(accuracy, wpm)
        msg = f"{'🏆 NEW BEST!  ' if is_best else ''}  {wpm} WPM  ·  {accuracy}% Accuracy  ·  {grade}"
        color = COLORS["success"] if accuracy >= 90 else COLORS["warn"]
        self.result_frame.configure(bg=color)
        self.lbl_result.configure(text=msg, bg=color)
        self.result_frame.pack(fill="x", pady=(8, 0))

        self.entry.configure(state="disabled")
        self._render_text(typed)

    def _grade(self, accuracy, wpm):
        if accuracy < 80:      return "Keep practicing! 💪"
        if wpm < 20:           return "Beginner 🌱"
        if wpm < 40:           return "Improving 📈"
        if wpm < 60:           return "Intermediate ⭐"
        if wpm < 80:           return "Advanced 🔥"
        if wpm < 100:          return "Expert ⚡"
        return "Master Typist 🏆"

    def _update_totals(self):
        self.lbl_total.configure(text=f"Tests: {self.db.data['total_tests']}")

    def _update_tip(self):
        self.lbl_tip.configure(text=random.choice(TIPS))
        self.root.after(12000, self._update_tip)

    # ── Stats Window ───────────────────────────────────────────────────────────
    def _show_stats(self):
        win = tk.Toplevel(self.root)
        win.title("TypingHub — Statistics")
        win.geometry("520x420")
        win.configure(bg=COLORS["bg"])
        win.grab_set()

        tk.Label(win, text="📊  Your Statistics", font=self.font_title,
                 bg=COLORS["bg"], fg=COLORS["accent"]).pack(pady=(18, 6))

        # High scores
        hs_frame = tk.Frame(win, bg=COLORS["surface"],
                             highlightbackground=COLORS["border"], highlightthickness=1)
        hs_frame.pack(fill="x", padx=20, pady=8)
        tk.Label(hs_frame, text="BEST SCORES PER LESSON",
                 font=tkfont.Font(family="Segoe UI", size=9, weight="bold"),
                 bg=COLORS["surface"], fg=COLORS["muted"]).pack(anchor="w", padx=12, pady=(8, 4))

        for lesson, score in self.db.data["high_scores"].items():
            row = tk.Frame(hs_frame, bg=COLORS["surface"])
            row.pack(fill="x", padx=12, pady=1)
            tk.Label(row, text=lesson, font=self.font_ui,
                     bg=COLORS["surface"], fg=COLORS["text"]).pack(side="left")
            tk.Label(row, text=f"{score} WPM", font=self.font_ui,
                     bg=COLORS["surface"], fg=COLORS["success"]).pack(side="right")
        if not self.db.data["high_scores"]:
            tk.Label(hs_frame, text="No data yet — complete a test!",
                     font=self.font_ui, bg=COLORS["surface"],
                     fg=COLORS["muted"]).pack(padx=12, pady=4)

        tk.Label(hs_frame, text="", bg=COLORS["surface"]).pack(pady=2)

        # Recent sessions
        rec_frame = tk.Frame(win, bg=COLORS["surface"],
                              highlightbackground=COLORS["border"], highlightthickness=1)
        rec_frame.pack(fill="x", padx=20, pady=8)
        tk.Label(rec_frame, text="RECENT SESSIONS",
                 font=tkfont.Font(family="Segoe UI", size=9, weight="bold"),
                 bg=COLORS["surface"], fg=COLORS["muted"]).pack(anchor="w", padx=12, pady=(8, 4))

        for s in self.db.recent(6):
            row = tk.Frame(rec_frame, bg=COLORS["surface"])
            row.pack(fill="x", padx=12, pady=1)
            tk.Label(row, text=f"{s['time']}  {s['lesson'][:18]}",
                     font=self.font_ui, bg=COLORS["surface"],
                     fg=COLORS["muted"]).pack(side="left")
            tk.Label(row, text=f"{s['wpm']} WPM  {s['accuracy']}%",
                     font=self.font_ui, bg=COLORS["surface"],
                     fg=COLORS["accent"]).pack(side="right")
        if not self.db.data["sessions"]:
            tk.Label(rec_frame, text="No sessions yet.",
                     font=self.font_ui, bg=COLORS["surface"],
                     fg=COLORS["muted"]).pack(padx=12, pady=4)
        tk.Label(rec_frame, text="", bg=COLORS["surface"]).pack(pady=2)

        # Summary
        total = self.db.data["total_tests"]
        avg = self.db.avg_wpm()
        tk.Label(win, text=f"Total Tests: {total}   ·   Average WPM: {avg}",
                 font=self.font_ui, bg=COLORS["bg"], fg=COLORS["muted"]).pack(pady=4)

        tk.Button(win, text="Close", font=self.font_ui,
                  bg=COLORS["highlight"], fg="white", bd=0, padx=24, pady=6,
                  cursor="hand2", command=win.destroy).pack(pady=6)


# ─── ENTRY POINT ──────────────────────────────────────────────────────────────
def main():
    root = tk.Tk()

    # DPI fix for Windows
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

    app = TypingHub(root)
    root.mainloop()


if __name__ == "__main__":
    main()
