# Hirst Painting: Turtle Style 🎨🐢

A dazzling digital take on Damien Hirst’s iconic spot paintings! This Python script uses the `turtle` module to splash a grid of colorful dots across a moody backdrop. It’s a mini masterpiece generator that picks hues from a vibrant palette and arranges them in neat rows. No brushes needed, just code and a click to admire your creation!

## Controls 🎮

Well, sorta! This isn’t an interactive doodler, it’s a one-shot art machine:
- **Run the Script**: Fire it up with `python hirst_painting.py` and watch the magic happen.
- **Click to Exit**: When you’re done gazing at your Hirst-inspired grid, click the window to close.

No keys, no fuss - just pure, automated artistry!

## Sample Output 🌟

Picture this: a dark bluish-gray canvas (think moody midnight vibes) dotted with 10 rows of 10 colorful circles. Each dot’s a surprise—maybe a fiery red, a cool teal, or a zesty yellow—pulled from a handpicked RGB list. It’s like a pixelated polka-dot party, and every run’s a fresh remix!

## Customize It! 🎉

Want to tweak your masterpiece? Dive into the code:
- Swap `my_screen.bgcolor(0.1, 0.1, 0.2)` for a new vibe—try `(0.9, 0.5, 0.1)` for a sunset glow!
- Add your fave colors to `color_list` in RGB format (e.g., `(255, 105, 180)` for hot pink).
- Change `dot(20, color)` to `dot(30, color)` for bigger spots, or shrink ‘em down to 10.
- Adjust the `50` in `tim_turtle.forward(50)` or `y_pos += 50` to squish or stretch the grid.

Make it yours—Hirst would approve!

## Why’d I Make This?

Because art + code = awesome! I wanted to sprinkle some Hirst-inspired chaos into Python, and `turtle` was the perfect brush. It’s quick, it’s quirky, and it’s a fun nod to those famous spot paintings, minus the million-dollar price tag.
