import time
import random

# the starting of the typing text.
def typing_hub():
    texts = [
        "The blue coffee mug sat perilously close to the edge of the glass table. A soft breeze tugged at the corner of a nearby newspaper, threatening to reveal a secret hidden in the headlines.",
        "Golden sunlight filtered through the oak leaves, casting dancing shadows on the mossy ground. A single blue jay screamed at the sky, indifferent to the quiet rustle of the approaching autumn.",
        "Bicycle gravity. Neon lemon slices on a velvet tectonic plate. Yesterday’s echoes are tomorrow’s ringtones. Five silver buttons lost in a field of static.",
        "A clockwork orange peeling itself under a digital moon while gravity leaks through the floorboards. The carpet is slowly turning into liquid static.",
        "Ivy growing over a neon sunset in the geometry of a whispered secret. Forty-two wooden whistles are singing to an audience of glass marbles.",
        "Raindrops that taste like forgotten anniversaries and cold electricity. A titanium hummingbird hovers over a sea of salt, searching for a frequency.",
        "Oxygen is just a metaphor for breathing in a room of tectonic plates. Binary moss creeps across the cooling server racks in the dark.",
        "The smell of old library books and ozone-scented static. A ghost in the machine is eating crackers made of information and broken television signals.",
        "Blue ink bleeding into a white-out horizon where punctuation marks dance. One hundred silver buttons are vibrating with the rhythm of a sub-atomic heartbeat.",
        "Yesterday’s echoes are today’s ringtones in a mountain of typewriter keys. A golden compass points toward a thunderstorm trapped inside a glass bottle.",
        "The sudden realization that the walls are made of crystallized honey. Bicycles made of frozen smoke lean against a brick wall that only exists in dreams.",
        "A kaleidoscope of jagged thoughts spinning inside a hollow lightbulb. Every tick of the clock is a tiny hammer hitting a nail into the fabric of space.",
        "Green light flickering through a forest of fiber-optic ferns. The architecture of a cloud is sturdy when viewed through a lens made of salt and polaroids."
    ]

    target_text = random.choice(texts)

    print("Wellcome to the 'typing_hub'!!!")
    print(f"Start typing : {target_text}")
    input("press the 'Enter' to start typing.")

    # starting the clock
    start_time = time.time()
    user_input = input("\n Go! -> : ")
    end_time = time.time()

    # calculating
    total_time = round(end_time - start_time, 2)

    if user_input == target_text:
        ## Standard WPM formula: (characters / 5) / minutes
        wpm = (len(target_text) / 5) / (total_time / 60)
        print(f"\n Success!")
        print(f"Time: {total_time} seconds")
        print(f"Speed: {round(wpm, 2)} WPM")

if __name__ == "__main__":
    while True:
        typing_hub()
