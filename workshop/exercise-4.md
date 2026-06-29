# Exercise 4: Spec Kit — Plan & Tasks

> **Time:** ~7 minutes
> **Prerequisite:** `constitution.md` and `specification.md` created ([Exercise 3](exercise-3.md))
> **Track:** Required for Exercise 5

---

> **Note for participants:** This exercise depends on the outputs of Exercise 3. The `plan.md` and `tasks.md` files generated here are used directly during implementation in Exercise 5.

> **Prefer the command line?** If you'd rather work entirely from the terminal without an IDE, see [Exercise CLI — Full Workflow from the Command Line](exercise-cli.md) which consolidates all exercises into a single CLI-based guide.

---

## Goal

Create a technical plan for how the three features will be implemented across the stack, then break it into concrete, trackable tasks.

---

## Context

The specification defines **what** to build. This exercise creates:

- `plan.md` — **how** to build it (implementation sequence, layer-by-layer approach, testing strategy)
- `tasks.md` — the actionable backlog with clear acceptance criteria

---

## Steps

**1.** In Copilot Chat, run:

```
/speckit.plan

Create a technical implementation plan for priority support, search, and filters in this Flask app:

- Layer sequence: model → repository → service → routes → UI

- Each phase must keep the app functional

- How search and filter query params interact

- Testing strategy for service layer changes
```

> Spec Kit creates `.specify/plan.md`.

---

**2.** Review `plan.md`. It should outline a phased approach — model changes first, then backend, then frontend — so the app remains functional at each step.

---

**3.** In Copilot Chat, run:

```
/speckit.tasks

Generate implementation tasks from the plan. For each task include:
- Exact file path
- Specific change required
- Acceptance criteria
- Dependencies

Order: Priority Support first (unblocks filters), then Search, then Filters. Mark tasks touching different files as parallelisable.
```

> Spec Kit creates `.specify/tasks.md`.

---

**4.** Review `tasks.md`. This is your implementation backlog for Exercise 5.

---

> **Optional:** Before moving to Exercise 5, run `/speckit.analyze` to check consistency and coverage across all your Spec Kit artifacts — constitution, specification, plan, and tasks.
>
> ```
> /speckit.analyze
> ```
>
> Spec Kit will flag any gaps or contradictions — for example, a task that references a field not defined in the specification, or a planned endpoint missing from the task list. Resolve any issues before implementing.

---

## Expected Output

`plan.md` should contain five sections:

- **Summary** — one paragraph describing the overall implementation approach and which layers are touched
- **Technical Context** — the confirmed tech stack (language, dependencies, storage, constraints, platform)
- **Constitution Check** — a table verifying each governing principle passes before implementation begins
- **Project Structure** — a file tree showing exactly which source files are changed and what change is made in each
- **Complexity Tracking** — any constitution violations that needed justification (none expected for this feature)

`tasks.md` should contain tasks grouped by user story across five phases: a foundational model change, Priority Support (US1), Keyword Search (US2), Filters (US3), and a final polish phase. Each task should reference the exact file path, describe the specific change, and state what done looks like. Tasks that touch different files should be marked as parallelisable (`[P]`).

> Your output will vary based on how Spec Kit interprets your specification. That's expected — focus on whether the tasks are actionable, the file paths are specific, and the acceptance criteria are testable.

---

## What You Did

| Item                | Description                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| **Plan Creation**   | Created a technical plan outlining the implementation sequence and testing strategy across all layers.  |
| **Task Generation** | Generated a detailed backlog of implementation tasks with acceptance criteria ready for Exercise 5.     |

---

_Next: [Exercise 5 →](exercise-5.md)_
