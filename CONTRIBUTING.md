# Contributing to Psychic Barnacle (proprietary)

Thank you for your interest. This repository is intended as a proprietary, commercial project owned by BravelyBaby. No part of the code may be used, copied, or redistributed without express written permission.

Before contributing
- Contact the repository owner at lifeoflandry@gmail.com to discuss contribution permissions and any necessary contribution license or agreement.
- Do not submit code or assets unless you have explicit permission to contribute.

Branch naming
- Use `feat/` for new features (e.g., `feat/add-node-stub`).
- Use `fix/` for bugs and `chore/` for maintenance.

PR checklist (for permitted contributors)
- [ ] The change is scoped and no larger than necessary.
- [ ] If you add code, include a small test in `tests/` and document how to run it.
- [ ] Update `README.md` with any new commands or manifest files added.
- [ ] No secrets committed — use environment variables and document them.

Legal note
- Contributions may require a signed Contributor License Agreement (CLA) or other written agreement. Contact the owner before submitting work.

Automation & branch protection
- This repository uses automated checks to detect signed CLAs and to gate merges until a maintainer verifies them.
- Workflow behavior:
	- `cla-check` verifies the PR body and requires a `CLA-<your-name>.md` file containing `<!-- CLA-SIGNED: true -->`.
	- `cla-labeler` will automatically add a `cla/present` label when a signed CLA file is detected in the PR.
	- Maintainers must perform manual verification (confirm email/identity) and then add the `cla/verified` label to allow merging.

Setup for maintainers (recommended):
1. In Repository Settings → Branches → Branch protection rules, require the checks `CLA check` and `CLA Verified Gate` to pass before merging to `main`.
2. Use the `cla/present` label as a quick indicator that a signed CLA file is attached and ready for review.

Maintainer helper: verifying a CLA quickly

We provide a small helper script `scripts/verify-cla.sh` that adds the `cla/verified` label after you've manually verified the contributor's signed CLA (email or attached file).

Requirements:
- GitHub CLI (`gh`) installed and authenticated as the maintainer (run `gh auth login`).

Usage:
```bash
# from the repo root
./scripts/verify-cla.sh <pr-number>
# or with explicit repo
./scripts/verify-cla.sh 42 BravelyBaby/psychic-barnacle
```

This script will create the `cla/verified` label if it does not exist and add it to the PR. After adding the label, the `CLA Verified Gate` workflow will pass and the PR becomes mergeable if other checks are satisfied.


