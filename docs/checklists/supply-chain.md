---
title: Supply Chain Security
description: Supply Chain Security page in the Web3 Security Resources 2026 hub.
---

# Supply Chain Security

- Dependencies are pinned and updated through review.
- Lockfiles are committed and reproducible.
- Install scripts are reviewed or disabled where practical.
- Dependency risk tools run in CI.
- GitHub branch protection and required reviews are enabled.
- Secret scanning is enabled.
- CI/CD deploy permissions are least privilege.
- Build artifacts are traceable to commits.
- Container images and actions use pinned versions or trusted publishers.
- Vendor access is reviewed and logged.


## Evidence gates

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| Build provenance is visible | CI logs, lockfiles, package manager config, deployment actor, and artifact hash. | Platform lead | Production artifacts tie back to reviewed source and dependency state. | Manual deploys bypass review and provenance. |
| High-risk dependencies are owned | Wallet connector, analytics, tag manager, RPC, SDK, and CDN dependency register. | Engineering lead | Each privileged dependency has owner, update rule, and fallback. | A package can change user signing behavior without security review. |
| Vendor compromise is rehearsed | Disable plan, allowlist, CSP/SRI limits, replacement path, and user comms draft. | Security lead | Critical vendors can be isolated without inventing response steps live. | Controls assume SRI or CSP alone can solve malicious trusted code. |
