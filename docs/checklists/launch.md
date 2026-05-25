# Launch Readiness

## Deployment

- Deployment commit, compiler versions, build settings, and addresses are recorded.
- Constructor and initializer arguments are reviewed.
- Source code is verified where possible.
- Deployment scripts are reproducible.
- Ownership transfer steps are rehearsed.
- Proxy implementations and admins are correct.

## Controls

- Admin roles are assigned to expected multisigs or governance.
- Timelocks are configured and tested.
- Emergency pause or rate-limit controls are documented.
- Oracle, bridge, and dependency assumptions are monitored.
- Launch parameters match audited assumptions.

## Monitoring

- Alerts exist for privileged actions, upgrades, oracle drift, reserve changes, and abnormal outflows.
- Frontend asset drift, DNS, TLS, and registrar changes are monitored.
- Incident response contacts and signer availability are confirmed.
- Public communication templates are prepared.

## Final Gate

- External audit fixes are verified.
- Known risks are accepted by the right owners.
- Bug bounty or disclosure channel is live.
- Rollback or mitigation options are understood.
