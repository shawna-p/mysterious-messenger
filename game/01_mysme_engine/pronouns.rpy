init python:

    ## Note: for cleaner pronoun code, check out my In-Depth Pronouns code:
    ## https://feniksdev.itch.io/in-depth-pronouns-for-renpy
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
            return fem
        elif persistent.gender == "male" and persistent.pronoun == "he/him":
            return masc
        else:
            return neutral

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
