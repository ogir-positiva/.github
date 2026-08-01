"""Convierte texto a paths SVG usando Inter, con shaping y kerning reales (HarfBuzz)."""
import io
from functools import lru_cache

import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

SRC = "inter/InterVariable.ttf"


@lru_cache(maxsize=None)
def _instance(wght: float, opsz: float):
    """Instancia estática de la fuente variable para un peso y tamaño óptico dados."""
    tt = instancer.instantiateVariableFont(
        TTFont(SRC), {"wght": wght, "opsz": opsz}, inplace=False, updateFontNames=False
    )
    buf = io.BytesIO()
    tt.save(buf)
    data = buf.getvalue()
    return tt, data


def typeset(text, size, x, y, wght=400, opsz=None, tracking=0.0):
    """Devuelve (path_d, ancho_total). `tracking` en unidades SVG por glifo."""
    opsz = opsz if opsz is not None else max(14.0, min(32.0, size))
    tt, data = _instance(wght, opsz)

    face = hb.Face(data)
    font = hb.Font(face)
    upem = face.upem
    font.scale = (upem, upem)
    hb.ot_font_set_funcs(font)

    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)

    glyph_order = tt.getGlyphOrder()
    glyph_set = tt.getGlyphSet()
    scale = size / upem

    pen = SVGPathPen(glyph_set, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    cursor = 0.0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        name = glyph_order[info.codepoint]
        tx = x + cursor + pos.x_offset * scale
        ty = y - pos.y_offset * scale
        glyph_set[name].draw(TransformPen(pen, Transform(scale, 0, 0, -scale, tx, ty)))
        cursor += pos.x_advance * scale + tracking

    return pen.getCommands(), cursor - tracking


def width(text, size, wght=400, opsz=None, tracking=0.0):
    return typeset(text, size, 0, 0, wght, opsz, tracking)[1]
