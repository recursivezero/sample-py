# Folder Tree Structure

````plaintext

└──/
     ├── CHANGELOG.md
     ├── LICENSE
     ├── LICENSE-PYTHON
     ├── README.md
     ├── WARP.md
     ├── assets/
     │    └── screenshots/
     ├── build-and-test.sh
     ├── check_import.py
     ├── debug_gemini.py
     ├── dist/
     │    ├── sample-3.4.7-py3-none-any.whl
     │    └── sample-3.4.7.tar.gz
     ├── docs/
     │    ├── AWS_integration.md
     ├── mypy.ini
     ├── packages.txt
     ├── poetry.lock
     ├── pyproject.toml
     ├── requirements.txt
     ├── ruff.toml
     ├── security-publish.sh
     ├── setup-hooks.sh
     ├── src/
     │    ├── __init__.py
     │    ├── api/
     │    │    ├── __init__.py
     │    │    ├── fast_api.py
     │    │    └── routes_helper.py
     │    ├── assets/
     │    │    ├── __init__.py
     │    │    └── images/
     │    │         ├── __init__.py
     │    │         ├── company_logo.png
     │    │         ├── generated/
     │    │         ├── sample/
     │    │         │    ├── __init__.py
     │    │         │    ├── card_samples/
     │    │         ├── sample_table_images/
     │    │         │    ├── group/
     │    │         │    └── single/
     │    │         └── uploaded/
     │    │              ├── group/
     │    │              └── single/
     │    ├── block_words
     │    ├── db/
     │    │    ├── __init__.py
     │    │    ├── connection.py
     │    │    ├── create_table.py
     │    │    └── delete_table.py
     │    ├── features/
     │    │    ├── __init__.py
     │    │    ├── audio_recorder/
     │    │    │    ├── __init__.py
     │    │    │    └── audio_recorder_ui.py
     │    │    ├── image_description/
     │    │    │    ├── __init__.py
     │    │    │    └── description.py
     │    │    ├── image_detection/
     │    │    │    ├── __init__.py
     │    │    │    ├── best.pt
     │    │    │    ├── color_transformer.py
     │    │    │    ├── image_detection_ui.py
     │    │    │    ├── oklch.py
     │    │    │    ├── trained_yolov12_model.pt
     │    │    │    └── visualizer.py
     │    │    ├── image_ocr/
     │    │    │    ├── __init__.py
     │    │    │    ├── business_cards.json
     │    │    │    └── ocr.py
     │    │    ├── image_search/
     │    │    │    ├── __init__.py
     │    │    │    ├── embedding_model.py
     │    │    │    ├── image_search_ui.py
     │    │    │    ├── schema.py
     │    │    │    └── vector_search.py
     │    │    ├── image_transformer/
     │    │    │    ├── __init__.py
     │    │    │    └── image_transformer_ui.py
     │    │    └── speech_to_text/
     │    │         ├── __init__.py
     │    │         └── speech_to_text_ui.py
     │    ├── sample/
     │    │    ├── __init__.py
     │    │    ├── __main__.py
     │    │    └── streamlit_app.py
     │    └── utils/
     │         ├── __init__.py
     │         ├── _version.py
     │         ├── aws_helper.py
     │         ├── blur.py
     │         ├── config_helper.py
     │         ├── constants.py
     │         ├── debug.py
     │         ├── exif_handler.py
     │         ├── github_models.py
     │         ├── helper.py
     │         ├── logger.py
     │         ├── messages.py
     │         ├── optional_check.py
     │         ├── profanity.py
     │         ├── shimmer_tile.py
     │         ├── time_middleware.py
     │         └── timing.py
     ├── static/
     │    └── index.css
     ├── templates/
     │    ├── doc.html
     │    └── index.html
     ├── trace_entry.py
     └── tz-script.code-workspace
     ```

````
