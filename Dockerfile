FROM python:3.8.2-slim

ENV APP_DIR /hackmd-archive


# Adding backend directory to make absolute filepaths consistent across services
WORKDIR $APP_DIR

# Install Python dependencies
RUN pip install --no-cache-dir pipenv==2020.11.15
COPY Pipfile* $APP_DIR
RUN pipenv lock --keep-outdated --requirements > requirements.txt \
    && pip3 install --no-cache-dir --upgrade pip -r $APP_DIR/requirements.txt
COPY . $APP_DIR
CMD ["python3", "app/main.py", "sync_all_notes", "--enable-index"]
