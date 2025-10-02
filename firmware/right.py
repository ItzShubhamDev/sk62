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

encoder_handler = EncoderHandler()

keyboard.modules.append(split)
keyboard.modules.append(Layers())
keyboard.modules.append(encoder_handler)

encoder_handler.pins = ((board.GP20, board.GP21, board.GP19),)
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),)
]

keyboard.keymap = [
    [
        KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC,
        KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC,
        KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.NO, KC.ENT,
        KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.NO, KC.RSFT,
        KC.RALT, KC.RGUI, KC.APP, KC.RCTL,
    ]
]
if __name__ == '__main__':
    keyboard.go()