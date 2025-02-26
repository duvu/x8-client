# Publishing to PyPI

This guide explains how to publish the x8-client package to PyPI.

## Prerequisites

1. Make sure you have an account on [PyPI](https://pypi.org/)
2. Install required tools:
   ```
   pip install build twine
   ```

## Steps to Publish

### 1. Update version number

Edit the version number in `x8/__init__.py`:

```python
__version__ = "0.1.0"  # Change this to the new version
```

### 2. Build the package

From the project root:

```bash
python -m build
```

This creates two files in the `dist/` directory:
- A source archive (`.tar.gz`)
- A wheel distribution (`.whl`)

### 3. Test the package

Before uploading to PyPI, you can upload to TestPyPI:

```bash
python -m twine upload --repository testpypi dist/*
```

Then install from TestPyPI to verify:

```bash
pip install --index-url https://test.pypi.org/simple/ x8-client
```

### 4. Upload to PyPI

Once you've verified everything works:

```bash
python -m twine upload dist/*
```

Enter your PyPI username and password when prompted.

### 5. Verify Installation

After publishing, verify your package can be installed:

```bash
pip install x8-client
```

## Troubleshooting

- If you get an error about version already existing, ensure you've incremented the version number
- If upload fails due to missing metadata, check your setup.py file
