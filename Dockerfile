# Start with slim Python 3.13 image
FROM python:3.13.10-slim

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set working directory
WORKDIR /app

# Add virtual environment to PATH so we can use installed packages
ENV PATH="/app/.venv/bin:$PATH"
s
# Copy dependency files firt (better layer caching)
COPY "pyproject.toml" "uv.lock" ".python-version" ".env" ./
# Install dependencies from lock file (ensures reproducible builds)
RUN uv sync --locked

# Copy application code
COPY script_dolar.py script_dolar.py

# Set entry point
ENTRYPOINT ["python", "script_dolar.py"]