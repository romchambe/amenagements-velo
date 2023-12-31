FROM python:3.11

# Install Miniconda
# Adaptation of the Miniconda install scripts urls and names might be needed depending on your machine's processor arch
RUN mkdir /usr/local/miniconda3 &&\
  wget -P /usr/local/miniconda3 https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh &&\
  sh /usr/local/miniconda3/Miniconda3-latest-Linux-aarch64.sh -b -u -p /usr/local/miniconda3 &&\
  rm -rf /usr/local/miniconda3/miniconda.sh

ENV PATH="/usr/local/miniconda3/bin:$PATH"

# Disable writing of bytecode files
ENV PYTHONDONTWRITEBYTECODE=1

# Install geopandas and psycopg with conda
RUN conda install --channel conda-forge psycopg2 geopandas

# Install standard python deps and start server
WORKDIR /code

COPY src src
COPY requirements.txt .
COPY alembic.ini .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]