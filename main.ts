radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber <= dice) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Happy)
        score += 1
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(dice)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(score)
})
input.onGesture(Gesture.Shake, function () {
    dice = randint(1, 6)
    basic.showNumber(dice)
})
let dice = 0
let score = 0
radio.setGroup(24)
radio.setTransmitPower(7)
score = 0
