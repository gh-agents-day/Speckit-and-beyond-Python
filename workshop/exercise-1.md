# Exercise 1 — Analyse the Codebase & Identify Gaps

> **Goal:** Create a GitHub Copilot agent that analyses the TaskManager codebase and generates a gap summary for the three features you need to build.

> **Prefer the command line?** If you'd rather work entirely from the terminal without an IDE, see [Exercise CLI — Full Workflow from the Command Line](exercise-cli.md) which consolidates all exercises into a single CLI-based guide.

---

## Context

The TaskManager Flask application is live and supports basic task CRUD operations. Rather than manually reviewing every file, you'll create a custom Copilot agent that does the analysis for you — reading the codebase, understanding its current state, and producing a structured gap report.

The three features the team needs:

1. **Priority Support** — tasks need a `priority` field (`HIGH`, `MEDIUM`, `LOW`) visible in the UI and editable via create/edit forms
2. **Search Bar** — a keyword search that filters tasks across title, description, category, and assignee in real time
3. **Status / Priority / Category Filters** — dropdown filters that narrow the task table independently or in combination

---

## Step 0 — Run the App

Before analysing the code, run the application so you can see the current state of the UI firsthand.

```bash
pip install -r requirements.txt
python run.py
```

Open [http://localhost:8080](http://localhost:8080) in your browser and explore what's already there:

- Create a task — notice there is no Priority field
- Look at the task table — no Priority column, no search bar, no filter dropdowns
- Try editing a task — same gaps in the form

This is the baseline you're about to improve. Keep the app running as you work through the exercises.

---

## Step 1 — Create the Codebase Analyser Agent

### First option:

1. Click on "**Open Customizations**" on the top right copilot chat panel
2. Click on dropdown "**Create New Agent**" and select "**New Agent(Workspace)**" to create the agent file in the current workspace
3. Name your agent "Codebase Analyser" the file path at which it gets created is `.github/agents/codebase-analyser.agent.md`
4. In the file `codebase-analyser.agent.md` click on "**ctrl+i**" to open the inline chat and ask copilot to generate the content based on the instructions below.
5. Paste the following content into the agent file:

   ```
   ---
   name: Codebase Analyser
   description: Analyses a codebase and produces a structured gap report for requested features.
   tools: [read, search]
   ---

   You are a senior software engineer performing a gap analysis.
   Given a list of features to build:
   1. Explore the project structure (model, repository, service, routes/app, frontend)
   2. Read the relevant source files in each layer
   3. Return only a markdown table — no prose:
   | Layer | What Exists | What Is Missing |
   | ----- | ----------- | --------------- |
   One row per layer. Ask for features if not provided.
   ```

### Second option:
   Create the file using the copilot chat

1. Open **Copilot Chat** in VS Code
2. Type `/create-agent` and send the following as your prompt:

   ```
   Create a custom agent at .github/agents/codebase-analyser.agent.md:

   ---
   name: Codebase Analyser
   description: Analyses a codebase and produces a structured gap report for requested features.
   tools: [read, search]
   ---

   You are a senior software engineer performing a gap analysis.
   Given a list of features to build:
   1. Explore the project structure (model, repository, service, routes/app, frontend)
   2. Read the relevant source files in each layer
   3. Return only a markdown table — no prose:
   | Layer | What Exists | What Is Missing |
   | ----- | ----------- | --------------- |
   One row per layer. Ask for features if not provided.
   ```

3. Review and accept the generated file.

---

## Step 2 — Run the Agent

1. Open **Copilot Chat** in VS Code
2. Click the **Agent** dropdown at the bottom of the chat input (it says "Agent" by default) and select **Codebase Analyser** from the list of custom agents
3. Send the following message:

```
Analyse the codebase for:

1. Priority (HIGH/MEDIUM/LOW) with full CRUD  
2. Search across title, description, category, assignee  
3. Status/Priority/Category combined filters  

Return ONLY the gap summary table.
```

4. Review the output. The agent will read each file and return a structured gap summary.

---

## Step 3 — Validate the Output

The agent's gap summary should identify the following missing pieces. Use this as a checklist to confirm the agent found them all:

| Layer          | What Is Missing                                                      |
| -------------- | -------------------------------------------------------------------- |
| **Model**      | `priority` field                                                     |
| **Repository** | Search and filter query methods                                      |
| **Service**    | Priority handling, search and filter logic                           |
| **Routes**     | Query param endpoints (`?search=`, `?priority=`, `?status=`)         |
| **Frontend**   | Priority field in form, search bar, filter dropdowns                 |

> If the agent misses any of the above, refine the instructions in `codebase-analyser.agent.md` and re-run.

---

## Done?

You have a clear, agent-generated picture of the gaps. Head to [Exercise 2 — Spec Kit Setup](exercise-2.md) to install and configure Spec Kit so you can turn these gaps into a governed specification.

---

_Next: [Exercise 2 →](exercise-2.md)_
