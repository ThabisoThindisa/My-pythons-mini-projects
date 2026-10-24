# Login and Registration App

## Windows setup

Run `setup.bat` once from this folder to create the project virtual
environment and install its dependencies. It uses the Python launcher to
select Python 3.14 and calls pip through that interpreter, so it does not use
the unrelated Python installation found first on `PATH`.

```powershell
.\setup.bat
.\.venv\Scripts\python.exe app.py
```

Do not use `py app.py` here: the Windows Python launcher selects its default
Python installation (currently Python 3.15), not this project's virtual
environment, so it cannot see the project's installed packages. The explicit
`.venv\Scripts\python.exe` command always runs the app with its dependencies.
Alternatively, activate the environment first and use `python app.py`; while
it is active, install additional packages with `python -m pip install PACKAGE`.
Outside the environment, bare `python` and `pip` currently resolve to Python
2.7 and pip 7.0.3, so do not use bare `pip install`.

For another project, create and activate its own environment with
`py -3.14 -m venv .venv` and `.\.venv\Scripts\Activate.ps1`. Making bare
`python` select Python 3 across all terminals and projects requires an
administrator to put Python 3 ahead of Python 2.7 in the machine `PATH`.
