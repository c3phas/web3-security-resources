# Pre-Audit Readiness

## Scope

- Code freeze date is defined.
- In-scope repositories, commits, contracts, deployments, and chains are listed.
- Out-of-scope components and trusted dependencies are explicit.
- Protocol documentation explains assets, roles, invariants, and emergency powers.
- Architecture diagram shows contracts, oracles, bridges, frontends, APIs, and governance.

## Code and Tests

- Unit tests cover expected and failing paths.
- Fuzz or invariant tests cover accounting, permissions, and core state machines.
- Static analysis has been run and triaged.
- Dependencies are pinned and licenses are acceptable.
- Upgradeable contracts have storage-layout checks.
- Deployment scripts are tested on a fork or testnet.

## Security Context

- Threat model is current.
- Privileged roles and multisigs are documented.
- Known issues and risk acceptances are listed.
- Prior audit reports and fix status are linked.
- Monitoring and incident plans exist for critical flows.

## Auditor Package

- Build and test instructions work from a clean clone.
- Environment variables are documented without secrets.
- Diagrams and protocol docs match the code.
- Contact path for questions is defined.
- Expected report format and severity model are agreed.
