import json

PALETTE = [
    "#161b22",  # 0: Empty (genuine dark)
    "#0e4429",  # 1: Low activity
    "#006d32",  # 2: Moderate activity
    "#26a641",  # 3: High activity
    "#39d353"   # 4: Very high activity
]

SWEEP_COLOR = "#39d353"  # Vibrant neon matrix green

def render_heatmap(json_path="data/contributions.json", output_svg="contrib-heatmap.svg"):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    days = data.get("days", [])
    total_summary = data.get("total_summary", "Contributions in the last year")

    if len(days) > 371:
        days = days[-371:]

    cell_size = 11
    cell_gap = 3
    x_offset = 32
    y_offset = 40

    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="860" height="170" viewBox="0 0 860 170">',
        '  <defs>',
        '    <filter id="neon" x="-30%" y="-30%" width="160%" height="160%">',
        '      <feGaussianBlur stdDeviation="2" result="blur" />',
        '      <feComposite in="SourceGraphic" in2="blur" operator="over" />',
        '    </filter>',
        '    <style>',
        '      .lbl { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 11px; fill: #768390; }',
        '      .box {',
        '        opacity: 0;',
        '        transform-origin: center;',
        '      }',
        '    </style>',
        '  </defs>',
        '  <rect width="100%" height="100%" fill="#0d1117" rx="6" stroke="#30363d" stroke-width="1" />',
        f'  <text x="32" y="24" class="lbl" style="fill: #58a6ff; font-weight: 600;">{total_summary}</text>'
    ]

    for idx, day in enumerate(days):
        col = idx // 7
        row = idx % 7
        x = x_offset + (col * (cell_size + cell_gap))
        y = y_offset + (row * (cell_size + cell_gap))

        level = min(day["level"], 4)
        true_color = PALETTE[level]

        # Wave 1: Rapid diagonal sweep that turns everything glowing green
        sweep_delay = (col * 0.015) + (row * 0.018)
        
        # Wave 2: Settle to authentic color after the full sweep passes through
        settle_delay = sweep_delay + 0.55

        # SMIL animations for smooth browser transitions without CSS keyframe bloat
        anim_markup = (
            f'<animate attributeName="opacity" from="0" to="1" dur="0.15s" begin="{sweep_delay:.3f}s" fill="freeze" />'
            f'<animate attributeName="fill" from="{SWEEP_COLOR}" to="{true_color}" dur="0.45s" begin="{settle_delay:.3f}s" fill="freeze" />'
        )

        svg.append(
            f'  <rect class="box" x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" '
            f'rx="2" fill="{SWEEP_COLOR}">'
            f'{anim_markup}'
            f'</rect>'
        )

    # Legend
    leg_x = 690
    leg_y = 148
    svg.append(f'  <text x="{leg_x - 30}" y="{leg_y + 9}" class="lbl">Less</text>')
    for i, color in enumerate(PALETTE):
        svg.append(f'  <rect x="{leg_x + (i * 15)}" y="{leg_y}" width="10" height="10" rx="2" fill="{color}" />')
    svg.append(f'  <text x="{leg_x + 80}" y="{leg_y + 9}" class="lbl">More</text>')

    svg.append('</svg>')

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"[+] Re-rendered full matrix-to-authentic heatmap at {output_svg}")

if __name__ == "__main__":
    render_heatmap()
