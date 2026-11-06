"""
Builds a tiny synthetic topology + trajectory (a tetrahedron of 4 CA-only
"residues" that wobbles over a few frames) purely so the RMSD/RMSF pattern
used throughout this repo's notebooks can be demonstrated end-to-end without
needing the real (large, unpublished) HvGLU3-CESA trajectories.
"""
import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis import rms

# --- 1. Build a minimal 4-residue, CA-only Universe ---
n_atoms = 4
u = mda.Universe.empty(n_atoms, n_residues=n_atoms, atom_resindex=range(n_atoms), trajectory=True)
u.add_TopologyAttr('name', ['CA'] * n_atoms)
u.add_TopologyAttr('resname', ['GLY'] * n_atoms)
u.add_TopologyAttr('resid', list(range(1, n_atoms + 1)))
u.add_TopologyAttr('chainID', ['A'] * n_atoms)

ref_coords = np.array([
    [0.0, 0.0, 0.0],
    [3.8, 0.0, 0.0],
    [1.9, 3.3, 0.0],
    [1.9, 1.1, 3.1],
], dtype=np.float32)
u.atoms.positions = ref_coords
u.atoms.write("toy_reference.pdb")

# --- 2. Write a short "trajectory" (5 frames, small random perturbations) ---
rng = np.random.default_rng(42)
with mda.Writer("toy_traj.xtc", n_atoms=n_atoms) as w:
    for frame in range(5):
        noisy = ref_coords + rng.normal(scale=0.3 * (frame + 1), size=ref_coords.shape).astype(np.float32)
        u.atoms.positions = noisy
        w.write(u.atoms)

print("Wrote toy_reference.pdb and toy_traj.xtc")
