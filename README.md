# HvGLU3–CESA Molecular Dynamics Analysis

Analysis notebooks supporting a study of HvGLU3 docking and molecular dynamics
with the barley cellulose synthase subunits CESA1, CESA3, and CESA6 (CESA6
was excluded after docking, see manuscript).

## What each notebook does

| Notebook | What it does |
|---|---|
| `phylogenetic_tree-2.ipynb` | Builds the CESA phylogenetic tree (38 sequences across 4 species: Hv, At, Os, Zm) — aligns with MAFFT, infers the tree with IQ-TREE, and draws it with Biopython's `Bio.Phylo`. |
| `CESA1_RMSD_MDAnalysis.ipynb` | Computes backbone RMSD of the HvGLU3-CESA1 complex against a reference frame for each of 8 independent MD replicas, then averages them into a single ensemble RMSD curve. |
| `CESA1_RMSF_MDAnalysis.ipynb` | Computes per-residue backbone RMSF for the HvGLU3-CESA1 complex across the 8 replicas, after aligning each to the common reference structure. |
| `CESA1_kmeans_v2.ipynb` | Loads the merged CESA1 trajectory, featurizes it with Cα pairwise distances, reduces dimensionality with PCA, and clusters the conformational landscape with K-means (elbow method for k). |
| `CESA1_contact_map.ipynb` | Computes HvGLU3–CESA1 residue-residue contact frequency maps: overall (all frames) and per conformational cluster, to characterize how the binding interface changes across states. |
| `rmsd_merged_complex.ipynb` | Computes backbone RMSD of the full concatenated, cross-fitted CESA3 trajectory (T1→T2→T3→T4) against a single shared reference structure. |
| `cesa3_trajectory_divergence-2.ipynb` | Diagnoses *why* the four CESA3 trajectories look structurally different in VMD, using per-residue RMSF within each trajectory and complementary per-residue diagnostics. |
| `CESA3_kmeans.ipynb` | Same PCA + K-means clustering pipeline as `CESA1_kmeans_v2.ipynb`, applied to CESA3, so the two systems' conformational landscapes can be directly compared. |
| `CESA3_contact_map.ipynb` | Computes HvGLU3–CESA3 contact frequency maps: overall, per cluster, and a residue × cluster heatmap showing which HvGLU3 residues are engaged in which conformational state. |
| `hvglu3_cesa_distance.ipynb` | Computes the center-of-mass (COM) distance between HvGLU3 and the CESA trimer over time/frames, for both the CESA1 and CESA3 systems, quantifying the qualitative "closer/farther" impression seen in VMD. |
| `kmeans-2.ipynb` | Earlier/exploratory version of the PCA + K-means clustering workflow (uses PyEMMA featurization and the `contact_map` package) that the CESA1/CESA3-specific kmeans notebooks above superseded. |

## Tools and libraries used

- **MD trajectory handling & structural analysis:** [MDAnalysis](https://www.mdanalysis.org/) and [MDTraj](https://www.mdtraj.org/) — RMSD, RMSF, alignment, distance and contact calculations directly on trajectory/topology files (`.xtc`, `.pdb`).
- **Dimensionality reduction & clustering:** [scikit-learn](https://scikit-learn.org/) (`PCA`, `KMeans`, `StandardScaler`) to project MD conformations into principal-component space and cluster them into discrete conformational states.
- **Phylogenetics:** [Biopython](https://biopython.org/) (`Bio.Phylo`) for tree parsing/visualization, with sequence alignment (MAFFT) and tree inference (IQ-TREE) run as external tools.
- **Data handling:** [NumPy](https://numpy.org/) and [pandas](https://pandas.pydata.org/) for numerical arrays and tabular results (contact frequencies, distances, cluster assignments).
- **Visualization:** [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) for all plots (RMSD/RMSF curves, PCA scatter plots, contact-frequency dot matrices and heatmaps); [py3Dmol](https://github.com/3dmol/3Dmol.js) for interactive 3D structure viewing in `CESA1_contact_map.ipynb`.
- **Exploratory-only (earlier version):** [PyEMMA](http://www.emma-project.org/) and the [`contact_map`](https://github.com/dwhswenson/contact_map) package, used only in `kmeans-2.ipynb`.

## Notes

- Notebooks expect MD trajectory and topology files (not included in this
  repository due to size) at relative paths — update paths before re-running.
- See the manuscript for full methodology, results, and discussion.
