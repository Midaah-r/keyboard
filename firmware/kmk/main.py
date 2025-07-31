#temporary firmware made using chatgpt, ill make the proper one when the MCU arrives. 

import kmk
from kmk.keys import KC
from kmk.modules.rotary_encoder import RotaryEncoder

keyboard = kmk.Keyboard()

encoder_pin_a = 4
encoder_pin_b = 5
encoder_button_pin = 6

rotary_encoder = RotaryEncoder(
    encoder_pin_a=encoder_pin_a,
    encoder_pin_b=encoder_pin_b,
    encoder_button_pin=encoder_button_pin,
)

keyboard.modules.append(rotary_encoder)

keymap = [
    [
        KC.ESC, KC.1, KC.2, KC.3, KC.4, KC.5, KC.6, KC.7, KC.8, KC.9, KC.0, KC.MINS, KC.EQL,
        KC.BSPC
    ],
    [
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, 
        KC.BSLS, KC.DEL
    ],
    [
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, 
        KC.ENT, KC.PGUP
    ],
    [
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, 
        KC.UP, KC.PGDN
    ],
    [
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT
    ]
]

keyboard.keymap = keymap

@keyboard.modules.append
def rotary_actions():
    def encoder_turn(direction):
        if direction == 'CW':
            keyboard.press(KC.VOLU)
            keyboard.release(KC.VOLU)
        elif direction == 'CCW':
            keyboard.press(KC.VOLD)
            keyboard.release(KC.VOLD)

    def encoder_click():
        keyboard.press(KC.MUTE)
        keyboard.release(KC.MUTE)

    rotary_encoder.on_encoder_turn = encoder_turn
    rotary_encoder.on_encoder_click = encoder_click

if __name__ == "main":
    keyboard.go()
