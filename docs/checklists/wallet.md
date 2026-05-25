---
title: Wallet Security
description: Wallet Security page in the Web3 Security Resources 2026 hub.
---

# Wallet Security

- Treasury and admin wallets are separate from personal wallets.
- Hardware wallets or MPC are used for high-value operations.
- Seed phrase storage is offline, access-controlled, and tested for recovery.
- Signing devices are hardened and used only for trusted workflows.
- Blind signing is disabled except under documented emergency procedure.
- Allowances and delegated permissions are reviewed.
- Address books and ENS names are verified before use.
- Wallet-drainer and approval-monitoring alerts are enabled where possible.


## Evidence gates

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| User intent is represented | Transaction preview, domain context, contract labels, method decode, value, approvals, and risk messages. | Wallet lead | A reasonable user can understand the consequence of signing. | UI copy looks safe while the transaction grants broad approval. |
| Simulation failures are safe | Fallback behavior, stale-state handling, unsupported chain path, and warning copy. | Wallet/frontend lead | Failed simulation never becomes silent approval. | Simulation failure is hidden to preserve conversion. |
| Delegation is bounded | Session key scope, expiry, revocation, spending limits, and chain/account binding. | Wallet lead | Delegated authority is limited and revocable. | Convenience flows grant durable authority with unclear revocation. |
