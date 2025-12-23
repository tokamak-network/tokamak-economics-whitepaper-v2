import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('PDF')

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']

FONTSIZE_TITLE = 16
FONTSIZE_LABEL = 14
FONTSIZE_TICK = 12
FONTSIZE_ANNOTATION = 12

# 파라미터
initial_supply = 50_000_000
annual_pre_merge = 9_509_317   # 13초 블록
annual_post_merge = 10_301_760  # 12초 블록
merge_year = 2.1

# Merge 전 (t < 2.1)
t_pre = np.linspace(0, merge_year, 100)
supply_pre = initial_supply + annual_pre_merge * t_pre
infl_pre = annual_pre_merge / supply_pre * 100

# Merge 시점 공급량
supply_at_merge = initial_supply + annual_pre_merge * merge_year

# Merge 후 (t >= 2.1)
t_post = np.linspace(merge_year, 50, 200)
supply_post = supply_at_merge + annual_post_merge * (t_post - merge_year)
infl_post = annual_post_merge / supply_post * 100

fig, ax = plt.subplots(figsize=(10,6))

# 두 구간 그리기
ax.plot(t_pre, infl_pre, color='blue', linewidth=1.5)
ax.plot(t_post, infl_post, color='blue', linewidth=1.5)

# 주요 시점 표시 (0, 10, 50년)
t_pts = [0, 10, 50]
for t in t_pts:
    if t < merge_year:
        supply = initial_supply + annual_pre_merge * t
        infl = annual_pre_merge / supply * 100
    else:
        supply = supply_at_merge + annual_post_merge * (t - merge_year)
        infl = annual_post_merge / supply * 100
    
    ax.scatter(t, infl, color='blue', marker='o', s=50, zorder=5)
    ax.plot([t, t], [0, infl], linestyle='--', color='gray', linewidth=0.7)
    ax.plot([0, t], [infl, infl], linestyle='--', color='gray', linewidth=0.7)
    ax.annotate(
    f"{infl:.1f}%",
    (t, infl),
    textcoords="offset points",
    xytext=(8, -5),
    fontsize=FONTSIZE_ANNOTATION,
    bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.8)
)

# Merge 시점 세로선
ax.axvline(x=merge_year, linestyle='--', color='red', linewidth=1.2)
ax.annotate("Ethereum Merge", (merge_year, 15), textcoords="offset points",
            xytext=(5, 2), fontsize=FONTSIZE_ANNOTATION, color='red')

ax.set_xlabel("Years Since Initial Issuance", fontsize=FONTSIZE_LABEL)
ax.set_ylabel("Inflation Rate (%)", fontsize=FONTSIZE_LABEL)
ax.tick_params(axis='both', labelsize=FONTSIZE_TICK)
ax.grid(True)

plt.savefig('seigniorage_generation.pdf', 
            bbox_inches='tight', facecolor='white', edgecolor='none',
            backend='pdf')
plt.close()