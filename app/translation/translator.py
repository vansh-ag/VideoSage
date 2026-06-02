from deep_translator import GoogleTranslator



def translate_text(
        text: str,
        source_language: str = "auto",
        target_language: str = "en"
):
    """
    Translate any text into English.
    """

    translated = GoogleTranslator(
        source=source_language,
        target=target_language
    ).translate(
        text
    )

    return translated



def translate_segments(
        segments: list
):
    """
    Preserve timestamps while translating.
    """

    translated_segments = []

    for segment in segments:

        translated_text = translate_text(
            segment["text"]
        )

        translated_segments.append(
            {
                "start": segment["start"],
                "end": segment["end"],
                "text": translated_text
            }
        )

    return translated_segments



def translate_transcript(
        transcript_data: dict
):
    """
    Input:
    {
        full_text,
        segments
    }

    Output:
    {
        full_text,
        segments
    }
    """

    translated_segments = translate_segments(
        transcript_data["segments"]
    )

    full_text = " ".join(
        [
            segment["text"]
            for segment in translated_segments
        ]
    )

    return {
        "full_text": full_text,
        "segments": translated_segments
    }