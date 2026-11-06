# HvGLU3–CESA Molecular Dynamics Analysis

Analysis notebooks supporting the study of HvGLU3 docking and molecular dynamics
with the barley cellulose synthase subunits CESA1, CESA3, and CESA6.

## Contents

| Notebook | Description |
|---|---|
| `phylogenetic_tree-2.ipynb` | Phylogenetic analysis of CESA proteins (Figure 1) |
| `CESA1_RMSD_MDAnalysis.ipynb` | Backbone RMSD analysis, HvGLU3-CESA1 complex |
| `CESA1_RMSF_MDAnalysis.ipynb` | Per-residue RMSF analysis, HvGLU3-CESA1 complex |
| `CESA1_kmeans_v2.ipynb` | PCA + K-means conformational clustering, CESA1 |
| `CESA1_contact_map.ipynb` | Residue-pair contact frequency analysis, CESA1 |
| `rmsd_merged_complex.ipynb` | Combined RMSD analysis across the merged complex |
| `cesa3_trajectory_divergence-2.ipynb` | Trajectory divergence analysis, CESA3 |
| `kmeans-2.ipynb` | PCA + K-means conformational clustering (general) |
| `CESA3_kmeans.ipynb` | PCA + K-means conformational clustering, CESA3 |
| `CESA3_contact_map.ipynb` | Residue-pair contact frequency analysis, CESA3 |
| `hvglu3_cesa_distance.ipynb` | Center-of-mass distance analysis, HvGLU3-CESA |

## Notes

- Notebooks assume MD trajectory and topology files (not included here) in
  expected relative paths — update paths before re-running.
- See the manuscript for full methodology.
