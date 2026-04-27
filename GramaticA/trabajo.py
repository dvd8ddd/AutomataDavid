import nltk
from nltk import CFG

elven_grammar = CFG.fromstring("""
    S -> NSC VS NSC | NSC VS
    NSC -> NSCP NSC_A
    NSC_A -> Conj NSCP NSC_A | Empty
    NSCP -> NS
    NS -> Vo | E | C

    Vo -> VoR VoE
    E -> ER EE
    C -> CR CE

    VoR -> 'nara' | 'luma' | 'sela' | 'tula' | 'vasa' | 'naya' | 'rima' | 'sora' | 'tila' | 'yara'
    ER -> 'dor' | 'sil' | 'tal' | 'mir' | 'nor' | 'lin' | 'gal' | 'tir' | 'bel' | 'car'
    CR -> 'balrog' | 'thandor' | 'morgul' | 'gondor' | 'istar' | 'durin' | 'angmar' | 'valnor' | 'belgar' | 'arnor'

    VoE -> 'r' | PP | Empty
    EE -> 'i' | 'e' PP | 'e' | 'ë'
    CE -> 'i' | PP | Empty

    PP -> 'li'
    VS -> 'martir' | 'harya' | 'hosta' | 'savin' | 'síla' | 'lanta' | 'tira' | 'norta' | 'cala' | 'mira'
    Conj -> 'ar' | 'hya'
    Empty ->
""")

parser = nltk.ChartParser(elven_grammar)

def separate(sentence):
    sentence = sentence.lower()

    endings = {
        'narar': 'nara r',
        'lumar': 'luma r',
        'selar': 'sela r',
        'tular': 'tula r',
        'vasali': 'vasa li',
        'nayali': 'naya li',
        'rimali': 'rima li',
        'sorar': 'sora r',
        'tilali': 'tila li',
        'yarali': 'yara li',

        'dori': 'dor i',
        'dore': 'dor e',
        'doreli': 'dor e li',
        'sili': 'sil i',
        'sile': 'sil e',
        'sileli': 'sil e li',
        'tali': 'tal i',
        'tale': 'tal e',
        'taleli': 'tal e li',
        'miri': 'mir i',
        'mire': 'mir e',
        'mireli': 'mir e li',
        'nori': 'nor i',
        'nore': 'nor e',
        'noreli': 'nor e li',
        'lini': 'lin i',
        'line': 'lin e',
        'lineli': 'lin e li',
        'gali': 'gal i',
        'gale': 'gal e',
        'galeli': 'gal e li',
        'tiri': 'tir i',
        'tire': 'tir e',
        'tireli': 'tir e li',
        'beli': 'bel i',
        'bele': 'bel e',
        'beleli': 'bel e li',
        'cari': 'car i',
        'care': 'car e',
        'careli': 'car e li',

        'balrogi': 'balrog i',
        'balrogli': 'balrog li',
        'thandori': 'thandor i',
        'thandorli': 'thandor li',
        'morguli': 'morgul i',
        'morgulli': 'morgul li',
        'gondori': 'gondor i',
        'gondorli': 'gondor li',
        'istari': 'istar i',
        'istarli': 'istar li',
        'durini': 'durin i',
        'durinli': 'durin li',
        'angmari': 'angmar i',
        'angmarli': 'angmar li',
        'belgari': 'belgar i',
        'belgarli': 'belgar li',
        'valnori': 'valnor i',
        'valnorli': 'valnor li',
        'arnori': 'arnor i',
        'arnorli': 'arnor li'
    }

    for original_word, new_word in endings.items():
        sentence = sentence.replace(original_word, new_word)

    return sentence.split()

def analyze(sentence):
    try:
        tokens = separate(sentence)
        trees = list(parser.parse(tokens))

        if trees:
            print("\nLa oración:", sentence)
            print("Sí es válida. Árbol:")
            trees[0].pretty_print()
        else:
            print("\nLa oración:", sentence)
            print("No es válida con esta gramática.")

    except ValueError:
        print("\nLa oración:", sentence)
        print("No es válida con esta gramática.")

sentences = [
    "narar martir lumar",
    "selar harya tular",
    "vasali hosta rimali",
    "sorar síla",
    "tilali savin yarali",

    "dori martir sili",
    "dore harya tale",
    "doreli hosta miri",
    "lini síla",
    "galeli savin tiri",

    "beli martir cari",
    "bele harya care",
    "beleli hosta careli",
    "tiri síla",
    "mire savin lini",

    "balrogi martir gondori",
    "thandori harya istari",
    "morguli hosta valnori",
    "gondorli síla",
    "istari savin durini",

    "angmari martir belgari",
    "belgarli harya arnorli",
    "valnori hosta balrogli",
    "arnori síla",
    "durinli savin morgulli",

    "narar martir lumar ar selar",
    "vasali hosta rimali ar tilali",
    "dori martir sili hya lini",
    "balrogi harya gondori ar istari",
    "angmari hosta valnori hya arnori"
]
incorrect_sentences = [
    "narar corre lumar",
    "martir narar lumar",
    "sorar lumar síla",
    "dori ar martir sili",
    "balrogi harya ar istari",
    "gondori savin istari ar",
    "valnori hya hosta arnori",
]

print("1. Run automatic tests")
print("2. Write your own sentence")
print("3. Run incorrect sentences")
print("------------")

while True:
    try:
        option = int(input("Choose your option: "))
        if option == 1 or option == 2 or option == 3:
            break
        print("Please type 1, 2 or 3.")
    except ValueError:
        print("Please write a number.")

if option == 1:
    for sentence in sentences:
        analyze(sentence)

elif option == 2:
    sentence = input("Write your sentence: ")
    analyze(sentence)

elif option == 3:
    for sentence in incorrect_sentences:
        analyze(sentence)