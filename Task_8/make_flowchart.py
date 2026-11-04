"""Draws the validation flowchart (flowchart_validation.png) with matplotlib."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

fig, ax = plt.subplots(figsize=(7.5, 10))
ax.set_xlim(0, 10.6); ax.set_ylim(0, 20); ax.axis("off")

def box(x, y, text, w=3.6, h=1.0, color="#E8F0FE", rounded=False):
    style = "round,pad=0.02,rounding_size=0.5" if rounded else "square,pad=0.02"
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=style, fc=color, ec="#333", lw=1.2))
    ax.text(x, y, text, ha="center", va="center", fontsize=9)

def diamond(x, y, text, w=4.0, h=1.5):
    ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y), (x, y - h / 2), (x - w / 2, y)], fc="#FFF4CC", ec="#333", lw=1.2))
    ax.text(x, y, text, ha="center", va="center", fontsize=8.5)

def arrow(x1, y1, x2, y2, label=None, lx=0.15, ly=0.1):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", lw=1.2))
    if label:
        ax.text((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, label, fontsize=8.5, color="#a00")

X = 4.0
box(X, 19, "START", rounded=True, color="#D7F5D7")
box(X, 17.4, "INPUT litres, fat, snf")
diamond(X, 15.5, "All three are\nvalid numbers?")
diamond(X, 12.9, "litres > 0 ?")
diamond(X, 10.3, "2.0 <= fat <= 7.0 ?")
diamond(X, 7.7, "6.0 <= snf <= 10.0 ?")
box(X, 5.0, 'OUTPUT "valid"', color="#D7F5D7")
box(X, 3.2, "END", rounded=True, color="#D7F5D7")
for y, label in [(15.5, 'OUTPUT "invalid: not a number"'), (12.9, 'OUTPUT "invalid: litres"'),
                 (10.3, 'OUTPUT "invalid: fat"'), (7.7, 'OUTPUT "invalid: snf"')]:
    box(8.2, y, label, w=3.2, h=1.0, color="#FADBD8")
    arrow(X + 2.0, y, 8.2 - 1.6, y, "NO", ly=0.15)
    ax.plot([9.8, 10.2], [y, y], color="#333", lw=1.0)
ax.plot([10.2, 10.2], [15.5, 3.2], color="#333", lw=1.0)
ax.annotate("", xy=(X + 1.8, 3.2), xytext=(10.2, 3.2), arrowprops=dict(arrowstyle="->", lw=1.2))
arrow(X, 18.5, X, 17.9)
arrow(X, 16.9, X, 16.25)
arrow(X, 14.75, X, 13.65, "YES")
arrow(X, 12.15, X, 11.05, "YES")
arrow(X, 9.55, X, 8.45, "YES")
arrow(X, 6.95, X, 5.5, "YES")
arrow(X, 4.5, X, 3.7)
ax.set_title("Flowchart: validating one milk entry", fontsize=12, pad=8)
plt.tight_layout()
plt.savefig("flowchart_validation.png", dpi=130)
