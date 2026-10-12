import json
import re

def make_stats_card(json_path="data/contributions.json", output_file="stats-card.svg"):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        days = data.get("days", [])
    except Exception:
        print("[!] No contributions.json found. Run contributions.sh first.")
        days = []

    # Calculate true stats mathematically
    active_days = 0
    longest_streak = 0
    temp_streak = 0
    current_streak = 0
    total_contribs = 0

    # Calculate totals, active days, and longest streak
    for day in days:
        level = day.get("level", 0)
        # We assume level 1 is roughly 1-3 commits, level 2 is 4-6, etc.
        # But for total contributions, we just want a rough accurate sum if exact count isn't in JSON.
        # If your JSON has a "count" field, use it. Otherwise, we estimate from levels.
        count = day.get("count", level * 2) 
        total_contribs += count
        
        if level > 0:
            active_days += 1
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 0
            
    # Find current streak by counting backwards from today
    for day in reversed(days):
        if day.get("level", 0) > 0:
            current_streak += 1
        else:
            break

    # If the JSON has a specific total_summary string, extract the exact number from it
    total_summary = data.get("total_summary", "")
    match = re.search(r'^([\d,]+)\s', total_summary)
    if match:
        total_str = match.group(1)
    else:
        total_str = str(total_contribs)
    
    total_days = max(len(days), 365)
    active_percent = int((active_days / total_days) * 100) if total_days > 0 else 0

    svg_template = """<svg xmlns="http://www.w3.org/2000/svg" width="425" height="425" viewBox="0 0 425 425">
  <defs>
    <style>
      .text { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
      .prompt { font-size: 11px; fill: #768390; }
      .num { font-size: 28px; font-weight: bold; fill: #adbac7; }
      .highlight { fill: #39d353; }
      .sub { font-size: 10px; fill: #484f58; }
      .bar { fill: #26a641; transform-origin: bottom; animation: grow 1s ease-out forwards; }
      @keyframes grow { from { transform: scaleY(0); } to { transform: scaleY(1); } }
      .fade { opacity: 0; animation: fadeIn 1s ease-in forwards; }
      @keyframes fadeIn { to { opacity: 1; } }
    </style>
  </defs>

  <rect width="100%" height="100%" fill="#0d1117" rx="8" stroke="#30363d" stroke-width="1" />
  
  <circle cx="20" cy="20" r="4" fill="#484f58" />
  <circle cx="34" cy="20" r="4" fill="#484f58" />
  <circle cx="48" cy="20" r="4" fill="#484f58" />

  <g transform="translate(30, 60)" class="text fade">
    <!-- Top Row -->
    <text x="0" y="0" class="prompt">$ current streak</text>
    <text x="0" y="35" class="num highlight">[CURRENT_STREAK] <tspan class="prompt" font-size="12px">days</tspan></text>

    <text x="200" y="0" class="prompt">$ longest streak</text>
    <text x="200" y="35" class="num">[LONGEST_STREAK] <tspan class="prompt" font-size="12px">days</tspan></text>

    <line x1="0" y1="80" x2="365" y2="80" stroke="#21262d" stroke-width="1" />

    <!-- Middle Row -->
    <text x="0" y="110" class="prompt">$ total contributions</text>
    <text x="0" y="145" class="num">[TOTAL_CONTRIBS]</text>
    <text x="0" y="165" class="sub">in the last year</text>

    <text x="200" y="110" class="prompt">$ active days</text>
    <text x="200" y="145" class="num">[ACTIVE_DAYS] <tspan class="prompt" font-size="12px">/ [TOTAL_DAYS]</tspan></text>
    <text x="200" y="165" class="sub">[PERCENT]% of the year</text>

    <line x1="0" y1="190" x2="365" y2="190" stroke="#21262d" stroke-width="1" />

    <!-- Chart Section (Visual Wave) -->
    <text x="0" y="220" class="prompt">$ activity wave</text>
    <g transform="translate(0, 330)">
      <rect x="0" y="-30" width="18" height="30" class="bar" style="animation-delay: 0.1s" />
      <rect x="30" y="-45" width="18" height="45" class="bar" style="animation-delay: 0.2s" />
      <rect x="60" y="-20" width="18" height="20" class="bar" style="animation-delay: 0.3s" />
      <rect x="90" y="-80" width="18" height="80" class="bar highlight" style="animation-delay: 0.4s" />
      <rect x="120" y="-55" width="18" height="55" class="bar" style="animation-delay: 0.5s" />
      <rect x="150" y="-40" width="18" height="40" class="bar" style="animation-delay: 0.6s" />
      <rect x="180" y="-65" width="18" height="65" class="bar" style="animation-delay: 0.7s" />
      <rect x="210" y="-35" width="18" height="35" class="bar" style="animation-delay: 0.8s" />
      <rect x="240" y="-50" width="18" height="50" class="bar" style="animation-delay: 0.9s" />
      <rect x="270" y="-25" width="18" height="25" class="bar" style="animation-delay: 1.0s" />
      <rect x="300" y="-60" width="18" height="60" class="bar" style="animation-delay: 1.1s" />
      <rect x="330" y="-40" width="18" height="40" class="bar" style="animation-delay: 1.2s" />
    </g>
  </g>
</svg>"""

    # Inject true numbers
    svg = svg_template.replace("[CURRENT_STREAK]", str(current_streak))
    svg = svg.replace("[LONGEST_STREAK]", str(longest_streak))
    svg = svg.replace("[TOTAL_CONTRIBS]", str(total_str))
    svg = svg.replace("[ACTIVE_DAYS]", str(active_days))
    svg = svg.replace("[TOTAL_DAYS]", str(total_days))
    svg = svg.replace("[PERCENT]", str(active_percent))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[+] Re-rendered stats dashboard with TRUE live data to {output_file}")

if __name__ == "__main__":
    make_stats_card()
