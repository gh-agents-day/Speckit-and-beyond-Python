# Exercise 2: Spec Kit Setup

> **Time:** ~5 minutes
> **Standalone:** No prior exercises needed.
> **Track:** Required for Exercises 3, 4, and 5

---

> **Note for participants:** This is a required setup exercise. Exercises 3, 4, and 5 all depend on Spec Kit being installed. Complete this before moving to any of those exercises.

> **Prefer the command line?** If you'd rather work entirely from the terminal without an IDE, see [Exercise CLI — Full Workflow from the Command Line](exercise-cli.md) which consolidates all exercises into a single CLI-based guide.

---

## Goal

Install the Spec Kit CLI and initialize it in the project so the `/speckit.*` slash commands are available in Copilot Chat

---

## Context

Spec Kit is a powerful tool for defining software specifications, creating implementation plans, and ensuring code quality. In this exercise, you'll set up Spec Kit in this project to prepare for the upcoming feature development work.

---

## Steps

**1.** Install `uv` (required to install Spec Kit) in a new terminal:

```bash
# Windows — run in PowerShell
winget install astral-sh.uv

# Windows — alternative (PowerShell, bypasses execution policy to allow the install script)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, you may need to restart your terminal or add `uv` to your PATH:

```powershell
# PowerShell
$env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
```

```cmd
# CMD
set Path=%USERPROFILE%\.local\bin;%Path%
```

Verify installation:

```bash
uv --version
```

---

**2.** Install Spec Kit:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

---

**3.** Initialize Spec Kit in the project:

```bash
specify init --here
```

When prompted _"Initialize Spec Kit in existing repository?"_, type **yes** to continue, choose **GitHub Copilot** as the AI Assistant and **PowerShell** as the script type.

---

**4.** Open Copilot Chat and type `/spec` to verify the commands appear:

**Essential commands for the Spec-Driven Development workflow:**

| Command                 | Description                                                            |
| ----------------------- | ---------------------------------------------------------------------- |
| `/speckit.constitution` | Create or update project governing principles and development guidelines |
| `/speckit.specify`      | Define what you want to build (requirements and user stories)          |
| `/speckit.plan`         | Create technical implementation plans with your chosen tech stack      |
| `/speckit.tasks`        | Generate actionable task lists for implementation                      |
| `/speckit.implement`    | Execute all tasks to build the feature according to the plan           |

**Optional Commands**

Additional commands for enhanced quality and validation:

| Command              | Description                                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `/speckit.clarify`   | Clarify underspecified areas (recommended before `/speckit.plan`)                                                   |
| `/speckit.analyze`   | Cross-artifact consistency & coverage analysis (run after `/speckit.tasks`, before `/speckit.implement`)            |
| `/speckit.checklist` | Generate custom quality checklists that validate requirements completeness, clarity, and consistency                |

---

## What You Did

| Item                       | Description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| **Spec Kit Installation**  | You installed the Spec Kit CLI using `uv`.                   |
| **Project Initialization** | You initialized Spec Kit in the project repository.          |
| **Slash Commands**         | The `/speckit.*` commands are now available in Copilot Chat. |

---

_Next: [Exercise 3 →](exercise-3.md)_
