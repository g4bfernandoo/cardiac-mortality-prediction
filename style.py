"""
Visual identity for the cardiovascular research portfolio.
Shared across Project 5 (clustering), Project 1 (mortality prediction),
and Project 4 (systematic review) for consistent figure branding.

Usage:
    from style import apply_style, add_figure_rule, add_source_note, \
                       add_separator, title_font, PALETTE, CLUSTER_COLORS, CLUSTER_LABELS
"""

import matplotlib.pyplot as plt
import matplotlib as mpl

# ---------------------------------------------------------------------------
# Color palette (fixed across all three projects — do not modify per-project)
# ---------------------------------------------------------------------------
PALETTE = {
    "navy": "#1B2A4A",     # titles, primary
    "crimson": "#C0392B",  # key findings, alerts
    "steel": "#2471A3",    # secondary data
    "amber": "#D4AC0D",    # warnings
    "slate": "#566573",    # annotations, source notes
}

# Project 5 cluster labels, reused in Project 1 as the "care desert origin"
# feature (MUNIC_RES joined against para_cardiovascular_clustered.csv).
CLUSTER_COLORS = {
    -1: PALETTE["navy"],     # Reference Center (Belem / Ananindeua)
    0: PALETTE["steel"],     # Structural Care Desert
    1: PALETTE["amber"],     # Rapidly Deteriorating Access
    2: PALETTE["crimson"],   # High-Mortality Economic Corridor
}

CLUSTER_LABELS = {
    -1: "Reference Center",
    0: "Structural Care Desert",
    1: "Rapidly Deteriorating Access",
    2: "High-Mortality Economic Corridor",
}

title_font = {
    "family": "DejaVu Sans",
    "weight": "bold",
    "color": PALETTE["navy"],
}


def apply_style():
    """Call once at the top of every notebook, before any plotting."""
    mpl.rcParams.update({
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": PALETTE["slate"],
        "axes.labelcolor": PALETTE["navy"],
        "axes.titlecolor": PALETTE["navy"],
        "axes.titleweight": "bold",
        "axes.titlesize": 13,
        "axes.labelsize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.color": PALETTE["slate"],
        "ytick.color": PALETTE["slate"],
        "grid.color": "#D5D8DC",
        "grid.linewidth": 0.5,
        "axes.grid": True,
        "axes.axisbelow": True,
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
    })


def add_figure_rule(ax, y=1.02, color=None):
    """Thin horizontal rule under the title, spanning the axes width."""
    color = color or PALETTE["slate"]
    ax.axhline(y=y, xmin=0, xmax=1, color=color, linewidth=0.8,
               transform=ax.transAxes, clip_on=False)


def add_source_note(fig, text, y=-0.02):
    """Bottom-left source/methodology note in slate, small italic."""
    fig.text(0.01, y, text, fontsize=7.5, color=PALETTE["slate"],
              style="italic", ha="left")


def add_separator(fig, y):
    """Full-width horizontal separator line for multi-panel figures."""
    fig.add_artist(plt.Line2D([0.02, 0.98], [y, y],
                               transform=fig.transFigure,
                               color="#D5D8DC", linewidth=0.8))
