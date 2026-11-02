"""Generate assets/terminal.svg, the animated terminal at the top of README.md.

Edit SESSION below, then rerun: python build_terminal_svg.py
"""
import html
import os

SVG_PATH = "assets/terminal.svg"

# (command, output). The last command has no output; the cursor stays there
# and the README below reads as its output.
SESSION = [
    ("whoami",        "Bruce Huang · AI Engineer · Medical AI"),
    ("echo $MISSION", "Building AI that works reliably in the real world"),
    ("cat README.md", None),
]
PROMPT = [("bruce@github", "user"), (":", "fg"), ("~", "path"), ("$ ", "fg")]

FONT_SIZE    = 15
CHAR_W       = 9.0          # every line is stretched to this grid via textLength,
                            # so the typing steps line up whatever monospace font loads
LINE_H       = 24
PAD_X        = 22
TITLE_BAR_H  = 36
FIRST_LINE_Y = TITLE_BAR_H + 30

TYPE_SPEED   = 0.09         # seconds per character
START_DELAY  = 0.8
THINK_DELAY  = 0.6          # new prompt shown → typing starts
ENTER_DELAY  = 0.4          # typing done → output shown
NEXT_DELAY   = 0.15         # output shown → next prompt shown

COLORS = {
    "bg"    : "#0d1117",
    "bar"   : "#161b22",
    "border": "#30363d",
    "title" : "#8b949e",
    "fg"    : "#e6edf3",
    "out"   : "#c9d1d9",
    "user"  : "#3fb950",
    "path"  : "#58a6ff",
}

def show(at, until=None):
    animation = f"show .01s steps(1) {at:.2f}s forwards"
    if until is not None:
        animation += f", hide .01s steps(1) {until:.2f}s forwards"
    return f'class="hidden" style="animation: {animation}"'

def text(x, y, chars, body, cls=""):
    cls_attr = f' class="{cls}"' if cls else ""
    return (
        f'<text x="{x}" y="{y}" textLength="{chars * CHAR_W:g}"{cls_attr}>'
        f"{body}</text>"
    )

def build():
    prompt_len  = sum(len(part) for part, _ in PROMPT)
    prompt_body = "".join(
        f'<tspan class="{cls}">{html.escape(part)}</tspan>' for part, cls in PROMPT
    )
    longest = max(
        max(prompt_len + len(cmd), len(out or "")) for cmd, out in SESSION
    )
    width  = round(2 * PAD_X + (longest + 1) * CHAR_W)
    rows   = 2 * len(SESSION) - 1
    height = FIRST_LINE_Y + (rows - 1) * LINE_H + 22

    keyframes = []
    body      = []
    t   = 0.0
    row = 0
    for i, (cmd, out) in enumerate(SESSION):
        y       = FIRST_LINE_Y + row * LINE_H
        cmd_x   = PAD_X + prompt_len * CHAR_W
        cmd_w   = len(cmd) * CHAR_W
        shown   = t
        t      += START_DELAY if i == 0 else THINK_DELAY
        type_at = t
        type_s  = len(cmd) * TYPE_SPEED
        t      += type_s
        cursor_until = None
        if out is not None:
            t += ENTER_DELAY
            cursor_until = t

        # A background-coloured cover slides right one character per step,
        # revealing the command; the cursor rides along with it
        keyframes.append(
            f"@keyframes type{i} {{ to {{ transform: translateX({cmd_w:g}px); }} }}"
        )
        typing = f"animation: type{i} {type_s:.2f}s steps({len(cmd)}, end) {type_at:.2f}s forwards"
        body.append(
            f'<g {show(shown)}>'
            + text(PAD_X, y, prompt_len + len(cmd),
                   prompt_body + f'<tspan class="fg">{html.escape(cmd)}</tspan>')
            + f'<rect class="move" x="{cmd_x:g}" y="{y - LINE_H + 7}" width="{cmd_w + 2:g}" '
              f'height="{LINE_H}" fill="{COLORS["bg"]}" style="{typing}"/>'
            + "</g>"
        )
        body.append(
            f'<g {show(shown, cursor_until)}><g class="move" style="{typing}">'
            f'<rect class="blink" x="{cmd_x:g}" y="{y - FONT_SIZE + 2}" width="{CHAR_W:g}" '
            f'height="{FONT_SIZE + 3}" fill="{COLORS["fg"]}"/></g></g>'
        )
        row += 1

        if out is not None:
            y = FIRST_LINE_Y + row * LINE_H
            body.append(
                f'<g {show(t)}>' + text(PAD_X, y, len(out), html.escape(out), "out") + "</g>"
            )
            t   += NEXT_DELAY
            row += 1

    alt = "  ".join(
        f"$ {cmd}" + (f" → {out}" if out else "") for cmd, out in SESSION
    )
    c = COLORS
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" xml:space="preserve" role="img" aria-label="{html.escape(alt)}">
<title>{html.escape(alt)}</title>
<style>
text {{ font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; font-size: {FONT_SIZE}px; fill: {c["fg"]}; }}
.user {{ fill: {c["user"]}; }}
.path {{ fill: {c["path"]}; }}
.fg {{ fill: {c["fg"]}; }}
.out {{ fill: {c["out"]}; }}
.title {{ font-size: 12px; fill: {c["title"]}; }}
.hidden {{ opacity: 0; }}
.blink {{ animation: blink 1s steps(1) infinite; }}
@keyframes show {{ to {{ opacity: 1; }} }}
@keyframes hide {{ to {{ opacity: 0; }} }}
@keyframes blink {{ 50% {{ opacity: 0; }} }}
{chr(10).join(keyframes)}
@media (prefers-reduced-motion: reduce) {{
  .hidden, .move {{ animation-duration: 0s !important; animation-delay: 0s !important; }}
}}
</style>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="10" fill="{c["bg"]}" stroke="{c["border"]}"/>
<path d="M0.5 {TITLE_BAR_H} V10.5 A10 10 0 0 1 10.5 0.5 H{width - 10.5} A10 10 0 0 1 {width - 0.5} 10.5 V{TITLE_BAR_H} Z" fill="{c["bar"]}"/>
<line x1="0.5" y1="{TITLE_BAR_H}" x2="{width - 0.5}" y2="{TITLE_BAR_H}" stroke="{c["border"]}"/>
<circle cx="20" cy="{TITLE_BAR_H / 2:g}" r="6" fill="#ff5f57"/>
<circle cx="40" cy="{TITLE_BAR_H / 2:g}" r="6" fill="#febc2e"/>
<circle cx="60" cy="{TITLE_BAR_H / 2:g}" r="6" fill="#28c840"/>
<text x="{width / 2:g}" y="{TITLE_BAR_H / 2 + 4:g}" text-anchor="middle" class="title">bruce@github: ~</text>
{chr(10).join(body)}
</svg>
"""

if __name__ == "__main__":
    os.makedirs(os.path.dirname(SVG_PATH), exist_ok=True)
    with open(SVG_PATH, "w", encoding="utf-8") as f:
        f.write(build())
    print(f"{SVG_PATH} written.")
