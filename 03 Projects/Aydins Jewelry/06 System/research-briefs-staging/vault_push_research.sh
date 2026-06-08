#!/bin/bash
# vault_push_research.sh — Commits and pushes new research briefs from VPS to GitHub.
# Runs after agent_research_loop.py at 5am CT (10 UTC during CDT).
# So Amir's local Obsidian vault pulls the briefs on its next sync cycle.
#
# Deploy to: /home/openclaw/.openclaw/command-center/scripts/vault_push_research.sh
# Cron entry: 0 10 * * * /home/openclaw/.openclaw/command-center/scripts/cron_run.sh vault-push-research /home/openclaw/.openclaw/command-center/scripts/vault_push_research.sh >> /home/openclaw/.openclaw/command-center/work/vault-push-research.log 2>&1

set -e
cd /home/openclaw/vault

ts=$(date -u +%FT%TZ)

# Pull latest to avoid divergence with Amir's local pushes
git pull --rebase origin main 2>&1 | tail -5

# Only stage research briefs and learnings
git add brands/aydins/research/

# Check if there's anything to commit
if git diff --staged --quiet; then
  echo "[$ts] no research changes to push"
  exit 0
fi

# Count files
file_count=$(git diff --staged --name-only | wc -l)

# Commit + push
git commit -m "research briefs daily push: $ts ($file_count files)"
git push origin main 2>&1 | tail -5

echo "[$ts] pushed $file_count research file(s) to GitHub"
