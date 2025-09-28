CLA integration (minimal)

This repository's `README.md` references this document only for CLA App installation and migration guidance. The current project uses an Actions-based CLA flow by default; if you prefer to install a GitHub App to manage CLAs (recommended for scale), follow the short steps below.

Install CLA Assistant (recommended small-scale App)
1. Visit https://cla-assistant.io/ and sign in with your GitHub account.
2. Click "Install" and select this repository (or your organization) to grant permissions.
3. In the CLA Assistant dashboard, add a project for `BravelyBaby/psychic-barnacle` and point it to this repository's `CLA.md` (paste the CLA text or provide a link).
4. Enable the project so CLA Assistant enforces signatures on pull requests. Test with a draft PR from a fork to verify behavior.

Migration note
- After you confirm the App works, disable or remove the repository's Actions-based CLA workflows (`cla-check`, `cla-labeler`) to avoid duplicate checks. Optionally keep `cla-verified-gate` if you want an additional manual verification label.

That's all this file provides in the current README-focused version.
