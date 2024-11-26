emoji_dict = {
    ":thumbs_up:": "👍",
    ":thumbsup:": "👍",
    ":1st_place_medal:": "🥇",
    ":earth_asia:": "🌏",
    ":candy:": "🍬",
    ":ice_cream:": "🍨",

}

def emojize(text):
    """Convert text codes to their corresponding emojis."""
    for code, emoji in emoji_dict.items():
        text = text.replace(code, emoji)
    return text

def main():
    user_input = input("Enter a string with emoji codes: ")
    emojized_text = emojize(user_input)
    print(emojized_text)

if __name__ == "__main__":
    main()