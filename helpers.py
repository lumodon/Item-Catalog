# Python currency conversion
# Citation: July 29th, 2019. https://stackoverflow.com/Questions/320929/currency-formatting-in-python
import locale


def currency_convert(number, dollar_sign=False):
    """
    Removes dollar sign from arbitrary string
    Formats string to match currency conventions
    Then if dollar_sign is True, changes back to standard string
    """
    locale.setlocale( locale.LC_ALL, '' )
    # Remove character from string
    # Citation: Aug 1st, 2019. https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
    converted_price = float(number.translate({ord('$'): None}))
    converted_price = locale.currency( converted_price )
    if not dollar_sign:
        converted_price = str(converted_price).translate(None, '$')
    return converted_price