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

## Reproducing

**Python version:** 3.10–3.12 recommended (tested with 3.13; `MDAnalysis`,
`mdtraj`, and `pyemma` are the packages most likely to lag behind the very
latest Python release, so if installation fails, try 3.11).

**Install dependencies:**

```bash
pip install -r requirements.txt
```

`pyemma` and `contact_map` in `requirements.txt` are only needed for the
exploratory `kmeans-2.ipynb`; every other notebook runs without them.

**External (non-Python) tools**, needed only for `phylogenetic_tree-2.ipynb`:
[MAFFT](https://mafft.cbrc.jp/alignment/software/) (sequence alignment) and
[IQ-TREE](http://www.iqtree.org/) (tree inference) must be installed and on
your `PATH`; the notebook calls them as external processes via `subprocess`.

**What input the notebooks expect:** None of the raw MD trajectory or
topology files are included in this repository — the full HvGLU3-CESA1 and
HvGLU3-CESA3 trajectory sets are tens of gigabytes and are not public data.
Concretely, the notebooks expect, at paths set in their first "Configuration"
cell:

- A reference/topology structure, `backbone.pdb` (CESA trimer + HvGLU3,
  chains A-D), used for alignment and as the RMSD/RMSF reference.
- Per-replica backbone-only trajectories, e.g. `traj1.xtc` … `traj8.xtc`
  (CESA1, 8 replicas) or `traj1.xtc` … `traj4.xtc` (CESA3, 4 replicas), or a
  single pre-merged trajectory such as `CESA1_all_backbone.xtc` /
  `CESA3_all_backbone.xtc` for the clustering notebooks.
- Chain IDs are expected to follow A = HvGLU3, B/C/D = the three CESA
  subunits of the homotrimer, matching the conventions in the manuscript and
  figure captions.

Without those files, the notebooks won't execute past the data-loading cell
— that's expected; they're included so the method (and exact code) used to
produce each figure is fully visible and checkable, not necessarily so a
visitor can one-click reproduce the result without the (very large) raw data.

**Minimal runnable example:** `example/` contains a tiny synthetic 4-atom
system (`toy_reference.pdb`, `toy_traj.xtc`, generated by
`make_toy_system.py`) and `run_toy_rmsd.py`, which applies the exact same
`MDAnalysis.analysis.rms.RMSD` pattern used in
`CESA1_RMSD_MDAnalysis.ipynb` / `rmsd_merged_complex.ipynb` to that toy
system. It runs in a few seconds with no external data and confirms the
analysis code itself is correct and runnable end-to-end:

```bash
cd example
python run_toy_rmsd.py
```

## Notes

- See the manuscript for full methodology, results, and discussion.
- Repository license: MIT (see `LICENSE`).
