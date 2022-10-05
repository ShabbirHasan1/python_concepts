# What is Git
## Git is a de facto standard
Versioning allows you to keep track of your software at the source level. 
You can track changes, revert to previous stages, and branch to create alternate versions of files and directories.
Many software projects’ files are maintained in Git repositories, and platforms like GitHub, GitLab, and Bitbucket help
 to facilitate software development project sharing and collaboration.
# Install Git

# Getting Started
## Setting up a repository
### Converting an existing project into a workspace environment
You can initialize a Git repository in an existing directory by using the git init command.
```
$ git init
```
Next, you’ll need to use the git add command in order to allow your existing files to be tracked by Git. For the most part, 
Git will never track new files automatically, so git add is a necessary step when adding new content to a repository that 
Git has not previously tracked.
```
$ git add .
```
### Creating a commit message
Each time you commit changes to a Git repository, you’ll need to provide a commit message.
Commit messages summarize the changes that you’ve made. Commit messages can never be empty, but can be any length.
If you are importing an existing project to Git for the first time, it’s typical to just use a message like “Initial Commit”.
 You can create a commit with the git commit command:
 ```
$ git commit -m "Initial Commit" -a
```
There are two important parameters of the above command. 
The first is -m, which signifies that your commit message (in this case “Initial Commit”) is going to follow. Secondly, 
the -a signifies that your commit should include all added or modified files. Git does not treat this as the default behavior, but when working with Git in the future, you may default to including all updated files in your future commits most of the time.

In order to commit a single file or a few files, you could have used:
 ```
$ git commit -m "Initial Commit" file1 file2
```
### Pushing changes to a remote server

## Push a branch

# Collaborating
## Making pull request
## Using Branches
### Viewing branches
Prior to creating new branches, we want to see all the branches that exist.
We can view all existing branches by typing the following:
 ```
$ git branch -a
```
Additonal tips
# Merging vs Rebasing

# Learn More