from pathlib import Path

# Create a folder in current directory
for i in range(1, 26):
    folder = Path(f"day{i}")
    try:
        folder.mkdir()
    except FileExistsError:
        print(f"{folder} already exists")
        pass

    if not any(folder.iterdir()):
        (folder / "input_test.txt").touch()
        (folder / f"day{i}.ipynb").touch()