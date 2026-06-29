# Exercise 3: Spec Kit — Constitution & Specification

> **Time:** ~8 minutes
> **Prerequisite:** Spec Kit installed and initialized ([Exercise 2](exercise-2.md))
> **Track:** Required for Exercises 4 and 5

---

> **Note for participants:** This exercise builds on Exercise 2 and is required before you can do Exercises 4 and 5. The outputs (`constitution.md` and `specification.md`) are referenced in the planning and implementation steps.

> **Prefer the command line?** If you'd rather work entirely from the terminal without an IDE, see [Exercise CLI — Full Workflow from the Command Line](exercise-cli.md) which consolidates all exercises into a single CLI-based guide.

---

## Goal

Define the governing principles for the feature sprint (constitution), then generate a detailed specification of what will be built across the full stack.

---

## Context

The TaskManager app needs three new features added across all layers:

| Feature                                  | Scope                                                      |
| ---------------------------------------- | ---------------------------------------------------------- |
| **Priority Support**                     | `Task` model, repository, service, routes, and UI form     |
| **Search Bar**                           | Backend keyword search + frontend real-time filter         |
| **Status / Priority / Category Filters** | Backend query params + frontend dropdown controls          |

---

## Steps

**1.** Open Copilot Chat and run:

```
/speckit.constitution

Define governing standards for this application — not for any specific feature, but as lasting rules all future development must follow:

1. Architecture — model → repository → service → routes; each layer has a single responsibility; no layer bypasses the one above it.

2. Data Storage — data/tasks.json is the single source of truth; all reads/writes go through TaskRepository only.

3. Field Naming — field names must be identical across model, JSON store, REST API, and UI; no aliasing between layers.

4. Validation — all validation and business rules live in TaskService only; routes and repository do not validate.

5. Frontend — single-page vanilla JS; data fetched from backend per operation; only editingId held in memory; no page reloads.

6. Code Quality — no business logic in routes; no file I/O outside repository; no inline styles/scripts outside existing index.html structure
```

> Spec Kit creates `.specify/constitution.md`.

---

**2.** Review `constitution.md`. It should define clear principles that every implementation decision in Exercises 4 and 5 must follow.

---

**3.** In Copilot Chat, run:

```
/speckit.specify

Extend the TaskManager Flask app per the constitution:

1. Priority Support — add priority field (HIGH/MEDIUM/LOW) to Task model; persist and return in all CRUD; show as dropdown in create/edit form; display as table column.

2. Search Bar — optional search param in service layer; case-insensitive match across title, description, category, assignedTo; real-time filter input above task table.

3. Filters — optional status, priority, category params in service layer; combinable with each other and with search; three dropdowns above task table
```

> Spec Kit creates `.specify/specification.md`.

---

**4.** Review `specification.md`. It defines **what** will be built — fields, backend methods, UI components, and success criteria.

---

> **Optional:** Before moving to Exercise 4, you can run `/speckit.clarify` to let Spec Kit identify any underspecified or ambiguous areas in your specification. This is useful if you want to tighten the spec before planning begins.
>
> ```
> /speckit.clarify
> ```
>
> Spec Kit will ask questions about anything unclear — for example, whether the priority field should have a default value, or how the search and filters should behave when combined. Answer them to refine `specification.md` before proceeding.

---

## Expected Output

`constitution.md` should capture the application's governing principles — architecture boundaries, data access rules, validation ownership, and frontend standards. Expect 5–7 principles, each clearly stating what is required and why.

`specification.md` should describe each feature in terms of what changes at each layer — model fields, backend methods, and UI components — along with success criteria that can be verified without running implementation code.

> Your output will vary based on how Spec Kit interprets your inputs. That's expected — focus on whether the principles are enforceable and the success criteria are measurable.

---

## What You Did

| Item              | Description                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| **Constitution**  | Defined the core principles guiding the feature implementation.                                |
| **Specification** | Created a detailed spec outlining the fields, endpoints, UI components, and success criteria.  |

---

_Next: [Exercise 4 →](exercise-4.md)_
