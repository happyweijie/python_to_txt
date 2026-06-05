# Python to Text Converter

> For educational purposes 

Small command-line scripts for copying Python source files to `.txt` files, and
copying `.txt` files back to `.py` files.

The original input directory is never modified. Converted files are written to a
separate output directory while preserving the same folder structure.

## Scripts

- `py_to_txt.py`: copies every `.py` file to a matching `.txt` file.
- `txt_to_py.py`: copies every `.txt` file to a matching `.py` file.

Both scripts skip common generated/cache directories such as `__pycache__`,
`.git`, `.venv`, `venv`, `build`, and `dist`.

## Usage

Convert Python files to text files:

```powershell
python py_to_txt.py path/to/source_directory
```

By default, this writes to a sibling directory named:

```text
path/to/source_directory_txt
```

Convert text files back to Python files:

```powershell
python txt_to_py.py path/to/source_directory
```

By default, this writes to a sibling directory named:

```text
path/to/source_directory_py
```

## Custom Output Directory

Pass a second argument to choose the output directory yourself:

```powershell
python py_to_txt.py path/to/source_directory path/to/output_directory
python txt_to_py.py path/to/source_directory path/to/output_directory
```

The output directory must be separate from the source directory. It cannot be the
same directory or inside the source directory.

## Options

Preview what would be copied without writing files:

```powershell
python py_to_txt.py path/to/source_directory --dry-run
python txt_to_py.py path/to/source_directory --dry-run
```

Replace existing files in the output directory:

```powershell
python py_to_txt.py path/to/source_directory --overwrite
python txt_to_py.py path/to/source_directory --overwrite
```

Without `--overwrite`, the scripts stop if a target file already exists.

## Example

Input:

```text
leetcode/
  arrays/two_sum.py
  linked_list/reverse.py
```

Command:

```powershell
python py_to_txt.py leetcode
```

Output:

```text
leetcode_txt/
  arrays/two_sum.txt
  linked_list/reverse.txt
```
