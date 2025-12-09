# CSC223 Final

The final project for CSC223 (Fall 2025 semester) at Mississippi College

**Created by:** [Micah Lindley](https://github.com/micahlt), [Max Jones](https://github.com/Max-J11), and [Ian Turner](https://github.com/TheLazyProgrammer-ux)

## Setup Docs

1. Clone the repository to your computer.
2. Install [Python 3](https://www.python.org/downloads) if you haven't already.
3. Initialize the Python Virtual Environment: `python3 -m venv venv`
4. Enter the virtual environment: `source venv/bin/activate` on Linux/macOS or `venv\Scripts\activate` on Windows.
5. Install dependencies: `pip install numpy matplotlib seaborn`

## Git Cheatsheet

Here's Micah's basic Git cheat sheet:

***Rules:***

- **Always do your work in a branch.**  Don't commit to `master`.
- **Fetch and pull before branching.**  Don't forget this, as it'll cause merge conflicts down the line.
- **Keep commits contextual.**  For readability's sake, don't do a TON of work in a single commit.  If you're done with a small fix or feature addition, go ahead and commit to your branch, then make another commit for the next change.

***Workflow:***

1. Branch from `master`.  Make sure you're on the `master` branch (see the bottom right of VSCode), and that there is nothing to be pulled from GitHub.  Then open the command palette (**Ctrl+Shift+P**) and run the **Git: Create branch...** command.  Name your branch something like `feature/species-hunting` or `fix/type-error`, based on whether or not it's a feature or a bugfix.  The current branch in the bottom right of VSCode should show your new branch name.
2. Make changes to your code, and save each of your files (**Ctrl+S**).
3. Stage the changes to be committed.  In the Source Control panel, hover over changes until the plus icon appears.  It should say **Stage All Changes** when you hover over it.  Click it.  Alternatively, you can choose which files you want to commit.  This is good for when you accidentally forgot to commit and need to separate your changes into two or more commits.
4. Commit the changes.  Write a good commit message that describes what you changed.  Then click the big **Commit** button with a checkmark in it.
5. Push your changes to GitHub.  Click the big **Sync Changes** button.
6. When your branch is ready to be merged, create a **pull request**.  Go to the GitHub page for this repository, click the branch dropdown that probably says **master** with a branch icon beside it, and select your branch.  When the page switches to your branch, click the **Contribute** button and click **Open pull request**.  Change the title and description to be descriptive of what your branch adds to the project.
7. Wait for review (*probably*).  If your code modifies important sections of the codebase, or if there are merge conflicts, talk to Micah first.  He can review the pull request (or **PR**) to make sure that everything gets merged in a way that nothing gets broken.  If it's clear that your pull request is ok to merge, go ahead and find the button that says **Merge pull request**.  This will apply your changes to the `master` branch.
8. Start your next large-scale feature or fix by starting over and creating a new branch from `master` (as in step 1).  Do this by switching back to the `master` branch by clicking the name of your branch in the bottom right of VSCode, and then clicking the `master` branch from the list that pops up at the top of the window.  *Alternatively*, you can merge `master` into your branch to get it up to date, but that's more complex.
