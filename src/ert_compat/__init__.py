import warnings


def warn_ert_compat(modulename: str = None):
    msg = (
        "Usage of deprecated ERT API has been detected.\n"
        "Please reach out for help to fix this."
    )
    if modulename is not None:
        msg += f"\nThe deprecated module name was: {modulename}"
    warnings.warn(msg, FutureWarning)
