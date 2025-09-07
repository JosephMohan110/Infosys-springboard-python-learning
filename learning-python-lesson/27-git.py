#    # GIT


# 1. Difference Between Git and GitHub


# Git:

# A version control system (VCS) used to track changes in code
# Installed locally on your computer
# Manages local repositories
# Helps in committing, branching, merging, and reverting code versions

# GitHub:
# A cloud-based platform for hosting Git repositories
# Allows collaboration between developers
# Provides features like pull requests, issues, code reviews, and project management
# Used to push local repositories to the cloud and share code online
# Summary: Git is a tool to track code changes, GitHub is a platform to host and collaborate using Git



# 2. Untracked and Modified Files in Git

# Untracked Files:
# Files that are in your project folder but not added to Git
# Git doesn’t track changes in these files yet
# You can add them using git add filename


# Modified Files:
# Files that are already tracked by Git but have been changed since the last commit
# You need to add and commit them to save changes


# Example Workflow:
# Create a new file → it appears as untracked
# git add : stages the file
# Modify the file : it appears as modified
# git commit : saves changes permanently in Git history




# 3. Comments in Git / Git Commands Explained

# git init
# Initializes a new Git repository in your project folder
# Creates a .git folder that tracks all changes

# git add <filename>
# Adds untracked or modified files to the staging area
# Only staged files are included in the next commit

# git status
# Shows the current state of the repository.
# Displays untracked, modified, and staged files

# git commit -m "message"
# Saves staged changes to the local repository
# -m adds a commit message describing the changes

# git log
# Shows the history of commits in the repository
# Includes commit ID, author, date, and message

# git push
# Sends local commits to a remote repository on GitHub
# Requires linking with git remote add origin <repo-url>

# git pull
# Fetches changes from GitHub and merges them with your local repository

# git branch
# Lists all branches or creates a new branch for development

# git checkout <branch>
# Switches between branches

# git merge <branch>
# Merges another branch into the current branch.