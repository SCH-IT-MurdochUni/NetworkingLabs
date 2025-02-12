This lab will introduce you to Github. Before starting, ensure you have the following:

*A Linux-based system (Ubuntu, Fedora, etc.)
*Terminal access
*A GitHub account (Sign up here if you don't have one)
*Basic knowledge of using the terminal

## Installing git

```
sudo apt update
sudo apt install git
```

Verify Installation:
After installation, verify that Git is installed correctly by checking its version:

BASH
git --version
Expected Output:

TEXT
git version 2.x.x
🛠 Step 2: Configure Git
Set up your Git configuration with your name and email. These details will appear in your commit messages.

BASH
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
Verify Configuration:

BASH
git config --list
Expected Output:

TEXT
user.name=Your Name
user.email=your.email@example.com
...
🔑 Step 3: Generate SSH Key (Optional but Recommended)
Using SSH keys allows for secure communication between your local machine and GitHub without repeatedly entering your credentials.

Check for Existing SSH Keys:
BASH
ls -al ~/.ssh
Look for files named id_rsa and id_rsa.pub or similar.

Generate a New SSH Key:
If you don't have an SSH key, generate one:

BASH
ssh-keygen -t ed25519 -C "your.email@example.com"
If your system doesn't support Ed25519, use RSA:

BASH
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
Follow the prompts:

Enter file in which to save the key: Press Enter to accept the default location.
Enter passphrase: (Optional) Add a passphrase for added security or press Enter for none.
Add SSH Key to SSH-Agent:
Start the SSH agent in the background:

BASH
eval "$(ssh-agent -s)"
Add your SSH private key to the agent:

BASH
ssh-add ~/.ssh/id_ed25519
Replace id_ed25519 with your key filename if different.

Add SSH Key to GitHub:
Copy the SSH Key to Clipboard:

BASH
cat ~/.ssh/id_ed25519.pub
Select and copy the output.

Add to GitHub:

Log in to your GitHub account.
Go to Settings > SSH and GPG keys > New SSH key.
Title: Enter a descriptive name (e.g., "Linux Laptop").
Key: Paste the copied SSH key.
Click Add SSH key.
Test SSH Connection:
BASH
ssh -T git@github.com
Expected Output:

TEXT
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
📁 Step 4: Create a GitHub Repository
Log in to GitHub and click the + icon in the top-right corner, then select New repository.

Fill in Repository Details:

Repository name: my-first-repo
Description: (Optional) e.g., "This is my first repository."
Privacy: Choose between Public or Private.
Initialize: Do not check "Initialize this repository with a README" since we'll do it via CLI.
Click Create repository.

🖥 Step 5: Clone the Repository to Your Local Machine
Navigate to the directory where you want to store your project.

BASH
cd ~/projects
If the projects directory doesn't exist, create it:

BASH
mkdir ~/projects
cd ~/projects
Clone Using SSH:
BASH
git clone git@github.com:your-username/my-first-repo.git
Or Clone Using HTTPS:
If you chose not to set up SSH.

BASH
git clone https://github.com/your-username/my-first-repo.git
Navigate into the repository:

BASH
cd my-first-repo
✏️ Step 6: Make Changes, Commit, and Push to GitHub
1. Create a New File:
Create a simple README file.

BASH
echo "# My First Repository" > README.md
2. Check Repository Status:
BASH
git status
Expected Output:

TEXT
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
3. Add Files to Staging Area:
BASH
git add README.md
Alternatively, add all changes:

BASH
git add .
4. Commit the Changes:
BASH
git commit -m "Add README.md"
Expected Output:

TEXT
[main (root-commit) abcdefg] Add README.md
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
5. Push Changes to GitHub:
BASH
git push origin main
If your default branch is master, replace main with master.

If using HTTPS, you might be prompted for your GitHub username and password or a personal access token.

Expected Output:

TEXT
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 245 bytes | 245.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:your-username/my-first-repo.git
 * [new branch]      main -> main
🔍 Step 7: Verify Changes on GitHub
Go to your repository on GitHub: https://github.com/your-username/my-first-repo

You should see the README.md file with the content # My First Repository.

📂 Additional Commands and Tips
1. Checking Status and History:
Check Status:

BASH
git status
View Commit History:

BASH
git log
Press q to exit the log view.

2. Creating and Switching Branches:
Create a New Branch:

BASH
git branch feature-branch
Switch to the New Branch:

BASH
git checkout feature-branch
Or combine both:

BASH
git checkout -b feature-branch
3. Merging Branches:
Switch to main Branch:

BASH
git checkout main
Merge Changes:

BASH
git merge feature-branch
4. Pulling Updates:
If collaborating, always pull the latest changes before pushing.

BASH
git pull origin main
5. Cloning Another Repository:
BASH
git clone git@github.com:another-user/another-repo.git
🧪 Practice Exercise
To reinforce your learning, try the following exercise:

Create a new repository on GitHub named test-repo-cli.
Clone the repository to your local machine.
Create a new file called hello.txt with the content Hello, GitHub CLI!.
Add, commit, and push the changes to GitHub.
Verify that hello.txt appears in your GitHub repository.
📚 Additional Resources
Git Official Documentation
GitHub Guides
Atlassian Git Tutorials
Pro Git Book
🎉 Congratulations!
You've successfully completed a basic GitHub lab using the CLI on Linux. You now have a foundational understanding of:

Installing and configuring Git
Creating and cloning repositories
Making commits and pushing changes to GitHub
Continue practicing these commands and explore more advanced Git features to enhance your version control skills!

Need Further Assistance?

If you encounter any issues or have questions, consider visiting:

GitHub Community Forums
Stack Overflow Git Tag
[Your Linux Distribution’s Support Channels]
Happy coding!
