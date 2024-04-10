import random
import pandas as pd
from utils import InchtoFt


class PhysicalAttributes:
    def __init__(self, race, height, weight, eye_color, hair_color, hair_style, skin_tone):
        self.race = race
        self.height = height
        self.weight = weight
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_style = hair_style
        self.skin_tone = skin_tone

    def display_physAttributes(self):
        print("Physical Attributes:")
        print(f"Height: {InchtoFt.convert(self.height)}")
        print(f"Weight: {self.weight} lbs")
        print(f"Eye Color: {self.eye_color}")
        print(f"Race: {self.race}")
        print(f"Hair Color: {self.hair_color}")
        print(f"Hair Style: {self.hair_style}")
        print(f"Skin Tone: {self.skin_tone}")


def read_csv(filename):
    return pd.read_csv(filename)


def randGenAttributes(gender, race):
    skin_tone = rand_skinTone(race)
    eye_color = rand_eyeColor()
    hair_color = rand_hairColor(race)
    hair_style = rand_hairStyle(gender)
    return eye_color, hair_color, hair_style, skin_tone


def rand_hairColor(race):
    hair_color_df = pd.read_csv("data/hair_color.csv")
    grouped_hair_color = hair_color_df.groupby('race').agg(list).reset_index()

    race_data = grouped_hair_color[grouped_hair_color['race'] == race]

    if race_data.empty:
        raise ValueError(f"No hair color data found for race: {race}")

    hair_colors = race_data['hair_color'].iloc[0]
    likelihoods = race_data['likelihood'].iloc[0]

    if not hair_colors or not likelihoods:
        raise ValueError("Hair color data is empty")

    # Select a random hair color based on the likelihoods
    selected_hair_color = random.choices(hair_colors, weights=likelihoods)[0]

    return selected_hair_color


def rand_hairStyle(gender):
    hair_style_df = pd.read_csv("data/hair_styles.csv")
    filtered_hair_style = hair_style_df[(hair_style_df['gender'] == 'Any') | (hair_style_df['gender'] == gender)]

    if filtered_hair_style.empty:
        raise ValueError(f"No hair style data found for gender: {gender}")

    hair_styles = filtered_hair_style['hair_style']
    likelihoods = filtered_hair_style['likelines']

    if hair_styles.empty or likelihoods.empty:
        raise ValueError("Hair style data is empty")

    # Select a random hair style based on the likelihoods
    selected_hair_style = random.choices(hair_styles, weights=likelihoods)[0]

    return selected_hair_style


def rand_skinTone(race):
    skin_tone_df = pd.read_csv("data/skin_tone.csv")
    grouped_skin_tone = skin_tone_df.groupby('race').agg(list).reset_index()

    race_data = grouped_skin_tone[grouped_skin_tone['race'] == race]

    if race_data.empty:
        raise ValueError(f"No skin tone data found for race: {race}")

    skin_tones = race_data['skin_tone'].iloc[0]
    likelihoods = race_data['likelihood'].iloc[0]

    if not skin_tones or not likelihoods:
        raise ValueError("Skin tone data is empty")

    # Select a random hair color based on the likelihoods
    selected_skin_tone = random.choices(skin_tones, weights=likelihoods)[0]
    return selected_skin_tone


def rand_eyeColor():
    eye_color_df = read_csv("data/eyeColor.csv")
    eye_colors = eye_color_df['eye_color']
    frequencies = eye_color_df['frequency']

    # Select a random eye color based on the frequencies
    selected_eye_color = random.choices(eye_colors, weights=frequencies)[0]
    return selected_eye_color


def setHeightWeight(gender):
    filename = "heightweightValues.txt"
    if gender == "Female":
        rand_height = random.randint(58, 70)  # If female restricts height range to 4'10"-5'10"
    else:
        rand_height = random.randint(58, 76)
    with open(f"data/" + filename, "r") as file:
        for line in file:
            if int(line.split()[0]) == rand_height:
                height, min_weight, max_weight = map(int, line.split())
                if gender == "Female":
                    weight = random.randint(min_weight, max_weight + 5)
                else:
                    weight = random.randint(min_weight, max_weight)
                break
    return height, weight
