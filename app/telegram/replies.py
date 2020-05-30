from app import settings

HELP_REPLY = (
    "Send me a picture with an object and I will try to recognize it!\n"
    "P.S. for the better accuracy please choose an image with a white background with only one clothes on it.\n\n"
    "The objects I can recognize:\n" + "\n".join([class_name for class_name in settings.CLASS_NAMES])
)

START_REPLY = "Hello {}! I'm a bot that can recognize clothes on the image!\n\n" + HELP_REPLY

CERTAIN_DECISION_REPLIES = [
    "I'm quite sure it's a {}",
    "I think this is a {}",
    "Looks like a {}",
    "It seems that it's a {}",
]

NO_DECISION_REPLIES = [
    "I'm so confused! I can't imagine what can it be!",
    "Unfortunately, I didn't recognize clothes on this image =(",
    "Sorry, but I have no clue what it might be...",
]

UNCERTAIN_DECISION_REPLIES = [
    "I'm not sure, but probably this is a {}",
    "Probably it's a {}",
    "Let me guess...is this a {}?",
    "My intuition tells me this is {}",
]
