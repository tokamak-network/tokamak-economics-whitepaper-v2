import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 8), dpi=150)
ax.set_facecolor('white')
fig.patch.set_facecolor('white')

# Generate x values
x = np.linspace(0.001, 10, 500)

# Define curves - more hyperbolic, flattening more towards the end
y_operator = 0.28 * (1 - 1/(1 + x*0.8))
y_validator = 0.52 * (1 - 1/(1 + x*0.6))

# Total seigniorage (top - constant)
y_total = 0.85

# DAO bottom boundary (dotted line) - small gap above validator curve
y_dao_bottom = 0.56

# Fill L2 Operator area (bottom) - blue/gray
ax.fill_between(x, 0, y_operator, 
                alpha=0.12, color='#5D8AA8', 
                hatch='///', edgecolor='#5D8AA8', linewidth=0.5)

# Fill L2 Validator area (middle) - purple
ax.fill_between(x, y_operator, y_validator, 
                alpha=0.12, color='#9370DB', 
                hatch='///', edgecolor='#7B68EE', linewidth=0.5)

# Fill DAO area (top - green)
ax.fill_between(x, y_dao_bottom, y_total, 
                alpha=0.2, color='#2ECC71', 
                hatch='///', edgecolor='#27AE60', linewidth=0.5)

# Draw the curves
ax.plot(x, y_operator, color='#1a1a1a', linewidth=2, solid_capstyle='round')
ax.plot(x, y_validator, color='#1a1a1a', linewidth=2, solid_capstyle='round')

# Draw horizontal dashed lines
ax.axhline(y=y_total, color='#1a1a1a', linestyle='--', linewidth=1.5)
ax.axhline(y=y_dao_bottom, color='#1a1a1a', linestyle=':', linewidth=1.2)

# Add labels for each region
ax.text(5.5, 0.10, 'L2 Operator', fontsize=18, fontweight='medium', 
        ha='center', va='center', color='#1a1a1a')
ax.text(5.5, 0.32, 'L2 Validator', fontsize=18, fontweight='medium', 
        ha='center', va='center', color='#1a1a1a')
ax.text(5.5, 0.70, 'DAO', fontsize=18, fontweight='medium', 
        ha='center', va='center', color='#1a1a1a')

# Clean up the axes
ax.set_xlim(-0.5, 11.5)
ax.set_ylim(-0.08, 1.05)
ax.set_xticks([])
ax.set_yticks([])

# Remove all spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Remove grid
ax.grid(False)

# Draw custom arrows for axes
arrow_style = dict(arrowstyle='->', color='#1a1a1a', lw=2, 
                   mutation_scale=15)

# X-axis arrow
ax.annotate('', xy=(11, 0), xytext=(0, 0),
            arrowprops=arrow_style)

# Y-axis arrow  
ax.annotate('', xy=(0, 1.0), xytext=(0, 0),
            arrowprops=arrow_style)

# Labels at arrow ends
# Y-axis label at top (above arrow)
ax.text(0.3, 0.95, 'Seigniorage', fontsize=16, fontweight='medium',
        ha='left', va='bottom', color='#1a1a1a')

# "Total annual Seigniorage" annotation on the left
ax.text(-0.15, y_total, 'Total annual\nSeigniorage', fontsize=15,
        ha='right', va='center', color='#1a1a1a')

# X-axis labels: sigma TVL in center, Performance text at right end
ax.text(5.5, -0.02, r'$\sum TVL_i$', fontsize=16,
        ha='center', va='top', color='#1a1a1a')
ax.text(9.0, -0.02, 'TVL; Performance of L2', fontsize=16,
        ha='left', va='top', color='#1a1a1a')

plt.tight_layout()
plt.savefig('basic_tokenomics_model_without_burn_improved.png', 
            dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.show()