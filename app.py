from Transcript import Transcript

def whis(video):
    return Transcript.get_transcript(video)

whis("clase1.mp3")