import pandas as pd
import Slengine as sl
import random
import scipy.stats
import brand_profiles

data = pd.read_csv('prompt_words')  # DataFrame of words corresponding to each of the 14 brand profile attributes

slider_titles = [
    "Bold", "Confident", "Defiant", "Fun-loving",
    "Intense", "Joyful", 'Majestic', "Peaceful",
    "Pure", "Simple", "Sophisticated", "Spontaneous",
    "Technical", "Warm"
]  # 14 brand profile attributes

def highest_in_dictionary(word_dict, list_switch=True):  # finds highest-scoring brand attribute
    current_highest = [-1,""]
    for key in word_dict:
        if list_switch:
            this_len = len(word_dict[key])
        else:
            this_len = word_dict[key]
        if this_len > current_highest[0]:
            current_highest = [this_len, key]
    return current_highest[1]

def genre_adder(highest_two):  # builds the genre, instrumentation and tempo elements of the final prompt
    vowels = ['A', 'E', 'I', 'O', 'U']
    starter = 'A '
    genres = [
    'Funk Soul', 
    'Jazz', 
    'Pop', 
    'Latin', 
    'Rhythm and Blues',
    'Rock',
    'Electronic Dance Music',
    'Blues',
    'Hip Hop',
    'Reggae', 
    'Ambient', 
    'Classical', 
    'Metal', 
    'Folk Country', 
    'Singer-Songwriter']

    genre_weights = [469, 1006, 346, 230, 5, 2314, 3297, 180, 426, 42, 750, 973, 314, 7, 53]  # weights for genres based on genre popularity
    
    chosen_genre = random.choices(genres, weights=genre_weights, k=1)[0]  # chooses a genre based on weights
    if chosen_genre[0] in vowels:
        starter = 'An '  # grammatically corrects for genre names that begin with vowels

    instrumentation_BPM = {  # dictionary of instrumentation and tempo information for each genre
        'Funk Soul': (
            'electric bass, drums, brass section (trumpet, saxophone, trombone), electric guitar, and keyboard',
            random.randint(90, 120)  # chooses a random BPM from the expected range for the genre
        ),
        'Rock': (
            'electric guitar, bass guitar, and drums',
            random.randint(100, 160)
        ),
        'Blues': (
            'acoustic guitar, harmonica, drums, and bass',
            random.randint(70, 100)
        ),
        'Jazz': (
            'saxophone, trumpet, piano, double bass, and drums',
            random.randint(60, 240)
        ),
        'Reggae': (
            'electric guitar, bass, drums, keyboards, and skank guitar',
            random.randint(70, 90)
        ),
        'Metal': (
            'electric guitar with heavy distortion, bass guitar, and double bass drums',
            random.randint(100, 200)
        ),
        'Pop': (
            'synthesizers, electronic beats, guitars, and bass',
            random.randint(100, 130)
        ),
        'Singer-Songwriter': (
            'acoustic guitar or piano, and other acoustic instruments',
            random.randint(60, 120)
        ),
        'Folk Country': (
            'acoustic guitar, banjo, fiddle, mandolin, bass, and drums',
            random.randint(80, 120)
        ),
        'Classical': (
            'orchestral instruments including strings, woodwinds, brass, and percussion',
            random.randint(60, 180)
        ),
        'Electronic Dance Music': (
            'synthesizers, drum machines, electronic beats, and various sampled and manipulated sounds',
            random.randint(120, 150)
        ),
        'Rhythm and Blues': (
            'electric guitar, bass, drums, keyboards, and horns',
            random.randint (70, 100)
        ),
        'Hip Hop': (
            'sampled beats and electronic sounds',
            random.randint(80, 100)
        ),
        'Ambient': (
            'atmospheric textures, minimal percussion, and smooth synthesizers',
            'no fixed tempo'
        ),
        'Latin': (
            'congas, bongos, maracas, trumpets, guitars, and bass',
            random.randint(90, 140)
        )
    }

    return starter + chosen_genre + ' song with ' + instrumentation_BPM[chosen_genre][0] + '. \nTempo: ' + str(instrumentation_BPM[chosen_genre][1]) + ' BPM. \nEmotions: '


def sentence_builder(word_dict):  # builds the 'emotions' section of the final prompt, adding quanitifiers in front of the prompt words based on the inputted slider values. Prints the final prompt
    prefixes = [  # quantifiers to be added in front of the prompt words
    "Totally",
    "Extremely",
    "Very",
    "Moderately",
    "Fairly",
    "Quite",
    "Slightly",
    "A hint of",
    "Barely",
    "Hardly",
    "Almost"
]

    final_prompt = ""
    highest_two = []
    counter = 0
    used_words = []
    while len(prefixes) > 0 and len(word_dict) > 0:
        key = highest_in_dictionary(word_dict)
        if counter < 1:
            highest_two.append(key)
        value_counter = 0
        for value in word_dict[key]:
            if value in used_words:
                continue
            if value_counter + counter - 1 > len(word_dict[key]):
                break
            used_words.append(value)
            final_prompt += prefixes[0] + " " + value + ", "
            value_counter += 1
        prefixes.pop(0)
        word_dict.pop(key)
        counter += 0.5
    final_prompt = genre_adder(highest_two) + final_prompt[0:-2] + "."
    print(final_prompt)
    input()

def word_dict_constructor(slider_titles, processed):  # creates a list of words tied to each core attribute and weighted to the slider values
    counter = 0
    words = {}
    for title in slider_titles:
        sub_attributes = data[title].values.tolist()
        random.shuffle(sub_attributes)
        subcount = 0
        for val in range(processed[counter]):
            if title in words:
                words[title].append(sub_attributes[subcount])
            else:
                words[title] = [sub_attributes[subcount]]
            subcount += 1
        counter += 1
    sentence_builder(words)

def value_processor(values):  # normalizes slider values to correct positive skew
    min_val = min(values)
    max_val = max(values)
    processed = []
    for val in values:
        normalized_value = int(round(10 * (val - min_val) / (max_val-min_val))) 
        processed.append(normalized_value)
    word_dict_constructor(slider_titles, processed)

def update_values(v):
    value_processor(v)

def main(profile=False):  # builds sliders
    if profile:
        update_values(brand_profiles.profiles[profile])
        return
    sliders = []
    for t in slider_titles:
        sliders.append(sl.Slider(t,(0,100,1)))
    sl.create_window(sliders,update_values,(500,820))

if __name__ == "__main__":
    main()  # 'activia', 'apple', 'haribo' can be inputted into main() as example brand profiles





