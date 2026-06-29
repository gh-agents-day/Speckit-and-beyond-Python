# Exercise CLI — Full Workflow from the Command Line

> **Goal:** Complete the entire spec-driven development workflow using only the terminal and Spec Kit CLI — no IDE required.

---

> **Note for participants:** This exercise consolidates all five workshop exercises into a single CLI-based flow. If you prefer working in the terminal or are not familiar with VS Code, follow this guide instead. You will achieve the same outcome — analysing the codebase, defining a constitution and specification, planning, generating tasks, and implementing the three features.

---

## Prerequisites

- Git, Python 3.11+, and pip installed
- A terminal (PowerShell, bash, or zsh)
- GitHub Copilot CLI (`gh copilot`) **or** access to the GitHub Copilot Chat via [github.com](https://github.com) (for the analysis step)

---

## Step 0 — Clone and Run the App

```bash
git clone https://github.com/gh-agents-day/Speckit-and-beyond-Python.git
cd Speckit-and-beyond-Python
pip install -r requirements.txt
python run.py
```

Open [http://localhost:8080](http://localhost:8080) in your browser. Explore the current state:

- Create a task — notice there is no Priority field
- Look at the task table — no Priority column, no search bar, no filter dropdowns
- Try editing a task — same gaps in the form

Keep the app running (or stop it for now — you'll restart it at the end).

---

## Step 1 — Analyse the Codebase (Exercise 1)

In Exercise 1, IDE users create a custom agent.

**Option A — Create a custom agent in the Copilot CLI:**

GitHub Copilot CLI supports custom agents. You can create one directly from the terminal:

1. Run `gh copilot` to start an interactive session
2. Use the `/agent` command to open the agent selector
3. Choose **"Create new agent..."** from the menu
4. When prompted _"Where should the agent be created?"_, select **Project (.github/agents/)** so the agent is stored in the repository and available to all contributors
5. When prompted _"How would you like to create your agent?"_, select **Create manually**
6. When prompted for _"Agent name"_, enter `codebase-analyser` and press Enter
7. When prompted for _"Agent description"_, enter:
   ```
   Analyses any codebase and produces a structured gap report based on the features the user wants to build.
   ```
   Press Enter to continue.
8. When prompted for _"Custom instructions (optional)"_, enter:

   ```
   You are a senior software engineer performing a codebase gap analysis.

   When the user describes a set of features they want to build, you will:
   1. Explore the project structure to identify the key layers (model, repository, service, routes, and frontend if present)
   2. Read the relevant source files in each layer
   3. For each layer, determine what is currently implemented and what is missing to support the requested features
   4. Output a structured gap summary as a markdown table with columns: Layer | What Exists | What Is Missing

   One row per layer. Do not output prose — only the table.
   ```

9. When prompted _"Which tools should this agent have access to?"_, select **Select by category...**. In the category list, navigate to **Read files** using the arrow keys and press Enter to create the agent.

   The CLI creates `.github/agents/codebase-analyser.agent.md` with your name, description, instructions, and tool configuration.

10. Run `/agent` again to open the agent selector. You should now see **codebase-analyser** in the list. Select it, then send this prompt:

    ```
    I need to add three features to this project:
    1. Priority Support — a priority field (HIGH, MEDIUM, LOW) on tasks with full CRUD support
    2. Search Bar — keyword search across title, description, category, and assignee
    3. Status / Priority / Category Filters — dropdown filters on the task table

    Analyse the codebase and tell me what exists and what is missing for each of these features.
    ```

    The agent will read the codebase and produce a gap summary table in this format:

    | Layer | What Exists | What Is Missing |
    | ----- | ----------- | --------------- |
    | ...   | ...         | ...             |

    One row per layer (Model, Repository, Service, Routes, Frontend).

---

## Step 2 — Install Spec Kit (Exercise 2)

**Install `uv`:**

```bash
# Windows (PowerShell)
winget install astral-sh.uv

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify:

```bash
uv --version
```

**Install Spec Kit CLI:**

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

**Initialize Spec Kit in the project:**

```bash
cd Speckit-and-beyond-Python
specify init --here
```

When prompted:

- _"Warning: Current directory is not empty. Do you want to continue?"_ → type **y** and press Enter
- _"Choose your AI assistant"_ → navigate to **copilot (GitHub Copilot)** and press Enter
- Choose **PowerShell** (Windows) or **Bash** (macOS/Linux) as the script type

Verify the CLI commands are available:

```bash
specify --help
```

---

## Step 3 — Create the Constitution (Exercise 3, Part 1)

In the Copilot CLI session, type `@` followed by `.github/prompts/` to list all available prompt files. Select `speckit.constitution.prompt.md` using the arrow keys and press Enter. Then provide the following input:

```
Generate a constitution that captures the governing standards and principles for this application —
not for any specific feature, but as the lasting rules that all future development must follow. Cover:

1. Architecture — layered structure (model → repository → service → routes → UI);
   each layer has a single responsibility and must not bypass the one above it
2. Data Storage — data/tasks.json is the single source of truth; all reads and
   writes go through TaskRepository; no layer may access the file directly
3. Field Naming — field names in the Task model, the JSON store, the REST API
   response, and the UI must be identical; no aliasing or renaming between layers
4. Validation — all input validation and business rule enforcement happens in
   TaskService; routes do not validate; TaskRepository does not validate
5. Frontend Standards — the UI is a single-page vanilla JS app; data is fetched
   from the backend on each operation; only edit state (editingId) is held in memory;
   the page does not reload to reflect data changes
6. Code Quality — no business logic in routes; no file I/O outside the
   repository; no inline styles or scripts added to index.html outside its existing structure
```

---

## Step 4 — Create the Specification (Exercise 3, Part 2)

Type `@` followed by `.github/prompts/` and select `speckit.specify.prompt.md`. Then provide the following input:

```
Extend the TaskManager Flask app following the constitution:

1. Priority Support
   - Add a priority field (HIGH, MEDIUM, LOW) to the Task model
   - Persist and return priority in all CRUD operations
   - Show priority as a dropdown field in the create and edit form
   - Display the priority value as a column in the task table

2. Search Bar
   - Add keyword search support to the service layer with an optional search parameter
   - Search across title, description, category, and assignedTo fields (case-insensitive)
   - Frontend: a search input above the task table that filters results in real time

3. Status / Priority / Category Filters
   - Add filter support to the service layer with optional status, priority, and category parameters
   - Filters can be combined with each other and with search
   - Frontend: three dropdown controls above the task table

UI layout: the search bar and all three filter dropdowns (Status, Priority, Category)
must appear on a single row above the task table.
```

**Optional — Clarify ambiguities:** Type `@` followed by `.github/prompts/` and select `speckit.clarify.prompt.md`.

---

## Step 5 — Create the Plan (Exercise 4, Part 1)

Type `@` followed by `.github/prompts/` and select `speckit.plan.prompt.md`. Then provide the following input:

```
Create a technical implementation plan for adding priority support, search, and filters to the TaskManager Flask application.

Detail:
- Implementation sequence across layers (model → repository → service → routes → UI)
- How each feature should be phased to keep the app functional throughout
- Testing strategy for the service layer changes
- How search and filter query parameters interact with each other
```

---

## Step 6 — Generate Tasks (Exercise 4, Part 2)

Type `@` followed by `.github/prompts/` and select `speckit.tasks.prompt.md`. Then provide the following input:

```
Generate actionable implementation tasks from the plan.
For each feature phase include:
- Clear task description
- Acceptance criteria
- Dependencies on other tasks

Order by: Priority Support first (it unblocks the filter feature), then Search, then Filters.
```

**Optional — Analyse consistency across all artifacts:** Type `@` followed by `.github/prompts/` and select `speckit.analyze.prompt.md`.

---

## Step 7 — Implement (Exercise 5)

Type `@` followed by `.github/prompts/` and select `speckit.implement.prompt.md`. Then provide the following input:

```
Implement all tasks from tasks.md following the specification and plan:
- Phase 1: Priority Support — priority field across model, service, routes, and UI
- Phase 2: Search — keyword search across the backend and frontend
- Phase 3: Filters — status, priority, and category filters across the backend and frontend

UI layout: the search bar and all three filter dropdowns (Status, Priority, Category)
must appear on a single row above the task table. Use flex-wrap: nowrap so they
never stack vertically.

All existing CRUD operations must continue to work.
```

---

## Step 8 — Verify

Restart the app and test all three features:

```bash
python run.py
```

Open [http://localhost:8080](http://localhost:8080) and verify:

| Feature              | What to Check                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------ |
| **Priority Support** | Priority dropdown appears in create/edit form; Priority column visible in the task table               |
| **Search**           | Type a keyword in the search box — table filters in real time; clear it — all tasks reappear           |
| **Filters**          | Select a status — only matching tasks appear; combine filters — results narrow; combine with search — both apply |

---

## Quick Reference — Prompt Files

> **How to use:** In the Copilot CLI, type `@` followed by `.github/prompts/` to list all available prompt files. Use the arrow keys to select the one you want and press Enter. Then provide your instructions as the message.

| Prompt File                      | Output File                  |
| -------------------------------- | ---------------------------- |
| `speckit.constitution.prompt.md` | `.specify/constitution.md`   |
| `speckit.specify.prompt.md`      | `.specify/specification.md`  |
| `speckit.clarify.prompt.md`      | Refines `specification.md`   |
| `speckit.plan.prompt.md`         | `.specify/plan.md`           |
| `speckit.tasks.prompt.md`        | `.specify/tasks.md`          |
| `speckit.analyze.prompt.md`      | Consistency report           |
| `speckit.implement.prompt.md`    | Code changes across codebase |

---

## What You Did

| Item                      | Description                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------ |
| **Codebase Analysis**     | Reviewed the codebase and identified gaps across all layers.                         |
| **Spec Kit Installation** | Installed and initialized Spec Kit from the command line.                            |
| **Constitution**          | Defined governing principles that all implementation must follow.                    |
| **Specification**         | Created a detailed spec for priority support, search, and filters.                   |
| **Plan & Tasks**          | Generated a phased implementation plan and actionable task backlog.                  |
| **Implementation**        | Used Spec Kit to generate code changes across model, service, routes, and frontend.  |
| **Verification**          | Confirmed all three features work correctly in the browser.                          |

---

_This exercise covers the complete workflow. For the IDE-based version with step-by-step detail, see [Exercise 1](exercise-1.md) through [Exercise 5](exercise-5.md)._
