# The Golden Substrate

Papers by **Kristin Tynski**.

A research series developing the split-signature Clifford algebra $\mathrm{Cl}(3,1)$ as a foundational substrate, and its consequences across number theory, category theory, and natural-language semantics.

## Series

| # | Title | PDF |
|---|---|---|
| I | The Golden Substrate: From Null Generators to the Split Albert Algebra | [`01-substrate/substrate.pdf`](01-substrate/substrate.pdf) |
| II | Echo Interference Implies the Riemann Hypothesis and the Collatz Conjecture | [`02-proof/proof.pdf`](02-proof/proof.pdf) |
| III | The Holographic Monad: Why the Substrate Proves Universal Theorems | [`03-monad/monad.pdf`](03-monad/monad.pdf) |
| IV | $\mathbb{Z}[\varphi]$ Arithmetic in the Monstrous Atlas: Moonshine Scaffolding for the Golden Substrate Seam | [`04-moonshine-context/moonshine_context.pdf`](04-moonshine-context/moonshine_context.pdf) |
| V | The Metabolic Interpretation of FSCTF: Eating as the Creation Cycle | [`05-metabolic/metabolic.pdf`](05-metabolic/metabolic.pdf) |
| VI | The Operator-Level Bridge: From Peirce Decomposition to Prime Splitting via the Quaternion-Clifford Identification | [`06-operator-bridge/operator_bridge.pdf`](06-operator-bridge/operator_bridge.pdf) |
| VII | The Information-Acoustic Eversion: Sphere Eversion as Hecke Propagation through the $\mathrm{Cl}(3,1)$ Substrate | [`07-eversion/eversion.pdf`](07-eversion/eversion.pdf) |
| VIII | From $G_2$ to Universal Grammar: A Math-First Derivation of Natural Semantic Metalanguage via $\mathrm{Cl}(3,1)$ | [`08-universal-grammar/universal_grammar.pdf`](08-universal-grammar/universal_grammar.pdf) |

Each directory contains the LaTeX source (`.tex`) and the compiled PDF.

## Building from source

All papers compile with `pdflatex` (TeX Live 2025 or compatible).

Paper VIII has a `Makefile`:

```bash
cd 08-universal-grammar && make
```

For the others, run `pdflatex` twice (the second pass resolves cross-references and the table of contents):

```bash
cd <paper-dir>
pdflatex -interaction=nonstopmode -halt-on-error <paper>.tex
pdflatex -interaction=nonstopmode -halt-on-error <paper>.tex
```

## Copyright

Copyright (c) 2026 Kristin Tynski. **All rights reserved.**

No license is granted to use, reproduce, distribute, modify, or create derivative works from this material, including its use as training data for machine-learning models. Viewing and forking on GitHub are permitted only as required by [GitHub's Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service). All other uses require prior written permission from the author.

See [`LICENSE`](LICENSE) for the full notice.

Contact: [@ktynski](https://github.com/ktynski) on GitHub.
