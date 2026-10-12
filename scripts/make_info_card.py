def make_info_card(output_file="info-card.svg"):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="490" height="420" viewBox="0 0 490 420">
  <defs>
    <style>
      .t { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 13px; }
      .prompt { fill: #58a6ff; font-weight: bold; }
      .sep { fill: #484f58; }
      .k { fill: #f0883e; font-weight: bold; }
      .v { fill: #adbac7; }
      .row { opacity: 0; animation: fadeIn 0.4s ease forwards; }
      @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
      }
      .r1 { animation-delay: 0.2s; }
      .r2 { animation-delay: 0.4s; }
      .r3 { animation-delay: 0.6s; }
      .r4 { animation-delay: 0.8s; }
      .r5 { animation-delay: 1.0s; }
      .r6 { animation-delay: 1.2s; }
      .r7 { animation-delay: 1.4s; }
      .r8 { animation-delay: 1.6s; }
    </style>
  </defs>

  <rect width="100%" height="100%" fill="#0d1117" rx="6" stroke="#30363d" stroke-width="1" />

  <circle cx="20" cy="20" r="5" fill="#ff5f56" />
  <circle cx="36" cy="20" r="5" fill="#ffbd2e" />
  <circle cx="52" cy="20" r="5" fill="#27c93f" />

  <g transform="translate(25, 60)" class="t">
    <g class="row r1">
      <text x="0" y="0" class="prompt">om@Om_Chaitanya_Sharma</text>
    </g>
    <g class="row r2">
      <text x="0" y="20" class="sep">-------------------------------------</text>
    </g>
    <g class="row r3">
      <text x="0" y="55" class="k">OS</text>
      <text x="110" y="55" class="v">GitHub Linux x86_64</text>
    </g>
    <g class="row r4">
      <text x="0" y="85" class="k">Role</text>
      <text x="110" y="85" class="v">Software Developer</text>
    </g>
    <g class="row r5">
      <text x="0" y="115" class="k">Stack</text>
      <text x="110" y="115" class="v">Python, MERN, HTML5, CSS3, JavaScript</text>
    </g>
    <g class="row r6">
      <text x="0" y="145" class="k">Core Focus</text>
      <text x="110" y="145" class="v">Full-Stack Engineering &amp; Systems</text>
    </g>
    <g class="row r7">
      <text x="0" y="175" class="k">Uptime</text>
      <text x="110" y="175" class="v">Active daily / Commit-driven</text>
    </g>
    <g class="row r8">
      <text x="0" y="215" class="k">Palette</text>
      <rect x="110" y="203" width="16" height="16" rx="3" fill="#161b22" />
      <rect x="132" y="203" width="16" height="16" rx="3" fill="#0e4429" />
      <rect x="154" y="203" width="16" height="16" rx="3" fill="#006d32" />
      <rect x="176" y="203" width="16" height="16" rx="3" fill="#26a641" />
      <rect x="198" y="203" width="16" height="16" rx="3" fill="#39d353" />
    </g>
  </g>
</svg>"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"[+] Generated {output_file}")

if __name__ == "__main__":
    make_info_card()
