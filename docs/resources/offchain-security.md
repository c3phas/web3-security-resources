---
title: Offchain Security
description: Offchain Security page in the Web3 Security Resources 2026 hub.
---

# Offchain Security

Smart contract security is only one part of Web3 risk. Users reach protocols
through domains, frontends, wallets, APIs, RPCs, docs, governance portals,
support flows, analytics, bridges, and cloud infrastructure.

## What to Review

| Area | Why it matters |
| --- | --- |
| DNS and domains | Domain takeover can redirect users, wallets, docs, governance, and support flows. |
| Frontend builds | A compromised deploy can turn a safe contract into a wallet-draining interface. |
| Wallet UX | Users sign typed data, approvals, permits, and chain switches based on UI context. |
| APIs and admin panels | Offchain authz bugs can change protocol state, leak data, or bypass rate limits. |
| CI/CD and secrets | Build pipelines often hold deploy keys, RPC keys, package tokens, and cloud credentials. |
| Dependencies | Malicious packages and install scripts can compromise builds and frontends. |
| Cloud and hosting | Storage buckets, CDN rules, serverless functions, and WAF policies affect user trust. |
| Support and comms | Fake support, compromised Discord/Telegram/X accounts, and phishing links drive losses. |

## Must Learn

| Resource | Tier | Use |
| --- | --- | --- |
| [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) | Must learn | Web application testing methodology. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Must learn | Web/API security control baseline. |
| [OWASP API Security Top 10](https://owasp.org/www-project-api-security/) | Must learn | API auth, authorization, and abuse risk taxonomy. |
| [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/) | Use in real audits | Pipeline threat model and control checklist. |
| [Burp Suite Web Security Academy](https://portswigger.net/web-security) | Must learn | Practical web exploitation labs. |
| [DigiBastion Threat Intel](https://www.digibastion.com/threat-intel) | Use in real audits | Free alert feed for supply-chain, OPSEC, Web3, and DeFi threats. |
| [VANTAGE by DigiBastion](https://vantage.digibastion.com/) | Watchlist | Maintainer-labeled external domain and trust-risk monitoring. |

## Practical Tools

| Tool | Tier | Use |
| --- | --- | --- |
| [Burp Suite](https://portswigger.net/burp) | Must learn | Web/API proxying, authz testing, replay, and tampering. |
| [OWASP ZAP](https://www.zaproxy.org/) | Use in real audits | Open-source proxy and scanner. |
| [Semgrep](https://semgrep.dev/) | Use in real audits | Custom source-code rules for frontend, API, IaC, and CI. |
| [Socket](https://socket.dev/) | Use in real audits | JavaScript supply-chain risk. |
| [OpenSSF Scorecard](https://github.com/ossf/scorecard) | Use in real audits | Dependency and repository health checks. |
| [Sigstore](https://www.sigstore.dev/) | Situational / advanced | Artifact signing and provenance. |
| [SLSA](https://slsa.dev/) | Situational / advanced | Supply-chain integrity maturity model. |

## Web3-Specific Checks

- Verify contract addresses, chain IDs, spender addresses, and typed-data domains.
- Detect frontend asset drift and unauthorized deploys.
- Review third-party scripts, analytics, chat widgets, and wallet SDKs.
- Confirm DNS, TLS, CDN, registrar, and hosting ownership with phishing-resistant MFA.
- Test APIs for broken object-level authorization and tenant isolation.
- Review CI/CD secrets, branch protections, deploy tokens, and release provenance.
- Monitor domain lookalikes, phishing kits, wallet-drainer infrastructure, and support impersonation.
