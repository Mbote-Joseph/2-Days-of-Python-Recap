# Dictionaries are a collection of key-value pairs.
# They are unordered, changeable and indexed.
# They are mutable.
# They are iterable.
# They are hashable.
# They are callable.
monthsConversions={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthsConversions["Jan"])
print(monthsConversions["Dec"])
print(monthsConversions.get("Dec"))