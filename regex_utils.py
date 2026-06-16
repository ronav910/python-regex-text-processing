import re


def validate_email(searchstring):
    """
    Validate a structured email address format.

    Expected format:
        <name>.<employee_id><suffix>@<domain>

    where:
        - name is 1-10 alphabetic characters
        - employee_id is a 3-digit number (100-799)
        - suffix is optional alphabetic characters
        - domain is one of: vought.com | godolkin.edu | fbsa.gov

    Args:
        searchstring: string to validate

    Returns:
        "valid" if the string matches the format, "invalid" otherwise
    """
    pattern = re.compile(
        r"[A-Za-z]{1,10}\.(?:[1-6]\d{2}|7\d{2})[A-Za-z]*@(?:vought\.com|godolkin\.edu|fbsa\.gov)"
    )
    return "valid" if pattern.fullmatch(searchstring) else "invalid"


def extract_author_book(searchstring):
    """
    Extract author name and book title from a natural-language string.

    Looks for the pattern: "<Author Name> wrote <Book Title>"

    Args:
        searchstring: string that may contain an authorship statement

    Returns:
        (author, title) tuple if found, ("noauthor", "noname") otherwise
    """
    pattern = re.compile(
        r"\b([A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*)?)\s+wrote\s+"
        r"(books|[A-Z0-9][A-Za-z0-9]*(?:\s+[A-Z0-9][A-Za-z0-9]*){0,2})\b"
    )
    match = pattern.search(searchstring)
    if not match:
        return ("noauthor", "noname")
    return (match.group(1).strip(), match.group(2).strip())


def age_up_text(searchstring):
    """
    Replace gendered youth terms with their adult equivalents.

    Replaces "Boy" → "Man", "Girl" → "Woman", "boy" → "man", "girl" → "woman"
    when the term is preceded by a capitalized word (e.g., a name or title).

    Args:
        searchstring: input string

    Returns:
        The string with replacements applied, or "nomatch" if no match was found
    """
    pattern = re.compile(r"\b([A-Z][A-Za-z0-9]*)\b(\s+)(Boy|Girl|boy|girl)\b")
    replacements = {"Boy": "Man", "Girl": "Woman", "boy": "man", "girl": "woman"}

    def repl(match):
        return f"{match.group(1)}{match.group(2)}{replacements[match.group(3)]}"

    result, count = pattern.subn(repl, searchstring)
    return result if count > 0 else "nomatch"


if __name__ == '__main__':
    print(validate_email("john.123@vought.com"))         # valid
    print(validate_email("john.123@gmail.com"))           # invalid

    print(extract_author_book("Stephen King wrote It"))   # ('Stephen King', 'It')
    print(extract_author_book("no author here"))          # ('noauthor', 'noname')

    print(age_up_text("Spider boy"))    # Spider man
    print(age_up_text("Wonder girl"))   # Wonder woman
    print(age_up_text("no match here")) # nomatch
