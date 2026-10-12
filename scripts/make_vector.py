import re
import os

def build_animated_portrait(input_file="source-photo.svg", output_file="om-vector.svg"):
    if not os.path.exists(input_file):
        print(f"[!] Error: {input_file} not found in the current directory.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    paths = re.findall(r'd="([^"]+)"', content)

    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="425" height="425" viewBox="0 0 425 425">',
        '  <defs>',
        '    <style>',
        '      .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1; }',
        '      .line {',
        '        fill: none;',
        '        stroke: #a371f7; /* Terminal neon purple */',
        '        stroke-width: 4;',
        '        stroke-linecap: round;',
        '        stroke-linejoin: round;',
        '        stroke-dasharray: 100;',
        '        stroke-dashoffset: 100;',
        '        animation: draw 1.33s cubic-bezier(0.25, 1, 0.5, 1) forwards;',
        '      }',
        '      @keyframes draw { to { stroke-dashoffset: 0; } }',
        '    </style>',
        '    <filter id="glow">',
        '      <feGaussianBlur stdDeviation="1.5" result="blur" />',
        '      <feComposite in="SourceGraphic" in2="blur" operator="over" />',
        '    </filter>',
        '  </defs>',
        '  <rect class="bg" width="100%" height="100%" rx="8" />',
        '  <!-- Terminal Window Controls -->',
        '  <circle cx="20" cy="20" r="5" fill="#ff5f56" />',
        '  <circle cx="36" cy="20" r="5" fill="#ffbd2e" />',
        '  <circle cx="52" cy="20" r="5" fill="#27c93f" />',
        '  <!-- Scaled Inner Canvas -->',
        '  <svg x="10" y="30" width="405" height="385" viewBox="0 0 1178 1600">',
        '    <g filter="url(#glow)">'
    ]

    # 3x faster stagger timing
    for i, d in enumerate(paths):
        delay = i * 0.026
        svg.append(f'      <path pathLength="100" class="line" style="animation-delay: {delay:.3f}s" d="{d}" />')

    svg.append('    </g>')
    svg.append('  </svg>')
    svg.append('</svg>')

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"[+] Successfully converted {input_file} -> {output_file} (Fast Purple Wireframe)")

if __name__ == "__main__":
    build_animated_portrait()
