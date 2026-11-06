"""
Minimal, runnable example of the RMSD pattern used in
notebooks/CESA1_RMSD_MDAnalysis.ipynb and notebooks/rmsd_merged_complex.ipynb,
applied to a tiny synthetic 4-atom system (toy_reference.pdb / toy_traj.xtc)
so it can run in seconds with no external data.

In the real notebooks, "toy_reference.pdb" / "toy_traj.xtc" are replaced by
the actual backbone.pdb and per-replica trajN.xtc files, which are not
included in this repository (see README).
"""
import MDAnalysis as mda
from MDAnalysis.analysis import rms

u = mda.Universe("toy_reference.pdb", "toy_traj.xtc")
ref = mda.Universe("toy_reference.pdb")

R = rms.RMSD(u, ref, select="name CA")
R.run()

print("frame   time(ps)   RMSD(Å)")
for frame, time, rmsd in R.results.rmsd:
    print(f"{int(frame):5d}   {time:7.2f}   {rmsd:6.3f}")
