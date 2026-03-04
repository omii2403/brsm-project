"""
Inject savefig calls into VFT_Final_Analysis.ipynb and spam_consensus.ipynb,
then execute both notebooks to regenerate all images in images/.
Run once; safe to re-run (idempotent – checks if savefig already present).
"""
import json, os, subprocess, sys

BASE     = r"C:\Users\kotad\OneDrive\Desktop\BRSM"
PYTHON   = r"C:\Users\kotad\OneDrive\Desktop\BRSM\.venv\Scripts\python.exe"
IMG_DIR  = os.path.join(BASE, "images")
os.makedirs(IMG_DIR, exist_ok=True)

# ── helpers ──────────────────────────────────────────────────────────────────
def inject_savefig(source_lines, savefig_path):
    """Return new source_lines with savefig inserted before the last plt.show()."""
    if any('images/' in l for l in source_lines):
        return source_lines  # already injected
    new = []
    show_indices = [i for i, l in enumerate(source_lines) if 'plt.show()' in l]
    if not show_indices:
        return source_lines
    insert_at = show_indices[-1]          # last plt.show() in the cell
    for i, line in enumerate(source_lines):
        if i == insert_at:
            indent = len(line) - len(line.lstrip())
            prefix = ' ' * indent
            new.append(f"{prefix}fig.savefig('{savefig_path}', bbox_inches='tight', dpi=150)\n")
        new.append(line)
    return new


def inject_savefig_at(source_lines, show_occurrence, savefig_path):
    """Insert savefig before the N-th (0-based) plt.show() in the cell."""
    if any('images/' + os.path.basename(savefig_path) in l for l in source_lines):
        return source_lines
    new = []
    count = 0
    for line in source_lines:
        if 'plt.show()' in line:
            if count == show_occurrence:
                indent = len(line) - len(line.lstrip())
                prefix = ' ' * indent
                new.append(f"{prefix}fig.savefig('{savefig_path}', bbox_inches='tight', dpi=150)\n")
            count += 1
        new.append(line)
    return new


def patch_notebook(nb_path, patches):
    """
    patches: list of dicts with keys:
        'cell_match'   – substring that must be in source to identify the cell
        'show_index'   – which plt.show() occurrence (0-based) to precede
        'savefig_path' – relative path string for savefig
    """
    with open(nb_path, encoding='utf-8') as f:
        nb = json.load(f)

    changed = 0
    for patch in patches:
        for cell in nb['cells']:
            if cell['cell_type'] != 'code':
                continue
            src = cell['source']
            full_text = ''.join(src)
            if patch['cell_match'] not in full_text:
                continue
            orig_len = len(src)
            new_src = inject_savefig_at(src, patch['show_index'], patch['savefig_path'])
            if len(new_src) != orig_len:
                cell['source'] = new_src
                changed += 1
                print(f"  + injected savefig → {patch['savefig_path']}")
            break   # found cell; move to next patch

    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print(f"  Patched {changed} cell(s) in {os.path.basename(nb_path)}")


# ── VFT notebook patches ──────────────────────────────────────────────────────
VFT_NB = os.path.join(BASE, "VFT_Final_Analysis.ipynb")
print("── Patching VFT_Final_Analysis.ipynb ──")
patch_notebook(VFT_NB, [
    {
        'cell_match':   "fig.suptitle('Section 3",
        'show_index':   0,
        'savefig_path': 'images/vft_fig06_cluster_scoring.png',
    },
    {
        'cell_match':   'Plot 1 - Histogram of Inter-Response Times',
        'show_index':   0,
        'savefig_path': 'images/vft_fig01_irt_histogram.png',
    },
    {
        'cell_match':   'Plot 2 - Box Plots of Inter-Response Times',
        'show_index':   0,
        'savefig_path': 'images/vft_fig02_violin_irt.png',
    },
    {
        'cell_match':   'Plot 6 - Bar Charts: Mean and Median IRT',
        'show_index':   0,
        'savefig_path': 'images/vft_fig05_bar_mean_irt.png',
    },
    {
        'cell_match':   'Plot 10 - Scatter Plot: Serial Position vs IRT',
        'show_index':   0,
        'savefig_path': 'images/vft_fig07_word_irt_position.png',
    },
    # Section 4 big cell: RQ1 (0th), RQ3 (2nd), RQ4 (3rd) plt.show()
    {
        'cell_match':   'RQ1 - Within-Cluster vs Between-Cluster IRT',
        'show_index':   0,
        'savefig_path': 'images/vft_fig11_rq1_within_between.png',
    },
    {
        'cell_match':   'RQ3 - Fluency Score vs Mean IRT Correlation',
        'show_index':   2,
        'savefig_path': 'images/vft_fig13_rq3_fluency_scatter.png',
    },
    {
        'cell_match':   'RQ4 - Cluster Size',
        'show_index':   3,
        'savefig_path': 'images/vft_fig14_rq4_cluster_fluency.png',
    },
])

# ── SpAM notebook patches ─────────────────────────────────────────────────────
SPAM_NB = os.path.join(BASE, "spam_consensus.ipynb")
print("\n── Patching spam_consensus.ipynb ──")
patch_notebook(SPAM_NB, [
    {
        'cell_match':   'Consensus Semantic Distance Matrices (SpAM)',
        'show_index':   0,
        'savefig_path': 'images/spam_fig01_heatmaps.png',
    },
    {
        'cell_match':   "Domain-Level SpAM & VFT Comparison",
        'show_index':   0,
        'savefig_path': 'images/spam_fig08_domain_comparison.png',
    },
])

# ── Execute notebooks via nbconvert ──────────────────────────────────────────
def run_nb(nb_path):
    name = os.path.basename(nb_path)
    print(f"\n── Executing {name} ──")
    result = subprocess.run(
        [PYTHON, '-m', 'jupyter', 'nbconvert',
         '--to', 'notebook',
         '--execute',
         '--inplace',
         '--ExecutePreprocessor.timeout=600',
         nb_path],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  ERROR:\n{result.stderr[-3000:]}")
    else:
        print(f"  OK – {name} executed successfully.")

run_nb(VFT_NB)
run_nb(SPAM_NB)

# ── Verify images ─────────────────────────────────────────────────────────────
print("\n── Images in images/ ──")
for f in sorted(os.listdir(IMG_DIR)):
    size = os.path.getsize(os.path.join(IMG_DIR, f))
    print(f"  {f}  ({size/1024:.1f} KB)")
print("Done.")
