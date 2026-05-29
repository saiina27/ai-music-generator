from textblob import TextBlob

def detect_mood(lyrics):

    lyrics = lyrics.lower()

    sad_words = [
        "miss","alone","cry",
        "broken","hurt",
        "sad","lonely"
    ]

    happy_words = [
        "love","happy",
        "dance","smile",
        "party","joy"
    ]

    sad_score = 0
    happy_score = 0

    for word in sad_words:

        if word in lyrics:
            sad_score += 1

    for word in happy_words:

        if word in lyrics:
            happy_score += 1

    if sad_score > happy_score:
        return "Sad"

    elif happy_score > sad_score:
        return "Happy"

    else:

        analysis = TextBlob(lyrics)

        if analysis.sentiment.polarity > 0:
            return "Happy"

        elif analysis.sentiment.polarity < 0:
            return "Sad"

        return "Neutral"


def generate_notes(mood):

    if mood=="Sad":
        return [55,58,60]

    elif mood=="Happy":
        return [60,64,67]

    elif mood=="Energetic":
        return [72,74,76]

    elif mood=="Chill":
        return [50,53,57]

    return [60,62,64]