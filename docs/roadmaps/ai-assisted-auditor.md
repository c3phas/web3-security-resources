# AI-Assisted Auditor

Audience: auditors and engineers who use LLMs as assistants while keeping human
verification, reproducibility, and evidence as the standard.

## Principle

Use AI to accelerate reading, hypothesis generation, test scaffolding, and report
drafting. Do not use AI as the source of truth for exploitability, severity, or
correctness.

## Practical Workflow

| Step | AI can help with | Human must verify |
| --- | --- | --- |
| Scope reading | Summarize architecture and privileged flows. | Whether the summary matches code and docs. |
| Threat modeling | Generate abuse cases and trust boundaries. | Which assumptions are realistic for the protocol. |
| Tool triage | Explain warnings and cluster duplicates. | Whether any issue is exploitable. |
| Manual review | Suggest invariants and suspicious patterns. | State transitions, math, permissions, and external call behavior. |
| PoC writing | Scaffold tests and debug traces. | The PoC proves impact under realistic preconditions. |
| Reporting | Draft root cause and remediation language. | Accuracy, severity, evidence, and fix guidance. |

## Prompt Patterns

```text
Read this module as an auditor. Return only:
1. Assets controlled by this code.
2. Trust boundaries.
3. Privileged roles.
4. State transitions.
5. Invariants that must always hold.
6. Concrete review questions.
```

```text
Given this finding hypothesis, design a minimal Foundry test that proves or
falsifies it. Do not assume missing facts. List every required precondition.
```

## Limits

- LLMs hallucinate APIs, compiler behavior, and protocol details.
- They miss cross-file state transitions when context is incomplete.
- They can produce plausible but invalid PoCs.
- They can leak private code or secrets if used with unsafe tooling.
- They may overfit to famous bug classes and miss business-logic failures.

## Verification Standard

An AI-assisted finding is only reportable after it has the same evidence bar as
any other finding: code references, exploit path, realistic impact, reproducible
PoC or rigorous argument, severity reasoning, and fix guidance.
