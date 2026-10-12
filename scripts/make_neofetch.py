import json
import re

def make_neofetch_card(json_path="data/contributions.json", output_file="info-card.svg"):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        days = data.get("days", [])
        total_summary = data.get("total_summary", "")
    except Exception:
        print("[!] No contributions.json found.")
        days = []
        total_summary = ""

    # Calculate true stats mathematically
    active_days = 0
    longest_streak = 0
    temp_streak = 0
    current_streak = 0
    total_contribs = 0

    for day in days:
        level = day.get("level", 0)
        count = day.get("count", level * 2)
        total_contribs += count
        
        if level > 0:
            active_days += 1
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 0
            
    for day in reversed(days):
        if day.get("level", 0) > 0:
            current_streak += 1
        else:
            break

    match = re.search(r'^([\d,]+)\s', total_summary)
    total_str = match.group(1) if match else str(total_contribs)
    
    total_days = max(len(days), 365)
    active_percent = int((active_days / total_days) * 100) if total_days > 0 else 0

    svg_lines = []
    y_offset = 55

    # Neofetch Data Payload
    data_rows = [
        ("OS", "Windows 11, Omarchy Quatro"),
        ("Uptime", "21 years, 11 months, 29 days"),
        ("Host", "KIIT University"),
        ("Kernel", "Computer Science Engineering"),
        ("IDE", "VS Code, Terminal"),
        ("BLANK", ""),
        ("Languages.Programming", "Python, C++, JavaScript"),
        ("Languages.Computer", "HTML, CSS, JSON"),
        ("Languages.Real", "English, Hindi"),
        ("BLANK", ""),
        ("Hobbies.Software", "Open Source, Web Dev"),
        ("Hobbies.Physical", "Custom Mech Keyboards, Chess, Anime"),
        ("HEADER", "- Contact "),
        ("Email.Personal", "omranhi732@gmail.com"),
        ("LinkedIn", "OmChaitanyaSharma"),
        ("Instagram", "omchaitanyasharma"),
        ("HEADER", "- GitHub Stats "),
        ("Contributions", f"{total_str} (Last Year)"),
        ("Current Streak", f"{current_streak} days"),
        ("Longest Streak", f"{longest_streak} days"),
        ("Active Days", f"{active_days} / {total_days} ({active_percent}%)")
    ]

    for key, val in data_rows:
        if key == "BLANK":
            y_offset += 14
            continue
        elif key == "HEADER":
            dots = "-" * (44 - len(val))
            svg_lines.append(f'<text x="20" y="{y_offset}" class="txt"><tspan class="title">{val}</tspan><tspan class="dot">{dots}</tspan></text>')
            y_offset += 18
            continue

        # Terminal dot-leader alignment calculation
        key_str = key + ":"
        dots_needed = 24 - len(key_str)
        dots_str = "." * dots_needed
        
        line = f'<text x="20" y="{y_offset}" class="txt" xml:space="preserve"><tspan class="key">{key_str}</tspan> <tspan class="dot">{dots_str}</tspan> <tspan class="val">{val}</tspan></text>'
        svg_lines.append(line)
        y_offset += 18

    svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="440" height="460" viewBox="0 0 440 460">
  <defs>
    <style>
      .txt {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12px; }}
      .key {{ fill: #e3b341; font-weight: bold; }}
      .dot {{ fill: #484f58; }}
      .val {{ fill: #58a6ff; }}
      .title {{ fill: #adbac7; font-weight: bold; }}
      .fade {{ opacity: 0; animation: fadeIn 1s ease-in forwards; }}
      @keyframes fadeIn {{ to {{ opacity: 1; }} }}
    </style>
  </defs>
  <rect width="100%" height="100%" fill="#0d1117" rx="8" stroke="#30363d" stroke-width="1" />
  
  <circle cx="20" cy="20" r="4" fill="#ff5f56" />
  <circle cx="34" cy="20" r="4" fill="#ffbd2e" />
  <circle cx="48" cy="20" r="4" fill="#27c93f" />
  
  <g class="fade">
      <text x="20" y="55" class="txt" xml:space="preserve"><tspan class="title">Om_Chaitanya_Sharma@github</tspan> <tspan class="dot">-----------------</tspan></text>
      <g transform="translate(0, 20)">
        {chr(10).join(svg_lines)}
      </g>
  </g>
</svg>"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(svg_template)
    print(f"[+] Neofetch card generated: {output_file}")

if __name__ == "__main__":
    make_neofetch_card()
