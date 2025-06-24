# Snake Game

Welcome to my first GitHub repository!  
This repository was created as part of my technical preparation for an upcoming interview with Sogeti, with the goal of demonstrating proficiency in using Git and GitHub for project version control.

## About the Project

This is a classic Snake Game developed in Python using the `turtle` graphics module. It follows object-oriented programming (OOP) principles to structure the game components in a modular and maintainable way.

## Features

- Real-time snake movement
- Food spawning logic
- Score tracking and high score persistence
- Game over detection
- Clean OOP structure (`Snake`, `Food`, `Scoreboard` classes)

## High Score Tracking

The game keeps track of your highest score across sessions using a simple `data.txt` file. This file stores the top score and is automatically updated whenever a new high score is achieved.  
If the file is missing or empty, the game safely initializes the high score as `0`.

Git tip: You can choose to track `data.txt` in version control, or add it to `.gitignore` to keep it personal to each machine.

## How to Run

Make sure you have Python 3 installed, then run:

```bash
python main.py


