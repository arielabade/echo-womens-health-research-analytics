# Portfolio Audit Summary

This document records the repository-level audit performed before preparing the public portfolio case study.

## Materials Reviewed

- DOCX research writeups and article draft.
- XLSX spreadsheets containing aggregate results for instructional reaction and knowledge-management scales.
- PNG charts including bar charts, boxplots, regression-style trend plots, and Spearman correlation heatmaps.
- Duplicate exported chart folders.
- A Jupyter Notebook containing R and Python analysis cells, raw outputs, local Colab paths, and participant-level previews by state.
- Contextual Project ECHO and institutional logo images supplied separately by the project owner.

## Evidence Found

The files support describing the project as a quantitative evaluation of a remote ECHO-based women's health course. The materials include:

- a descriptive, quantitative, cross-sectional research design;
- Likert-scale evaluation instruments;
- organization of results in spreadsheets;
- descriptive statistics including mode, mean, and standard deviation;
- inferential tests including Kolmogorov-Smirnov, chi-square, Kruskal-Wallis, and Spearman correlation;
- reporting and interpretation of course evaluation results;
- chart-based communication of aggregate findings.
- scientific-computing work in R and Python, including data cleaning, statistical testing, visualization, correlation analysis, and regression-style experimentation.

## Privacy Decisions

The original DOCX, XLSX, Portuguese chart exports, and raw Colab notebook were moved to `source-documents/original-materials/` and excluded from Git. This protects source documents, metadata, unpublished drafts, raw notebook outputs, and research context that should not be exposed as a public file dump.

No private identification numbers, contact details, credentials, keys, or private emails were detected by automated text search in the extracted DOCX text. One document contained author metadata naming the project contributor, which is useful for internal attribution but does not need to be exposed as source metadata in public artifacts.

Because the materials relate to health/research evaluation, the original datasets, spreadsheets, and raw notebook outputs are treated as restricted even when they appear partially aggregated.

## Public Portfolio Artifacts

The public repository uses English-language README documentation, newly generated figures based on aggregate results, contextual logo/reach images, and a sanitized notebook. The figures and notebook avoid individual-level records and use English labels.

The map screenshot supplied for context was not included because it contains visible Portuguese map labels and is not necessary for the final portfolio narrative.
