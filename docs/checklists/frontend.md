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
