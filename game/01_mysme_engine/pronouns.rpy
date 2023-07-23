init python:

    ## Note: for cleaner pronoun code, check out my In-Depth Pronouns code:
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

    def set_pronouns():
        """Set the player's pronouns and pronoun variables."""

        global they, them, their, theirs, themself, they_re
        global They, Them, Their, Theirs, Themself, They_re
        global is_are, has_have, s_verb, do_does
        if persistent.pronoun == "she/her":
            they = "she"
            them = "her"
            their = "her"
            theirs = "hers"
            themself = "herself"
            they_re = "she's"
            is_are = "is"
            has_have = "has"
            do_does = "does"
            s_verb = "s"
        elif persistent.pronoun == "he/him":
            they = "he"
            them = "him"
            their = "his"
            theirs = "his"
            themself = "himself"
            they_re = "he's"
            is_are = "is"
            has_have = "has"
            do_does = "does"
            s_verb = "s"
        elif persistent.pronoun == "they/them":
            they = "they"
            them = "them"
            their = "their"
            theirs = "theirs"
            themself = "themself"
            they_re = "they're"
            is_are = "are"
            has_have = "have"
            do_does = "do"
            s_verb = ""
        # Set the capitalized versions
        They_re = string.capwords(they_re)
        They = string.capwords(they)
        Them = string.capwords(them)
        Their = string.capwords(their)
        Theirs = string.capwords(theirs)
        Themself = string.capwords(themself)
        # Save all variables
        renpy.retain_after_load()

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
