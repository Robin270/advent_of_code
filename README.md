# Advent of Code :sparkler::computer: 
![Advent of Code in Python](https://blog.pythondiscord.com/content/images/2021/03/AoC_banner.png "Advent of Code in Python")
My **Python** solutions to the **[Advent of Code event](https://adventofcode.com/)**.

All of them were done **purely on my own**. This means I haven't searched for solutions or any other help connected directly to the task. This basically means I didn't cheat – if there is ever something missing, then it means I didn't successfully solve it. But of course I was using Google a lot for those basic things I know about but never seem to be able to remember the syntax or whatever – but we're all like this, right? :sweat-smile:

And very important to mention is that this is why these solutions are not always the cleanest, most straight-forward, fastest or most efficient ones. But they're 100% working and that is what matters. At least for me, since I really enjoy it as a part of the endless process of self-improvement.

## Structure
Each included year has a dedicated directory in the root, and within that directory, subdirectories for each solved day of that year are located.

Inside the individual day subdirectories, there is always:
* a `main.py` script containing the whole working solution for both parts of that day
* an `input.in` file with the whole raw input data for the given day the way they were assigned

### AoC utils module
Apart from the technical/git-associated files, there is a custom Python module named [`aoc_utils.py`](/aoc_utils.py) directly in the root.

It's consisted of sparate functions that are used within the solution scripts to [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) those scripts at least a little bit. All the functions have their own docstrings.

The functions are:
* either general-purpose ones used to do technical stuff that are not connected to the actual task (e.g. load the input data)
* or specific-purpose ones that deal with some logical algorithms as a direct part of solving the task (e.g. find neighbouring elements in a 2D list)

## Thought
I don't feel like it is worth putting together my own comments or analysis of the tasks or making this repository super comprehensive in any other way, since others are already doing such things and I'm sure I at least wouldn't have done better than for example this guy [over here](https://github.com/mebeim/aoc) :smile:. So if you'd like to find out more about it all, go and check out the link.
