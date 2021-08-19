FROM python:3.8.2

ENV BASE_DIR /usr/local
ENV APP_DIR $BASE_DIR/app


# Adding backend directory to make absolute filepaths consistent across services
WORKDIR $APP_DIR

# Install Python dependencies
RUN pip install pipenv
COPY Pipfile* $APP_DIR
RUN pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip3 install --upgrade pip -r $APP_DIR/requirements.txt
COPY . $APP_DIR
CMD ["python3", "app/main.py", "sync_all_notes", "--enable-index"]