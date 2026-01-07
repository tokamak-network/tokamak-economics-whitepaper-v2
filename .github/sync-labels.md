# GitHub Labels Sync Instructions

This repository uses labels defined in `.github/labels.yml` for issue management.

## Manual Setup (GitHub Web UI)

1. Go to your repository on GitHub
2. Navigate to **Issues** → **Labels**
3. Create the following labels manually:

### Type Labels
- `type:doc` - Documentation feedback (color: #0E8A16)
- `type:model` - Model/math issues (color: #1D76DB)
- `type:param` - Parameter proposals (color: #5319E7)
- `type:sim` - Simulator issues (color: #006B75)
- `type:attack` - Security/attack issues (color: #D93F0B)
- `type:tokenholder` - Token-holder feedback (color: #FBCA04)
- `type:question` - General questions (color: #C2E0C6)

### Priority Labels
- `prio:P0-critical` - Critical (color: #B60205)
- `prio:P1` - High priority (color: #D93F0B)
- `prio:P2` - Medium priority (color: #FBCA04)
- `prio:P3` - Low priority (color: #0E8A16)

### Status Labels
- `status:needs-info` - Needs info (color: #FBCA04)
- `status:triaged` - Triaged (color: #1D76DB)
- `status:in-progress` - In progress (color: #5319E7)
- `status:waiting-review` - Waiting review (color: #FBCA04)
- `status:resolved` - Resolved (color: #0E8A16)
- `status:wontfix` - Won't fix (color: #B60205)
- `status:duplicate` - Duplicate (color: #C2E0C6)

## Automated Setup (using github-label-sync)

Alternatively, you can use the `github-label-sync` tool:

```bash
# Install github-label-sync
npm install -g github-label-sync

# Sync labels (requires GITHUB_ACCESS_TOKEN environment variable)
github-label-sync --access-token $GITHUB_ACCESS_TOKEN \
  tokamak-network/tokamak-economics-whitepaper-v2 \
  .github/labels.yml
```

## GitHub Actions (Recommended)

You can set up a GitHub Action to automatically sync labels on push or manually trigger it.

