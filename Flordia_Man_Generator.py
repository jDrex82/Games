import random

# List of random Florida Man crimes
florida_man_crimes = [
    "ate someone's face off",
    "tried to rob a bank with a live alligator",
    "traveled to space using a lawn chair and balloons",
    "used a swordfish to stab someone",
    "tried to wrestle an alligator at a family picnic",
    "stole a neighbor's lawnmower to go joyriding",
    "built a flamethrower to clear out a beehive",
    "attempted to swim with manatees while wearing a shark costume",
    "tried to start a dance party on a busy highway",
    "attempted to use a jet ski in a flooded shopping mall",
    "tried to surf on the hood of a moving car",
    "organized a flash mob in a fast-food drive-thru",
    "tried to sell the Eiffel Tower to unsuspecting tourists",
    "attempted to train squirrels for a circus act",
    "tried to use a chainsaw to carve a giant sandcastle",
    "attempted to break a world record for eating the most hot dogs in one minute",
    "tried to fish for sharks using a fishing rod made of spaghetti",
    "tried to launch a homemade rocket from the backyard",
    "attempted to parachute off a bridge using a bedsheet",
    "tried to create a human-sized hamster wheel for transportation",
    "attempted to start a petting zoo with wild raccoons",
    "tried to ride an ostrich through the neighborhood",
    "attempted to set a world record for the longest time spent juggling flamingos",
    "tried to create a backyard roller coaster with shopping carts",
    "attempted to use a lawnmower to give the entire neighborhood free haircuts",
    "tried to catch a swarm of bees with a butterfly net",
    "attempted to build a backyard zipline from the roof to the swimming pool",
    "tried to play hopscotch on a busy intersection",
    "attempted to reenact scenes from a superhero movie using a homemade costume",
    # ... (add more crimes as needed)
]

def generate_florida_man_meme():
    # Get user input
    full_name = input("Enter the full name of the person: ")
    city = input("Enter the city where the crime happened: ")

    # Split full name into first name and last name
    first_name, last_name = full_name.split(maxsplit=1)

    # Generate a random Florida Man crime headline
    random_crime_headline = random.choice(florida_man_crimes)

    # Display the news headline
    print("\nNews Headline:")
    print(f"Breaking news! Florida man {random_crime_headline}")

    # Display the news headline
    print()
    print(f"In a bizarre incident, {first_name} {last_name.capitalize()} is now at the center of a police investigation in {city.capitalize()}. Witnesses report that {last_name} {random_crime_headline}. Authorities are still investigating the motive behind why the suspect {random_crime_headline}, and {last_name.capitalize()} is expected to appear in court later this week to answer to the charges.")

def main():
    print("Welcome to the Florida Man News Generator!")

    while True:
        generate_florida_man_meme()

        # Ask if the user wants to generate another meme
        user_input = input("\nDo you want to generate another news graph? (yes/no): ").lower()
        if user_input != "yes":
            print("Exiting the Florida Man News Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
