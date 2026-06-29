# Exercise 5: Spec Kit — Implement

> **Time:** ~10 minutes
> **Prerequisite:** `plan.md` and `tasks.md` created ([Exercise 4](exercise-4.md))
> **Track:** Required

---

> **Prefer the command line?** If you'd rather work entirely from the terminal without an IDE, see [Exercise CLI — Full Workflow from the Command Line](exercise-cli.md) which consolidates all exercises into a single CLI-based guide.

---

## Goal

Use `/speckit.implement` to generate the code for all three features across the full stack — model, service, routes, and frontend — and verify the app works correctly.

---

## Context

You have a governed specification and a phased task list. Now you hand it to Spec Kit and let it implement the changes layer by layer, starting with Priority Support since it unblocks the filter feature.

---

## Steps

**1.** In Copilot Chat, run:

```
/speckit.implement

Implement all tasks from tasks.md:
- Phase 1: Priority Support — priority field across model, service, routes, UI
- Phase 2: Search — keyword search across backend and frontend
- Phase 3: Filters — status, priority, category filters across backend and frontend

UI constraint: search bar and all three filter dropdowns on one row; use flex-wrap: nowrap.
All existing CRUD operations must continue to work.
```

> Spec Kit generates changes across `model.py`, `service.py`, `app.py`, and `index.html`.

---

**2.** Restart the app and verify all three features:

```bash
python run.py
```

Open [http://localhost:8080](http://localhost:8080) and check:

- **Priority Support** — create a task and confirm the Priority dropdown appears in the form and a Priority column is visible in the table
- **Search** — type a keyword in the search box and confirm the table filters in real time; clear it and confirm all tasks reappear
- **Filters** — select a status from the Status filter and confirm only matching tasks appear; combine Status and Priority filters and confirm results narrow further; use search and a filter together and confirm both apply simultaneously

---

## What You Did

| Item                 | Description                                                                          |
| -------------------- | ------------------------------------------------------------------------------------ |
| **Priority Support** | Added `priority` field across model, service, routes, and UI.                        |
| **Search**           | Implemented keyword search in the service layer and wired it to the API and frontend.|
| **Filters**          | Implemented combinable status, priority, and category filters across the full stack. |

---

_You've completed the workshop!_
