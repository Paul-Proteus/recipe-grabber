# CLAUDE.md

This file provides guidance for AI assistants working in this codebase.

## Project Overview

**recipe-grabber** is a Python tool that automates recipe extraction from images stored in Google Drive. It:
1. Queries a Google Drive folder for recipe images (HEIF format)
2. Sends images to OpenAI's GPT-4o vision model for analysis
3. (Planned) Stores extracted recipe data into a database

Status: Early-stage prototype. Google Drive integration is functional; OpenAI integration exists but is not yet wired end-to-end; database persistence is not yet implemented.

## Repository Structure

```
recipe-grabber/
├── main.py                  # Entry point — orchestrates the full pipeline
├── google_drive_client.py   # Google Drive API client (service account auth)
├── open_ai_client.py        # OpenAI GPT-4o vision client
├── requirements.txt         # Python dependencies (currently empty — see below)
├── credentials/             # Gitignored — holds secrets (never commit)
│   └── my_paths.py          # Local-only config: CREDENTIALS_PATH, GOOGLE_DRIVE_FOLDER_ID
├── .gitignore
├── LICENSE                  # MIT, Copyright Dylan Bergstrom 2024
└── README.md
```

## Setup Requirements

### Python Dependencies

`requirements.txt` is currently empty. The following packages must be installed manually:

```
google-api-python-client
google-auth-oauthlib
google-auth-httplib2
openai
```

Install with: `pip install google-api-python-client google-auth-oauthlib google-auth-httplib2 openai`

### Required Credentials (not in repo)

The `credentials/` directory is gitignored and must be created locally:

1. **`credentials/my_paths.py`** — defines two constants:
   ```python
   CREDENTIALS_PATH = "/path/to/service_account.json"
   GOOGLE_DRIVE_FOLDER_ID = "your_google_drive_folder_id"
   ```

2. **Google service account JSON** — a Google Cloud service account key file with Google Drive API access. The path is referenced by `CREDENTIALS_PATH`.

3. **`OPENAI_API_KEY` environment variable** — must be set before running anything that uses the OpenAI client.

## Key Files

### `main.py`
The entry point. Currently only runs the Google Drive listing step. The OpenAI client calls are commented out pending full pipeline integration.

### `google_drive_client.py`
- Class: `GoogleDriveClient`
- Authenticates using a Google service account JSON file
- `list_files(query: str)` accepts Google Drive API query syntax (e.g., `'<folder_id>' in parents and mimeType='image/heif'`)

### `open_ai_client.py`
- Class: `OpenAIClient`
- Uses GPT-4o with vision capabilities
- `get_image_analysis()` sends an image URL to GPT-4o and prints the response
- **Known bug**: `get_image_analysis()` uses the module-level `client` instead of `self.client`, so the `api_key` passed to the constructor has no effect
- Module-level constants: `DETAIL_HIGH`, `DETAIL_LOW`, `GPT_4O`, `TEST_IMAGE`, `API_KEY`

## Code Conventions

- Class-based architecture for API clients
- Private/internal methods prefixed with `_` (e.g., `_load_credentials`, `_create_client`)
- Constants in `UPPER_CASE` at module level
- Type hints on method parameters
- No test framework currently exists
- No linting or formatting tools are configured

## Development Workflow

There is no CI/CD pipeline, no automated tests, and no linting setup. The workflow is:

1. Set up credentials (see above)
2. Install dependencies manually
3. Run `python main.py`

## Known Issues and Planned Work

- `requirements.txt` is empty — dependencies need to be documented
- `OpenAIClient.get_image_analysis()` uses the module-level `client` instead of the instance's `self.client`
- No database integration implemented yet (README describes it as a goal)
- No error handling anywhere (API failures will raise uncaught exceptions)
- No tests
- `main.py` has trailing semicolons on import lines (style inconsistency)
- The OpenAI pipeline is not connected to the Google Drive output yet

## Sensitive Files — Never Commit

- Anything under `credentials/`
- `.env` files
- Any file containing API keys, OAuth tokens, or service account credentials
