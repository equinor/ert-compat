import warnings


def warn_ert_compat(modulename: str = None):
    msg = "Your code uses outdated import statements from ERT. You must fix this ASAP."
    if modulename is not None:
        msg += f"\nYou tried to import from the module: {modulename}"
    warnings.warn(msg, FutureWarning)
