init python:

    ## Note: for cleaner pronoun code that can be adapted to new projects,
    ## check out my In-Depth Pronouns code:
    ## https://feniksdev.itch.io/in-depth-pronouns-for-renpy

    class Pronoun():
        """
        A helper class for picking the correct pronoun to use. Simplified from
        In-Depth Pronouns for Ren'Py.
        """
        def __init__(self, neutral, feminine=None, masculine=None):
            """
            Declare words for each pronoun set.
            """
            self.neutral = neutral
            self.feminine = feminine or neutral
            self.masculine = masculine or neutral

        def __str__(self):
            """
            A string representation of this pronoun or word. Ren'Py fetches this
            when you interpolate this object in dialogue like "[them]", so it's
            possible to do logic here to get the right word.
            """

            if persistent.pronoun == "she/her":
                return self.feminine
            elif persistent.pronoun == "he/him":
                return self.masculine
            else:
                return self.neutral


    class PronounVerb():
        """
        A special class to easily conjugate verbs for pronouns. Simplified
        from In-Depth Pronouns for Ren'Py on itch.io.

        Attributes:
        -----------
        plural : string
            The plural verb conjugation.
        singular : string
            The singular verb conjugation.
        """
        def __init__(self, plural, singular):
            """Create a PronounVerb object."""
            self.plural = plural
            self.singular = singular

        def __str__(self):
            """
            A string representation of this verb based on the player's
            current pronouns.
            """
            ## Use the plural or singular based on whether this pronoun
            ## set is plural or singular.
            if persistent.pronoun == "they/them":
                return self.plural
            else:
                return self.singular

    def get_term(fem, masc, neutral):
        """
        A function which will return a term based on the player's pronouns
        and gender. Generally prefers returning the neutral term.
        """
        if persistent.gender == "female" and persistent.pronoun == "she/her":
            return renpy.substitute(fem)
        elif persistent.gender == "male" and persistent.pronoun == "he/him":
            return renpy.substitute(masc)
        else:
            return renpy.substitute(neutral)

    class GenderedTerm(object):
        """
        A class which returns a term corresponding to the gender and pronouns
        of the player when interpolated in dialogue.
        """
        def __init__(self, fem, masc, neutral):
            self.fem = fem
            self.masc = masc
            self.neutral = neutral
        def __str__(self):
            return get_term(self.fem, self.masc, self.neutral)


########################################
## PRONOUN VARIABLES
########################################
# Extra variables since the player can choose their pronouns.
# Feel free to add more so script writing is easier.

define they = Pronoun("they", "she", "he")
define them = Pronoun("them", "her", "him")
define their = Pronoun("their", "her", "his")
define theirs = Pronoun("theirs", "hers", "his")
define themself = Pronoun("themself", "herself", "himself")
define they_re = Pronoun("they're", "she's", "he's")
define they_ve = Pronoun("they've", "she's", "he's")

define They = Pronoun("They", "She", "He")
define Them = Pronoun("Them", "Her", "Him")
define Their = Pronoun("Their", "Her", "His")
define Theirs = Pronoun("Theirs", "Hers", "His")
define Themself = Pronoun("Themself", "Herself", "Himself")
define They_re = Pronoun("They're", "She's", "He's")
define are = PronounVerb("are", "is")
define have = PronounVerb("have", "has")
define do = PronounVerb("do", "does")

define s_verb = PronounVerb("", "s")
define es_verb = PronounVerb("", "es")
