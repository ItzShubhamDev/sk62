import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kb import data_pin
from kmk.modules.split import Split, SplitSide

keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP16, board.GP17, board.GP26, board.GP22, board.GP27)
keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(split_side=SplitSide.LEFT)
keyboard.modules.append(split)
keyboard.modules.append(Layers())

keyboard.keymap = [
    [
        KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC,
    ]
]
if __name__ == '__main__':
    keyboard.go()