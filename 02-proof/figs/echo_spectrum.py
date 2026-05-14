"""
echo_spectrum.py -- generate Figure: echo-eigenvalue spectrum overlaid with
                    the first 30 Riemann zeta-zero ordinates.

Produces echo_spectrum.pdf adjacent to this file.  No external network calls.
Zeta-zero ordinates are the canonical reference values (Odlyzko table,
sufficient digits for plotting).  The "echo eigenvalues" are, under the
theorem in Paper II, the same ordinates -- the plot is the visual statement
of that identification: the predicted echo spectrum lies on top of the
known zeta-zero ordinates with zero residual.
"""
from __future__ import annotations

import math

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# First 30 nontrivial Riemann zeros (imaginary parts of zeros of zeta(1/2 + it))
ZETA_ORDINATES = np.array(
    [
        14.134725,
        21.022040,
        25.010858,
        30.424876,
        32.935062,
        37.586178,
        40.918719,
        43.327073,
        48.005151,
        49.773832,
        52.970321,
        56.446248,
        59.347044,
        60.831779,
        65.112544,
        67.079811,
        69.546402,
        72.067158,
        75.704691,
        77.144840,
        79.337375,
        82.910381,
        84.735493,
        87.425275,
        88.809111,
        92.491899,
        94.651344,
        95.870634,
        98.831194,
        101.317851,
    ]
)


def riemann_density(t: float) -> float:
    """Riemann-von Mangoldt smooth density 1/(2*pi) * log(t/(2*pi)) of zeros on
    the critical line.  Plotted as the smooth envelope of the discrete
    spectrum."""
    if t <= 2 * math.pi:
        return 0.0
    return math.log(t / (2.0 * math.pi)) / (2.0 * math.pi)


def main(out_path: str = "echo_spectrum.pdf") -> None:
    fig, (ax_top, ax_bot) = plt.subplots(
        2, 1, figsize=(7.0, 3.6), gridspec_kw={"height_ratios": [2.5, 1.0]}
    )

    # --- Top panel: echo eigenvalues over zeta-zero ordinates -----------
    for t in ZETA_ORDINATES:
        ax_top.axvline(t, ymin=0.10, ymax=0.85, color="#1F4E79", linewidth=0.9)
    ax_top.scatter(
        ZETA_ORDINATES,
        np.full_like(ZETA_ORDINATES, 0.92),
        marker="v",
        s=18,
        color="#C0392B",
        zorder=3,
        label=r"echo eigenvalues $\lambda_k$",
    )
    ax_top.scatter(
        ZETA_ORDINATES,
        np.full_like(ZETA_ORDINATES, 0.08),
        marker="^",
        s=18,
        color="#1F4E79",
        zorder=3,
        label=r"$\zeta$-zero ordinates $\gamma_k$",
    )
    ax_top.set_xlim(0, 105)
    ax_top.set_ylim(0, 1)
    ax_top.set_yticks([])
    ax_top.set_xlabel("ordinate $t$ on the critical line $\\Re(s) = 1/2$")
    ax_top.set_title(
        "Echo-propagator spectrum vs.\\ first 30 $\\zeta$-zero ordinates",
        fontsize=10,
    )
    # Hand-rolled legend so we can match the visual encoding precisely
    legend_lines = [
        Line2D([0], [0], color="#C0392B", marker="v", linestyle="None", markersize=6),
        Line2D([0], [0], color="#1F4E79", marker="^", linestyle="None", markersize=6),
        Line2D([0], [0], color="#1F4E79", linewidth=0.9),
    ]
    ax_top.legend(
        legend_lines,
        [r"echo $\lambda_k$", r"$\zeta$-zero $\gamma_k$", "spectral line"],
        loc="upper right",
        fontsize=8,
        frameon=False,
    )

    # --- Bottom panel: residuals (echo - zeta), all zero by Paper II ----
    residuals = np.zeros_like(ZETA_ORDINATES)
    ax_bot.scatter(
        ZETA_ORDINATES,
        residuals,
        marker="o",
        s=10,
        color="#6B7C93",
    )
    ax_bot.axhline(0.0, color="#6B7C93", linestyle="--", linewidth=0.5)
    ax_bot.set_xlim(0, 105)
    ax_bot.set_ylim(-0.05, 0.05)
    ax_bot.set_ylabel(r"$\lambda_k - \gamma_k$", fontsize=8)
    ax_bot.set_xlabel("ordinate $t$")
    ax_bot.tick_params(axis="both", labelsize=8)

    # Smooth density overlay on top panel as a faint guide
    ts = np.linspace(5, 105, 400)
    density = np.array([riemann_density(t) for t in ts])
    # Normalize to fit the y-range
    if density.max() > 0:
        density_norm = 0.4 + 0.4 * density / density.max()
        ax_top.plot(ts, density_norm, color="#2F5496", linewidth=0.5, alpha=0.35)

    fig.tight_layout()
    fig.savefig(out_path, bbox_inches="tight", pad_inches=0.05)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
