import json

# Function to get title and subtitle using the number
def get_title_and_subtitle(number):
    if number in data_dict:
        return data_dict[number]['title'], data_dict[number]['subtitle']
    else:
        return None, None

# Load Database JSON data
with open('allData.json', 'r') as file:
    data = json.load(file)

# Load the Matches Data
with open('matches.txt', 'r') as file:
    lines = file.readlines()

# Create a dictionary for easy access to database data
data_dict = {item['number']: item for item in data}

# Extract the values from each line in matches.txt and store them in a list
numbers = []
for line in lines:
    # Use eval to convert string representation of dictionary to actual dictionary
    match = eval(line.strip())  
    for value in match.values():
        # We only need the card id, so we disregard the filename
        numbers.append(value)

# Create a list to store my library dokkan entries
myLibrary = []

# Loop through list of matched card ids
for number in numbers:
    
    # Search the database by number to get the title and subtitle
    title, subtitle = get_title_and_subtitle(number)
    
    # Create a json entry to store card data
    entry = {
        'number' : number,
        'title' : title,
        'subtitle' : subtitle 
    }    
    
    # Add card to list of cards
    myLibrary.append(entry)

# Open a new json file to save dokkan library data 
with open('myLibrary.json', 'w+') as f2:
   data = json.dumps(myLibrary, indent=3)
   f2.write(data)


