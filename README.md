# Python Enterprise Control Systems

This repository contains a set of **enterprise-style Python systems** designed at the **control and reliability layer** of software systems.

Instead of building UI-heavy applications or CRUD projects, this repository focuses on how **real-world backend systems govern behavior, handle failures, and evaluate decision reliability**.

---

## 🧠 What This Project Is About

Most beginner projects answer:
> “What does the system do?”

This project answers:
- **Is this action allowed?** (Governance)
- **What happens when things fail?** (Reliability)
- **How confident can we be in a decision?** (Risk & uncertainty)

These are the problems solved inside **real IT and backend teams**.

---

## 🏗️ System Architecture Overview

The repository consists of **three tightly related modules**:

┌───────────────────────────────┐
│ Decision Confidence Engine │
│ (Risk & reliability scoring) │
├───────────────────────────────┤
│ Policy Engine │
│ (Rule-based governance) │
├───────────────────────────────┤
│ Task Orchestrator │
│ (Failure-aware execution) │
└───────────────────────────────┘

Each module can work independently but together form a **complete enterprise control system**.

---

## 📦 Modules

### 1️⃣ Policy Engine (Governance & Audit)
- Config-driven rule evaluation (JSON-based policies)
- Priority-based conflict resolution
- Explainable ALLOW / DENY decisions
- Full audit trail of every decision

📁 Folder: `policy_engine/`

---

### 2️⃣ Task Orchestrator (Reliability Engineering)
- Explicit task lifecycle modeling
- Failure-aware scheduling
- Retry and quarantine logic
- Separation of execution and failure handling

📁 Folder: `task_orchestrator/`

---

### 3️⃣ Decision Confidence Engine (Risk & Uncertainty)
- Data quality evaluation
- Risk analysis based on failure metrics
- Confidence scoring with explanations
- Decision reliability quantification

📁 Folder: `decision_confidence/`

---

## ▶️ How to Run the Demos

Each module includes a runnable demo file.

### Run Policy Engine
```bash
python policy_engine/run_policy_engine.py

