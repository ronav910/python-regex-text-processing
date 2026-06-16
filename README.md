# Python Regex Text Processing

Three regex utilities built with Python's `re` module covering validation, extraction, and substitution.

## Functions (`regex_utils.py`)

### `validate_email(searchstring)`
Validates a structured email format: `<name>.<employee_id><suffix>@<domain>`.
Returns `"valid"` or `"invalid"`.

```python
validate_email("john.123@vought.com")   # "valid"
validate_email("john.123@gmail.com")    # "invalid"
```

### `extract_author_book(searchstring)`
Extracts author name and book title from a string containing `"<Author> wrote <Title>"`.
Returns an `(author, title)` tuple, or `("noauthor", "noname")` if not found.

```python
extract_author_book("Stephen King wrote It")  # ('Stephen King', 'It')
```

### `age_up_text(searchstring)`
Replaces gendered youth terms preceded by a proper noun:
`Boy → Man`, `Girl → Woman` (case-sensitive). Returns `"nomatch"` if no substitution was made.

```python
age_up_text("Spider boy")   # "Spider man"
age_up_text("Wonder girl")  # "Wonder woman"
```

## Concepts demonstrated

- `re.fullmatch`, `re.search`, `re.sub` with callable replacement
- Named/unnamed capture groups
- Lookahead-free pattern design
- Case-preserving substitution via a replacement dictionary

## Requirements

Python 3.10+, no external dependencies.
