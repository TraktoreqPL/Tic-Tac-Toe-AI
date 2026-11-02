# Tic-Tac-Toe-AI

## What is it?
This is an Tic Tac Toe game with **AI** in *Pygame*.

## How to run it?
You need only to install *Pygame* for example
```bash
pip install pygame
```
and run it on the python interpreter.
```bash
python KółkoiKrzyżykAI.py
```
You can of course use other tools.

This app makes a file named `dane.pkl`. **Do not** delete it or the training data will be gone.

## How it works?
This is **not** an AI. It's just copying your moves. For example in the situation *A* you make a move *B*. The AI will remember that and if it will be in the situation *A* it will make the move *B*.

## History
I was on [*AlphaCamp*](https://www.alphacamp.pl/) in *Zaklinacze Robotów* (programming) and we need to make an *Python* game in few days. The game must contain AI (my doesn't :) ). Beacuse of short time there are weird optimizations (1-byte Boolean array instead of standard *Python*'s 28-byte).

#### I am working on an English variable and file version so don't worry if you don't understand. I will made a new branch for it.
