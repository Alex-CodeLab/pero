#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import sys
from .enum import Enum
from .values import *

# define line splitting character
LINE_SPLITTER = "\n"

# define default fonts
FONT_FACE_SERIF = "Times New Roman"
FONT_FACE_SANS = "Arial"
FONT_FACE_MONO = "Courier New"

if sys.platform == 'darwin':
    FONT_FACE_SERIF = "Times"
    FONT_FACE_SANS = "Helvetica"
    FONT_FACE_MONO = "Courier"

# define font families
FONT_FAMILY_SERIF = SERIF
FONT_FAMILY_SANS = SANS
FONT_FAMILY_MONO = MONO

FONT_FAMILY = Enum(
    SERIF = FONT_FAMILY_SERIF,
    SANS = FONT_FAMILY_SANS,
    MONO = FONT_FAMILY_MONO)

# define font families default names
FONT_FAMILY_NAMES = {
    FONT_FAMILY_SERIF: (FONT_FACE_SERIF, 'times', 'Times', 'Times New Roman'),
    FONT_FAMILY_SANS: (FONT_FACE_SANS, 'arial', 'Arial', 'Helvetica'),
    FONT_FAMILY_MONO: (FONT_FACE_MONO, 'courier', 'Courier', 'Courier New')}

# define font styles
FONT_STYLE_NORMAL = NORMAL
FONT_STYLE_ITALIC = ITALIC

FONT_STYLE = Enum(
    NORMAL = FONT_STYLE_NORMAL,
    ITALIC = FONT_STYLE_ITALIC)

# define font weight
FONT_WEIGHT_NORMAL = NORMAL
FONT_WEIGHT_LIGHT = LIGHT
FONT_WEIGHT_BOLD = BOLD
FONT_WEIGHT_BLACK = BLACK
FONT_WEIGHT_HEAVY = HEAVY
FONT_WEIGHT_SEMIBOLD = SEMIBOLD
FONT_WEIGHT_MEDIUM = MEDIUM
FONT_WEIGHT_ULTRALIGHT = ULTRALIGHT
FONT_WEIGHT_THIN = THIN

FONT_WEIGHT = Enum(
    NORMAL = FONT_WEIGHT_NORMAL,
    LIGHT = FONT_WEIGHT_LIGHT,
    BOLD = FONT_WEIGHT_BOLD,
    BLACK = FONT_WEIGHT_BLACK,
    HEAVY = FONT_WEIGHT_HEAVY,
    SEMIBOLD = FONT_WEIGHT_SEMIBOLD,
    MEDIUM = FONT_WEIGHT_MEDIUM,
    ULTRALIGHT = FONT_WEIGHT_ULTRALIGHT,
    THIN = FONT_WEIGHT_THIN)

# define font weight light values
FONT_WEIGHTS_LIGHT = {
    FONT_WEIGHT_LIGHT,
    FONT_WEIGHT_ULTRALIGHT,
    FONT_WEIGHT_THIN}

# define font weight bold values
FONT_WEIGHTS_BOLD = {
    FONT_WEIGHT_BOLD,
    FONT_WEIGHT_BLACK,
    FONT_WEIGHT_HEAVY,
    FONT_WEIGHT_SEMIBOLD}

# define text align
TEXT_ALIGN_LEFT = LEFT
TEXT_ALIGN_CENTER = CENTER
TEXT_ALIGN_RIGHT = RIGHT

TEXT_ALIGN = Enum(
    LEFT = TEXT_ALIGN_LEFT,
    CENTER = TEXT_ALIGN_CENTER,
    RIGHT = TEXT_ALIGN_RIGHT)

# define text baseline
TEXT_BASE_TOP = TOP
TEXT_BASE_MIDDLE = MIDDLE
TEXT_BASE_BOTTOM = BOTTOM

TEXT_BASE = Enum(
    TOP = TEXT_BASE_TOP,
    MIDDLE = TEXT_BASE_MIDDLE,
    BOTTOM = TEXT_BASE_BOTTOM)

# define polar text rotation
TEXT_ROT_NONE = NONE
TEXT_ROT_FOLLOW = FOLLOW
TEXT_ROT_NATURAL = NATURAL
TEXT_ROT_FACEOUT = FACEOUT
TEXT_ROT_FACEIN = FACEIN

TEXT_ROTATION = Enum(
    NONE = TEXT_ROT_NONE,
    FOLLOW = TEXT_ROT_FOLLOW,
    NATURAL = TEXT_ROT_NATURAL,
    FACEOUT = TEXT_ROT_FACEOUT,
    FACEIN = TEXT_ROT_FACEIN)
