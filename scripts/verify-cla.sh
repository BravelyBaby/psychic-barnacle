#!/usr/bin/env bash
# verify-cla.sh
# Helper for maintainers: add the `cla/verified` label to a PR after manual verification.
# Usage: ./scripts/verify-cla.sh <pr-number>

set -euo pipefail

usage() {
  echo "Usage: $0 <pr-number> [repo]"
  echo "  <pr-number> - the number of the pull request to verify"
  echo "  [repo] - optional owner/repo (defaults to git origin)
Example: $0 42 BravelyBaby/psychic-barnacle"
}

if [ "$#" -lt 1 ]; then
  usage
  exit 2
fi

PR_NUMBER="$1"
REPO="${2:-}" 

if [ -z "$REPO" ]; then
  # derive repo from git remote
  if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    origin_url=$(git remote get-url origin 2>/dev/null || true)
    if [ -z "$origin_url" ]; then
      echo "Could not determine git remote 'origin'. Please pass owner/repo as second argument." >&2
      exit 2
    fi
    # support git@github.com:owner/repo.git and https://github.com/owner/repo.git
    if echo "$origin_url" | grep -qE "git@github.com:"; then
      REPO=$(echo "$origin_url" | sed -E 's#git@github.com:([^/]+/[^.]+)(.git)?#\1#')
    else
      REPO=$(echo "$origin_url" | sed -E 's#https?://[^/]+/([^/]+/[^.]+)(.git)?#\1#')
    fi
  else
    echo "Not a git repo and no repo argument provided." >&2
    exit 2
  fi
fi

echo "Using repo: $REPO"

# Ensure gh is available
if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI not found. Install GitHub CLI and authenticate (gh auth login)." >&2
  exit 2
fi

LABEL_NAME="cla/verified"

echo "Ensuring label exists..."
if ! gh label view "$LABEL_NAME" --repo "$REPO" >/dev/null 2>&1; then
  echo "Label $LABEL_NAME not found; creating it."
  gh label create "$LABEL_NAME" --color 0e8a16 --description "CLA verified by maintainer" --repo "$REPO"
fi

echo "Adding label $LABEL_NAME to PR #$PR_NUMBER..."
gh pr edit "$PR_NUMBER" --add-label "$LABEL_NAME" --repo "$REPO"

echo "Label added. Consider leaving a comment documenting verification." 
echo "(You can remove the label with: gh pr edit $PR_NUMBER --remove-label $LABEL_NAME --repo $REPO)"
