---
title: Frontend Security
description: Frontend Security page in the Web3 Security Resources 2026 hub.
---

# Frontend Security

## Build and Hosting

- CI/CD requires code review and protected branches.
- Production deploys are tied to signed or traceable builds.
- Secrets are not available to untrusted build steps.
- Third-party scripts are minimized and reviewed.
- CSP is enforced where practical.
- Asset hashes or deploy manifests are monitored for drift.

## Wallet UX

- Chain ID, contract address, spender, method, amount, and typed-data domain are displayed safely.
- Dangerous approvals are labeled clearly.
- Transaction simulation is used where practical.
- WalletConnect and provider handling reject unexpected chains or accounts.
- Phishing and clone-site detection is part of monitoring.

## Web Controls

- Authentication and authorization are server-side.
- API requests are rate-limited and validated.
- XSS, CSRF, open redirect, and injection paths are tested.
- Error messages do not leak internals.
- Analytics and support widgets cannot alter transaction flows.


## Evidence gates

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| Browser-shipped material is intentional | Bundle review, source map policy, public env vars, API keys, comments, and endpoint inventory. | Frontend lead | No browser-visible material grants write capability or unnecessary reconnaissance value. | Public SDK keys are treated as harmless without quota, origin, or permission review. |
| Wallet signing path is stable | Route, modal, connector, RPC, simulation, transaction preview, and copy baseline. | Wallet/frontend lead | Unexpected signing-path changes are reviewed before users rely on them. | A vendor widget can alter a wallet-facing flow without approval. |
| Emergency rollback exists | Rollback runbook, cache invalidation, CDN owner, release artifact retention, and comms path. | Engineering lead | The team can remove malicious or broken browser code quickly. | CDN caches keep serving compromised assets after rollback. |
