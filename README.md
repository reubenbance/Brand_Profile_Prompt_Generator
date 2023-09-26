# Brand profile text prompt generator for MusicGen track generation

Made for use with Facebook's MusicGen (https://github.com/facebookresearch/audiocraft) generative AI.

EXE Build: https://drive.google.com/drive/folders/1W28CXWJ1WehQm2dyIa9BAYsMWScHvuo6?usp=sharing \

## **Setup**

The program requires the following Python libraries to be installed:\
_pandas_\
_scipy.stats_

## **Files in the source code**
  
promptgenerator.py: the main python file for the prompt generator; open it to run the program\
Slengine.py: contains code that builds the sliders for the brand profile input\
brand_profiles.py: several example brand profiles that can be used for testing\
prompt_words.csv: contains all of the emotion words used to build the text prompt\

## **Using the generator**

1. Run the 'promptgenerator.py' python file
2. A window will appear with 14 sliders corresponding to 14 core brand attributes: use these sliders to input the desired brand profile
3. Press 'submit' in the slider window
4. A text prompt will be generated that can then be inputted into the MusicGen generative AI to produce original music consistent with the inputted brand profile
