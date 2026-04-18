# STEM on Stage — Course Notebooks 📓

Welcome! This repo holds the **Jupyter notebooks** we use in class. Everything runs in your web browser — there is **nothing to install**. 🎉

---

## ✨ What's a notebook?

A **notebook** is a document that mixes:
- 📝 **text** (like the words you're reading right now),
- 💻 **Python code**, and
- 📊 **the output** of that code (numbers, plots, tables) — all on the same page.

You read top-to-bottom and run code as you go. Notebooks live in files that end in `.ipynb`.

## 🚀 How to open a notebook (the easy way)

We use **Google Colab**, a free service from Google that runs notebooks in your browser. You don't install anything — Colab is just a website.

1. Find the notebook you want in the file list above (e.g. `hello.ipynb`).
2. Click on it. GitHub will show a preview.
3. Look for the badge that says ![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) at the top — click it.
4. Sign in with **any Google account** (a personal `gmail.com` account is fine).
5. Colab opens the notebook. You're ready to go.

> **Use Chrome or Edge** as your browser. Colab works in others, but later in the course we capture sensor data from a micro:bit, and that step needs Chrome or Edge.

## ▶️ How to run code

Each grey box is a **cell**. To run one:

1. Click anywhere inside the cell.
2. Press **`Shift` + `Enter`**.

The output (text, a plot, a number) shows up right under the cell. Then the next cell is selected — keep pressing `Shift+Enter` to walk through the whole notebook.

That's it. Really.

## 🔁 Re-running and editing

You can **edit any cell** and run it again. Notebooks are scratchpads — break them, fix them, that's the whole point.

If something gets stuck or weird (a variable disappeared, a plot won't update), use:

> **`Runtime` → `Restart session`**

This wipes everything and lets you start the notebook fresh. Don't worry — your text and code stay; only the running state resets.

## 💾 Saving your work

⚠️ **Important:** Colab does **not** automatically save your changes back to GitHub. Your work lives in a temporary copy. To keep your edits:

- **`File` → `Download` → `Download .ipynb`** — saves the file to your computer's Downloads folder. This is the simplest option for class.
- *Or*, **`File` → `Save a copy in Drive`** — keeps it in your Google Drive so you can come back to it later.

Bring the downloaded `.ipynb` to next class if you're asked to.

> 🧹 If you don't open the notebook for ~90 minutes, Colab "times out" and any uploaded files (like your sensor recordings) disappear. The notebook itself is fine — just re-upload your CSV when you come back.

---

## 📂 What's in this repo

| File / folder | What it is |
|---|---|
| `hello.ipynb` | **Start here.** A 5-minute first-time tour of notebooks — no data needed. Try it the first time you open Colab. |
| `L10/L10_starter.ipynb` | Lesson 10 — load and visualize accelerometer data from your micro:bit. |
| `data/sample-walk.csv` | A pretend "walking" recording, so the L10 notebook works before you've made your own. |
| `data/microbit-data-2026-04-17T...csv` | A real recording — useful as a reference for what your own captures should look like. |

---

## 🎚️ Lesson 10 special: capturing your own sensor data

After you can read a CSV in the notebook, you'll record your own from a micro:bit. Two browser tabs:

1. **Tab 1 — capture (Chrome/Edge required):** open https://makecode.microbit.org, flash the *Reading Raw Acceleration* program, then `Show Console Device` → `Download`. A CSV with a name like `microbit-data-2026-04-18T....csv` lands in your Downloads folder.
2. **Tab 2 — analyze (Colab):** open `L10/L10_starter.ipynb`, click the 📁 folder icon on the left, and drag your CSV in. Re-run the cells with the new file — done.

The slides for L10 walk through this with screenshots.

---

## 🆘 Troubleshooting

- **"My code says `NameError: name 'df' is not defined`"** — you ran a later cell before the earlier ones. Click the first cell and `Shift+Enter` your way down.
- **"My plot is empty / wrong"** — `Runtime` → `Restart session`, then re-run from the top.
- **"Where did my CSV go?"** — Colab probably timed out. Re-upload it from the 📁 panel on the left.
- **"The MakeCode console won't download"** — make sure you're in **Chrome** or **Edge**, not Safari or Firefox.
- **Stuck on something else?** — bring it to class. Asking is the fastest debugger. 🛠️

Have fun! 🪩
