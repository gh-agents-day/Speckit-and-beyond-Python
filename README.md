# Agent-Driven Spec Development: The TaskManager Feature Sprint

> **Product Demand:** Extend a working task manager with priority support, search, and advanced filtering — all driven by GitHub agents.

---

## The Scenario

Monday, 9:00 AM. The TaskManager app is live, but the team is swamped with feature requests.

Users need to prioritize tasks, search by keyword, and filter by status, priority, and category — or they're switching to a competitor.

Engineering Lead says: deliver all three features by end of sprint, with clean specs and no regressions.

This workshop walks you through exactly that — using GitHub's agent ecosystem to go from a bare-bones CRUD app to a fully-featured, production-ready task manager.

---

## What You'll Learn

| | |
|---|---|
| **Spec Kit** | Drive governance, planning, and code generation from a specification |
| **Custom Agent** | Create and configure your own agent to automate specialized workflows and tasks |

---

## Prerequisites

- Python 3.11+ installed
- pip available
- Valid GitHub Copilot subscription (Individual, Business, or Enterprise)
- [VS Code](https://code.visualstudio.com/download) with GitHub Copilot Chat extension
- [Git CLI](https://git-scm.com/install/) for version control
- [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli) installed — requires Node.js 22+ (install via `npm install -g @github/copilot`), or use [WinGet](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows) / [Homebrew](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux) for platform-specific options
- [Speckit](https://github.com/github/spec-kit?tab=readme-ov-file#-get-started) installed and configured
- [UV](https://docs.astral.sh/uv/getting-started/installation/) (for installing Spec Kit)

> **Starter Code Provided:** TaskManager Flask brownfield application — a working but feature-incomplete task management system ready for your enhancements

---

## Workshop Structure

| | Exercise | Description | Time |
|---|---|---|---|
| 1 | Exercise 1 | Analyse the Codebase & Identify Gaps | ~3 min |
| 2 | Exercise 2 | Spec Kit Setup | ~5 min |
| 3 | Exercise 3 | Constitution & Specification | ~8 min |
| 4 | Exercise 4 | Plan & Tasks | ~7 min |
| 5 | Exercise 5 | Implement All Three Features | ~10 min |
| — | **Total** | | **~33 min** |

> Prefer the CLI? [Exercise CLI](workshop/exercise-cli.md) consolidates all five exercises into a single Copilot CLI-based flow using `@.github/prompts/` prompt files — no IDE required.

---

## Features You'll Build

| | |
|---|---|
| **Priority Support** | Add HIGH, MEDIUM, LOW priority to tasks with full CRUD support |
| **Search Bar** | Keyword search across title, description, category, and assignee |
| **Status Filter** | Filter the task table by TODO, IN_PROGRESS, DONE, CANCELLED |
| **Priority Filter** | Filter tasks by priority level |
| **Category Filter** | Filter tasks by category |

> The workshop has been tested with the following AI models on GitHub Copilot: `Claude Sonnet 4.6`, `GPT-4.1`. Results may vary with different models. If you encounter issues, try switching to one of these models in your Copilot settings.

---

## Get Started

Once your repo is created and cloned, install dependencies and run the app:

```bash
pip install -r requirements.txt
python run.py
```

Then open [http://localhost:8080](http://localhost:8080) to see the current state of the application, and start here: [Exercise 1 — Analyse the Codebase](workshop/exercise-1.md)

---

## Resources

- [Spec Kit Documentation](https://github.github.io/spec-kit/)
- [GitHub Repository](https://github.com/github/spec-kit)
- [Video Overview](https://www.youtube.com/watch?v=a9eR1xsfvHg)
