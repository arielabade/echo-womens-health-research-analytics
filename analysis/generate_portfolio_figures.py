from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

import brand_theme


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "assets" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_instructional_scores():
    items = [
        "Content aligned with course goals",
        "Content aligned with personal goals",
        "Session sequence",
        "Language used in course material",
        "Chat discussions",
        "Learning-session discussions",
        "Recommended material/readings",
        "Session updates and reminders",
        "Questions and answers",
        "Links shared during sessions",
        "Content-retention methodology",
        "End-of-session activities",
        "Guidance for resolving care errors",
        "Content volume per session",
        "Scientific evidence suggested",
    ]
    means = [9.38, 8.92, 9.11, 9.45, 8.75, 8.83, 9.15, 9.29, 9.15, 9.25, 9.13, 8.66, 9.05, 9.15, 9.30]

    y = np.arange(len(items))
    fig, ax = plt.subplots(figsize=(11, 8))
    bars = ax.barh(y, means, color=brand_theme.series_colors(means, "max"), height=0.62)
    ax.set_yticks(y)
    ax.set_yticklabels(items, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlim(0, 10)
    ax.set_xlabel("Mean score on a 0-10 Likert scale")
    ax.set_title("Instructional Procedure Evaluation: Mean Scores by Item", pad=16, weight="bold")
    brand_theme.finish(ax)

    for bar, value in zip(bars, means):
        ax.text(
            value + 0.08,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.2f}",
            va="center",
            fontsize=8,
            color=brand_theme.GRAPHITE,
        )

    fig.text(
        0.01,
        0.01,
        "Source: aggregated, non-identifiable results from ECHO women's health course evaluation materials.",
        fontsize=8,
        color=brand_theme.STEEL,
    )
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(OUTPUT_DIR / "instructional-procedure-scores.png", dpi=200)
    plt.close(fig)


def save_knowledge_scores():
    items = [
        "Knowledge appears in products/services",
        "Knowledge improves performance",
        "Knowledge is useful for work",
        "Knowledge increases productivity",
        "Knowledge makes the team more effective",
        "Knowledge improves work quality",
    ]
    means = [3.95, 4.67, 4.67, 4.60, 4.60, 4.68]
    std = [0.88, 0.56, 0.57, 0.60, 0.56, 0.50]

    y = np.arange(len(items))
    fig, ax = plt.subplots(figsize=(10, 5.8))
    ax.barh(
        y,
        means,
        xerr=std,
        color=brand_theme.series_colors(means, "min"),
        ecolor=brand_theme.GRAPHITE,
        capsize=4,
        height=0.6,
    )
    ax.set_yticks(y)
    ax.set_yticklabels(items, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlim(0, 5.4)
    ax.set_xlabel("Mean score on a 1-5 Likert scale")
    ax.set_title("Knowledge Management Scale: Mean Scores and Dispersion", pad=16, weight="bold")
    brand_theme.finish(ax)

    # Place the label clear of the error bar so dispersion stays readable.
    for index, (value, dispersion) in enumerate(zip(means, std)):
        ax.text(
            value + dispersion + 0.07,
            index,
            f"{value:.2f}",
            va="center",
            fontsize=8,
            color=brand_theme.GRAPHITE,
        )

    fig.text(
        0.01,
        0.01,
        "Error bars show standard deviation. Source: aggregated, non-identifiable ECHO evaluation results.",
        fontsize=8,
        color=brand_theme.STEEL,
    )
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(OUTPUT_DIR / "knowledge-management-scores.png", dpi=200)
    plt.close(fig)


def save_analysis_summary():
    labels = [
        "Instructional reaction",
        "Knowledge management",
        "Correlation analysis",
        "Group comparison",
    ]
    values = [
        "All 15 items had mode = 10; means ranged from 8.66 to 9.45.",
        "Knowledge-related items were generally positive; means ranged from 3.95 to 4.68.",
        "Strong reported Spearman associations included Q1-Q2 = 1.00 and Q14-Q15 = 0.87.",
        "Kruskal-Wallis tests did not identify statistically significant group differences in the reviewed materials.",
    ]

    fig, ax = plt.subplots(figsize=(11, 5.6))
    ax.axis("off")
    ax.set_title("Aggregated Analytical Evidence Used in the Portfolio", weight="bold", fontsize=16, pad=18)

    for idx, (label, value) in enumerate(zip(labels, values)):
        y = 0.82 - idx * 0.2
        ax.add_patch(
            plt.Rectangle(
                (0.04, y - 0.08), 0.92, 0.13,
                color=brand_theme.IVORY, ec=brand_theme.HAIRLINE, lw=1,
            )
        )
        ax.add_patch(
            plt.Rectangle(
                (0.04, y - 0.08), 0.008, 0.13,
                color=brand_theme.COBALT, ec=brand_theme.COBALT,
            )
        )
        ax.text(0.07, y + 0.015, label, fontsize=11, weight="bold", va="center", color=brand_theme.CARBON)
        ax.text(0.07, y - 0.04, value, fontsize=9.5, va="center", color=brand_theme.GRAPHITE)

    fig.text(
        0.04,
        0.04,
        "This figure summarizes aggregate results only. Original source documents and datasets are excluded from Git.",
        fontsize=8,
        color=brand_theme.STEEL,
    )
    fig.savefig(OUTPUT_DIR / "aggregated-analysis-summary.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    brand_theme.apply()
    save_instructional_scores()
    save_knowledge_scores()
    save_analysis_summary()
