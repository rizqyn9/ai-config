"""drawlib: draw.io page helpers for architect-style diagrams (zone, subnet, card, edge, header, legend).
Extracted from the BytePlus review set. Build pages by calling the helpers, close each with end_page(), then write(path).
Icons: draw.io alibaba_cloud stencils as generic service glyphs, recoloured by card kind (edit ICON for other sets)."""
import sys
from xml.sax.saxutils import escape

INK, MUTED, FONT = "#172033", "#56657A", "Helvetica"
BP, GREEN, ORANGE, GREY, RED, TEAL = "#3370FF", "#2E7D32", "#E65100", "#8A97A8", "#C62828", "#00897B"
CARD = {  # fill, stroke, dashed
    "core": ("#FFFFFF", "#9FB3C8", False),
    "product": ("#EEF8F0", GREEN, False),
    "gateway": ("#FFF4E8", ORANGE, False),
    "routed": ("#E6F6F4", TEAL, False),
    "planned": ("#F4F6F8", GREY, True),
    "guard": ("#FDECEC", RED, False),
    "temp": ("#FFF8E1", "#F9A825", True),
}
ICON = {  # stencil, w, h
    "nat": ("nat_gateway", 34, 28), "clb": ("clb_classic_load_balancer_01", 34, 29),
    "vke": ("ask_ack_container_service_for_kubernetes", 28, 32), "pool": ("ess_elastic_scaling_service", 36, 20),
    "pg": ("postgresql", 30, 30), "ecs": ("ecs_elastic_compute_service", 32, 29),
    "bastion": ("bastionhost", 36, 29), "tr": ("tr_transit_router", 30, 30), "vpc": ("vpc_virtual_private_cloud", 34, 22),
    "oss": ("oss_object_storage_service", 34, 26), "acr": ("acr_cloud_container_registry", 26, 30),
    "user": ("user", 30, 30), "vpn": ("vpn_gateway", 30, 30), "fw": ("cfw_cloud_firewall", 36, 25),
    "router": ("router", 28, 30), "gw": ("slb_server_load_balancer_01", 34, 29),
}
ICON_COLOR = {"core": BP, "product": GREEN, "gateway": ORANGE, "routed": TEAL, "planned": GREY, "guard": RED, "temp": "#F9A825"}

pages, cells, n = [], [], [0]


def nid(p="c"):
    n[0] += 1
    return f"{p}{n[0]}"


def put(i, value, style, x, y, w, h):
    cells.append(f'<mxCell id="{i}" value="{escape(value, {chr(34): "&quot;"})}" style="{style}" vertex="1" parent="1">'
                 f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    return i


def zone(x, y, w, h, title, stroke, fill="none", dashed=False, size=15, bold=True):
    d = "dashed=1;dashPattern=8 4;" if dashed else ""
    st = (f"rounded=1;arcSize=2;html=1;whiteSpace=wrap;fillColor={fill};strokeColor={stroke};strokeWidth=1.5;{d}"
          f"align=left;verticalAlign=top;spacingLeft=14;spacingTop=8;fontSize={size};fontColor={INK};fontFamily={FONT};"
          + ("fontStyle=1;" if bold else ""))
    return put(nid("z"), title, st, x, y, w, h)


def subnet(x, y, w, h, title, routed=False):
    fill, stroke = ("#F0FAF8", TEAL) if routed else ("#F7F9FC", "#C7D3E3")
    st = (f"rounded=1;arcSize=4;html=1;whiteSpace=wrap;fillColor={fill};strokeColor={stroke};strokeWidth=1;dashed=1;dashPattern=4 3;"
          f"align=left;verticalAlign=top;spacingLeft=12;spacingTop=6;fontSize=12;fontColor={MUTED};fontFamily={FONT};")
    return put(nid("s"), title, st, x, y, w, h)


def strip(x, y, w, h, title):
    st = (f"rounded=1;arcSize=6;html=1;whiteSpace=wrap;fillColor=#F7F9FC;strokeColor=#C7D3E3;strokeWidth=1;dashed=1;dashPattern=4 3;"
          f"align=left;verticalAlign=middle;spacingLeft=12;fontSize=12;fontColor={MUTED};fontFamily={FONT};")
    return put(nid("s"), title, st, x, y, w, h)


def icon(kind, x, y, color):
    s, w, h = ICON[kind]
    st = f"points=[];aspect=fixed;html=1;align=center;shadow=0;dashed=0;fillColor={color};strokeColor=none;shape=mxgraph.alibaba_cloud.{s};"
    return put(nid("i"), "", st, x, y, w, h)


def card(x, y, w, h, title, sub="", k="core", ic=None):
    f, s, dashed = CARD[k]
    d = "dashed=1;dashPattern=6 4;" if dashed else ""
    left = 56 if ic else 14
    v = f"<b>{escape(title)}</b>"
    if sub:
        v += f'<br><font style="font-size:12px" color="{MUTED}">{sub}</font>'
    st = (f"rounded=1;arcSize=8;html=1;whiteSpace=wrap;fillColor={f};strokeColor={s};strokeWidth=1.2;{d}"
          f"align=left;verticalAlign=middle;spacingLeft={left};spacingRight=8;fontSize=14;fontColor={INK};fontFamily={FONT};")
    i = put(nid("k"), v, st, x, y, w, h)
    if ic:
        _, iw, ih = ICON[ic]
        icon(ic, x + 12 + (36 - iw) // 2, y + (h - ih) // 2, ICON_COLOR[k])
    return i


def text(x, y, w, h, t, size=12, bold=False, color=MUTED, align="left"):
    st = (f"text;html=1;strokeColor=none;fillColor=none;align={align};verticalAlign=middle;whiteSpace=wrap;"
          f"fontSize={size};fontColor={color};fontFamily={FONT};" + ("fontStyle=1;" if bold else ""))
    return put(nid("t"), t, st, x, y, w, h)


def edge(a, b, label, color, width=2.0, dashed=False, both=False, exit_=(0.5, 1), entry=(0.5, 0), pos=None, end=True):
    i = nid("e")
    st = (f"edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor={color};strokeWidth={width};fontSize=12;"
          f"fontColor={INK};fontFamily={FONT};labelBackgroundColor=#FFFFFF;"
          + ("endArrow=blockThin;endFill=1;" if end else "endArrow=none;")
          + ("startArrow=blockThin;startFill=1;" if both else "") + ("dashed=1;dashPattern=8 5;" if dashed else "")
          + f"exitX={exit_[0]};exitY={exit_[1]};exitDx=0;exitDy=0;entryX={entry[0]};entryY={entry[1]};entryDx=0;entryDy=0;")
    geo = f'<mxGeometry x="{pos}" relative="1" as="geometry"/>' if pos is not None else '<mxGeometry relative="1" as="geometry"/>'
    cells.append(f'<mxCell id="{i}" value="{escape(label)}" style="{st}" edge="1" parent="1" source="{a}" target="{b}">{geo}</mxCell>')


def sample_line(x, y, label, color, width=2.0, dashed=False):
    i = nid("l")
    st = (f"endArrow=blockThin;endFill=1;html=1;strokeColor={color};strokeWidth={width};"
          + ("dashed=1;dashPattern=8 5;" if dashed else ""))
    cells.append(f'<mxCell id="{i}" value="" style="{st}" edge="1" parent="1"><mxGeometry relative="1" as="geometry">'
                 f'<mxPoint x="{x}" y="{y}" as="sourcePoint"/><mxPoint x="{x + 56}" y="{y}" as="targetPoint"/></mxGeometry></mxCell>')
    text(x + 66, y - 14, 300, 28, label)


def header(title, subtitle, tag="<b>Proposal</b> · v1 · YYYY-MM-DD", src="source-doc.md", team="DevOps", page_w=2420):
    text(40, 18, 1700, 40, title, 28, True, INK)
    text(40, 58, 1900, 24, subtitle, 13)
    put(nid("m"), f'{tag}<br><font color="{MUTED}">{team} · source: {src}</font>',
        f"rounded=1;arcSize=10;html=1;whiteSpace=wrap;fillColor=#FFFFFF;strokeColor=#9FB3C8;align=left;verticalAlign=middle;"
        f"spacingLeft=14;fontSize=13;fontColor={INK};fontFamily={FONT};", page_w - 380, 22, 350, 60)


def end_page(pid, name, w, h):
    global cells
    pages.append(f'<diagram id="{pid}" name="{name}"><mxGraphModel dx="{w}" dy="{h}" grid="1" gridSize="10" page="1" '
                 f'pageWidth="{w}" pageHeight="{h}"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
                 + "".join(cells) + "</root></mxGraphModel></diagram>")
    cells = []


def legend(y, kinds, extra_lines=()):
    """kinds: [(label, CARD key)]; extra_lines: [(label, colour, width, dashed)] sample edges."""
    zone(30, y, 1610, 110, "Legend", "#C7D3E3", "#FFFFFF", size=13)
    for k, (t, kind) in enumerate(kinds):
        card(50 + k * 312, y + 36, 292, 30, t, k=kind)
    for k, (t, c, w, d) in enumerate(extra_lines):
        sample_line(60 + k * 390, y + 86, t, c, w, d)
def write(path):
    """Write all finished pages (end_page) as one multi-page .drawio file."""
    open(path, "w").write("<mxfile>" + "".join(pages) + "</mxfile>")
