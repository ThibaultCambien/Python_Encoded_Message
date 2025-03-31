import string

def clean_word(word):
    return word.strip().lower()

def extract_keys(encoded_text, filler_words):
    """Extrait les clés uniques en supprimant les mots de remplissage."""
    return sorted(set(clean_word(word) for word in encoded_text.split()) - filler_words)

def assign_keys_to_letters(keys):
    """Assign each key to a letter or number."""
    alphabet = list(string.ascii_uppercase) + [str(i) for i in range(10)]
    key_mapping = {}
    for i, key in enumerate(keys):
        if i < len(alphabet):
            key_mapping[key] = alphabet[i]
    return key_mapping

def decode_message(encoded_message, key_mapping):
    """Décode un message encodé en utilisant le mapping des clés."""
    decoded_chars = []
    missing_words = []
    for word in encoded_message.split():
        cleaned = clean_word(word)
        if cleaned in key_mapping:
            decoded_chars.append(key_mapping[cleaned])
        else:
            missing_words.append(cleaned)
    if missing_words:
        print("Clé non trouvé dans mapping:", missing_words)
    return "".join(decoded_chars)

def load_encoded_message(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

filler_words = {'rhubarb', 'quince', 'watermelon', 'ximenia', 'nut', 'zucchini', 'blackberry', 'vine', 'cranberry',
                'durian', 'papaya', 'huckleberry', 'jujube', 'xerophyte', 'elderberry', 'tangerine', 'satsuma',
                'kiwi', 'victoria', 'lime', 'saffron', 'ugni', 'rasp', 'kale', 'avocado', 'xigua', 'ugly',
                'waxberry', 'eggplant', 'honeydew', 'lychee', 'dragonfruit', 'zinfandel', 'raspberry', 'guava',
                'indian', 'fig', 'orange', 'yuzu', 'date', 'tamarind', 'yam', 'strawberry', 'hawthorn', 'apple',
                'nectarine', 'cherry', 'fennel', 'elderflower', 'quandary', 'blueberry', 'quandong', 'zest',
                'wildberry', 'yellow', 'apricot', 'onion', 'cantaloupe', 'nutmeg', 'persimmon', 'mandarin', 'olive',
                'lemon', 'tamarillo', 'ugli', 'mango', 'grape', 'banana', 'jackfruit', 'gooseberry', 'vanilla',
                'mulberry', 'kumquat', 'peach', 'feijoa'}

old_message = """Strawberry quince olive fig bliss peach ximenia victoria grape kiwi cherry
feijoa cloud fig nectarine guava blackberry papaya kumquat eggplant watermelon
blackberry strawberry rhubarb lime feijoa eggplant ice apricot nutmeg tamarillo
ugni victoria victoria huckleberry yellow zest elderflower zucchini nebula
apricot ugly jackfruit ugli raspberry zinfandel feijoa vanilla ivory ugli
quandary ximenia blackberry tamarind quince kale avocado oasis eggplant jujube
elderberry mulberry raspberry elderberry feijoa nut abbey kiwi jackfruit ugli
yuzu blackberry mulberry orange waxberry quince vine marvel jackfruit
strawberry kale guava mandarin ugli mulberry nutmeg serene zest dragonfruit
jujube victoria zest kumquat hawthorn waxberry ocean xerophyte lime fig
cantaloupe nutmeg feijoa apple tamarillo lychee hawthorn vine tamarillo palm
kumquat elderflower kale ugni nut kiwi wildberry fennel garden gooseberry
mandarin hawthorn kiwi date xerophyte elderflower raspberry elderberry pearl
onion kale ugni strawberry zucchini banana hawthorn mulberry feast tangerine
jackfruit vanilla indian ugni olive satsuma ugly papaya guava eagle nectarine
wildberry wildberry lemon dragonfruit saffron haven blackberry strawberry grape
jujube tamarind watermelon quandong hawthorn persimmon lemon harmony kale
elderflower vine date persimmon quandong dragonfruit quartz mulberry quince
zinfandel kale cranberry lychee jade tamarillo papaya gooseberry ugly eggplant
elderberry jackfruit cranberry elderberry cactus honeydew vine kale tangerine
persimmon rasp zest dragonfruit jujube blackberry ximenia daisy cantaloupe
papaya hawthorn nut nectarine apricot durian hawthorn mango meadow orange
indian zinfandel lychee tamarillo ugni zest fennel satsuma ugli jackfruit
elderberry jazz durian jujube grape mulberry xerophyte yam kumquat apple
cranberry quest watermelon dragonfruit apricot jujube papaya orange mandarin
rhubarb watermelon banana falcon apple yuzu kumquat elderberry nectarine apple
yuzu satsuma dragonfruit elderflower xerophyte cantaloupe hawthorn luna jujube
elderflower jackfruit zest yam dragonfruit banana rasp date rain kale tamarillo
tamarillo lime ximenia raspberry strawberry fennel ximenia lime lagoon satsuma
grape strawberry zest ugly nut indian cherry kale zinfandel huckleberry
tamarillo zinfandel dawn quandong blueberry blueberry raspberry banana papaya
satsuma ximenia watermelon glow dragonfruit zucchini durian guava olive yam
papaya nest eggplant strawberry cranberry indian strawberry rasp watermelon
koala nut cantaloupe feijoa xerophyte quince apricot river tamarillo orange
ugly zest jujube lychee kiwi mandarin mandarin breeze avocado wildberry
zucchini jackfruit gooseberry durian waxberry wildberry echo nut cherry
quandong lychee blackberry huckleberry amber mandarin xigua quandong banana
mango"""


# On extrait les clés du message
keys = extract_keys(old_message, filler_words)
print("Clés trouvées :", keys)

# On assigne les clés aux lettres
key_mapping = assign_keys_to_letters(keys)
print("Mapping :", key_mapping)

file_path = "message_encoded.txt"
encoded_text = load_encoded_message(file_path)

# On décode le message
decoded_text = decode_message(encoded_text, key_mapping)
print("Message décodé :", decoded_text)
