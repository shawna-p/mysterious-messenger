label example_solo_story_call():
    ja "Hello, [name]. I hope I haven't found you at a bad time."
    menu:
        extend ''
        "No, not at all!":
            ja "Ah, that's good to hear."
        ""
    return

label example_solo_story_call_expired():
    return