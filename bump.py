# bump.py: raise the last part of a version number by one.
def bump_patch(version):                       # version is text like "1.4.2"
    major, minor, patch = version.split(".")   # split at the dots: "1", "4", "2"
    new_patch = int(patch) + 1                 # int() turns the text "2" into the number 2; add 1
    return f"{major}.{minor}.{new_patch}"      # glue the parts back together: "1.4.3"
