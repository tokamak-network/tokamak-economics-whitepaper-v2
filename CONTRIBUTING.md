# Contributing Guide (Feedback via GitHub Issues)

Thanks for helping improve this proposal. This repository publishes a **Discussion Draft** (not an official replacement). We collect feedback via GitHub Issues and incorporate it into versioned releases.

---

## 1. Scope & Positioning
- This document is a **meaningful proposal / discussion draft**.
- Official adoption (if any) is a separate step and may require additional review (legal, exchange comms, official docs updates).

---

## 2. Where to Leave Feedback
Please open a **GitHub Issue** using the appropriate template:
- Doc feedback / clarification
- Model / assumptions / math
- Parameters / ranges / tuning
- Simulator / reproducibility / results
- Token-holder-facing notes

**Single feedback hub:** GitHub Issues (this repo)

---

## 3. Expected Handling Time (SLA)
Assuming no major/security-critical problems:

### Standard Issues
- **Acknowledgement:** within **24 hours**
- **Triage:** within **2 business days**
- **First response:** within **5 business days**
- **Resolution / merge / close:**
  - Simple doc fixes: **~10 business days**
  - Typical model/param/sim updates: **~15 business days**
  - Experiment-heavy or sensitivity analysis: **~20 business days**

### Critical Issues (Economic attack / severe vulnerability / fatal inconsistency)
If you believe the issue is critical, label it as **prio:P0-critical** (or state "CRITICAL" in the title).
- **Acknowledgement:** within **6 hours**
- **Initial mitigation / guidance:** within **24 hours**
- **Target fix window:** **72 hours – 1 week**, depending on complexity

> Note: These are targets, not guarantees. We will always update the issue with current status and next steps.

---

## 4. How We Triage Issues
We apply:
- `type:*` (doc/model/param/sim/attack/tokenholder/question)
- `prio:*` (P0–P3)
- `status:*` (needs-info/triaged/in-progress/waiting-review/resolved)

We may request additional info. If we mark `status:needs-info` and there is no response for **7 days**, we may close the issue as incomplete.

---

## 5. Versioning Policy
This repository uses:
- `v0.x` = Discussion Draft releases
- `v0.9` = Candidate release (internally aligned, ready for adoption decision)
- `v1.0` = Official adoption release (only if/when adopted via official channels)

**Increment rule**
- `v0.(x+1)` for regular feedback-driven updates.
- Major conceptual changes may “jump” minor versions (e.g., `v0.3 -> v0.5`) with clear changelog notes.

---

## 6. Making Changes (PR Workflow)
### Branch naming (recommended)
- `doc/issue-123-...`
- `model/issue-123-...`
- `param/issue-123-...`
- `sim/issue-123-...`
- `tokenholder/issue-123-...`

### Pull Requests
- Create a PR and link issues via:
  - `Closes #123` (auto-closes when merged) or `Refs #123` (references)
- Include:
  - What changed and why
  - Which sections/files are affected
  - If simulator results changed: reproduction steps + output artifacts

### Minimal Review Rules
- Doc-only changes: 1 reviewer
- Model/parameter changes: 1–2 reviewers
- Simulator/result changes: at least 1 reviewer must confirm reproducibility

---

## 7. Release Process (Maintainers)
Each release must include:
- Updated PDF (and sources)
- Updated `CHANGELOG.md`
- Git tag + GitHub Release notes
- A short note in the issue(s) referencing the release version and links

---

## 8. Code of Conduct (Short)
Be constructive and respectful. We welcome strong critique if it is specific and backed by reasoning or data.

Thank you!
