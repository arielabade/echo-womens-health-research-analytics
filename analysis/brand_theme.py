"""Shared chart theme for the portfolio figures.

Presentation layer only: this module sets colours, type and spacing. It never
touches a value. Every number plotted comes from the aggregated results in
``generate_portfolio_figures.py``.

Palette roles
-------------
Carbon / Graphite  text and structure
Steel              neutral series, metadata, support
Cobalt             the one series that answers the question
Ivory              soft surfaces

Chart rule: start in neutrals and let a single accent carry the reading.
A rainbow without semantics is decoration, not analysis.
"""

from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager

CARBON = "#050505"
GRAPHITE = "#1B1C1F"
STEEL = "#7E8791"
COBALT = "#5B6CFF"
IVORY = "#F6F5F0"
HAIRLINE = "#D8D9DC"


def apply() -> None:
    """Install the house style. Falls back cleanly when Lato is absent."""
    available = {font.name for font in font_manager.fontManager.ttflist}
    stack = [name for name in ("Lato", "Helvetica Neue", "Helvetica", "Arial") if name in available]
    stack.append("DejaVu Sans")

    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": stack,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": HAIRLINE,
            "axes.labelcolor": GRAPHITE,
            "axes.labelsize": 10,
            "axes.titlesize": 15,
            "axes.titlecolor": CARBON,
            "axes.titleweight": "bold",
            "axes.grid": False,
            "text.color": GRAPHITE,
            "xtick.color": STEEL,
            "ytick.color": GRAPHITE,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "grid.color": HAIRLINE,
            "grid.linewidth": 0.8,
            "legend.frameon": False,
            "savefig.facecolor": "white",
        }
    )


def series_colors(values: list[float], highlight: str = "max") -> list[str]:
    """Neutral bars, with Cobalt on the single value that carries the finding.

    ``highlight`` selects the extreme worth reading: the strongest item, or the
    one that stands apart from the rest.
    """
    target = max(values) if highlight == "max" else min(values)
    index = values.index(target)
    return [COBALT if i == index else STEEL for i in range(len(values))]


def finish(ax, *, xgrid: bool = True) -> None:
    """Remove frame noise so the bars carry the composition."""
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color(HAIRLINE)
    if xgrid:
        ax.grid(axis="x", color=HAIRLINE, linewidth=0.8, alpha=0.9)
        ax.set_axisbelow(True)


def source_note(fig, note: str, y: float = 0.01) -> None:
    fig.text(0.01, y, note, fontsize=8, color=STEEL)
